from chatterbot.logic.logic_adapter import LogicAdapter
from database.database import DataBase
from preprocessing.stemmer import Stemmer
import chatterbot.comparisons as comparisons
from chatterbot.conversation import Statement

class VectorLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(VectorLogicAdapter, self).__init__(**kwargs)
        self.db = DataBase()
        self.stemmer = Stemmer()

    def getVector(self,tokens,info):
        vec = [0 for x in range(200)]
        for t in tokens:
            v = self.db.getVector(t)
            if v is None:
                v = self.db.getVector(self.stemmer.stem(t))
            if v is not None:
                vec = [x + y for x, y in zip(vec, v)]
            elif info:
                pass
                # print("No vector for word", t,"or",self.stemmer.stem(t))
        return vec

    def cosine_similarity(self,vec1, vec2):
        dot = sum(x * y for x, y in zip(vec1, vec2))
        mag1 = sum(x * x for x in vec1) ** 0.5
        mag2 = sum(y * y for y in vec2) ** 0.5
        div = mag1 * mag2
        if div == 0:
            return 0
        return dot / div

    def getStatementVec(self,statement):
        vec = self.db.getSentenceVector(statement.text)
        if vec is None:
            t = self.__tokenize(statement.text)
            vec = self.getVector(t, False)
            self.db.cacheSentence(statement.text, vec)
        return vec

    def get(self, input_statement):
        statement_list = self.chatbot.storage.get_response_statements()

        if not statement_list:
            if self.chatbot.storage.count():
                # Use a randomly picked statement
                self.logger.info(
                    'No statements have known responses. ' +
                    'Choosing a random response to return.'
                )
                random_response = self.chatbot.storage.get_random()
                random_response.confidence = 0
                return random_response
            else:
                raise self.EmptyDatasetException()

        closest_match = input_statement
        closest_match.confidence = 0
        closest_match.lev = 0
        closest_match.cos = 0
        # Find the closest matching known statement
        questionVector = self.getVector(input_statement.tokens, True)
        if not all(x == 0 for x in questionVector):
            # If there is a vector for the statement compare it with all other
            # statements in the database
            for statement in statement_list:
                vec = self.getStatementVec(statement)
                lev_similarity = comparisons.levenshtein_distance(Statement(input_statement.text),
                                                                  Statement(statement.text))
                cosine_similarity = self.cosine_similarity(questionVector, vec)
                # normalize
                cosine_similarity = (cosine_similarity + 1) / 2
                if all(x == 0 for x in vec):
                    # There is no vector for the statement so the comparison is meaningless
                    lev_similarity = 0
                    cosine_similarity = 0

                # print(statement.text,cosine_similarity,lev_similarity)
                if cosine_similarity > closest_match.cos:
                    closest_match = statement
                    closest_match.lev = lev_similarity
                    closest_match.cos = cosine_similarity
                elif abs(cosine_similarity - closest_match.cos) < 0.01 and lev_similarity > closest_match.lev:
                    closest_match = statement
                    closest_match.lev = lev_similarity
                    closest_match.cos = cosine_similarity

        closest_match.confidence = closest_match.cos
        print("Closest Match:", closest_match,\
              "Lev:",closest_match.lev, \
              "Cos:",closest_match.cos, "Confidence:",closest_match.confidence)
        return closest_match

    def process(self,input_statement):

        input_statement.tokens = self.__tokenize(input_statement.text)
        # Select the closest match to the input statement
        # print("Selecting closest match")
        closest_match = self.get(input_statement)
        self.logger.info('Using "{}" as a close match to "{}"'.format(
            input_statement.text, closest_match.text
        ))

        # Get all statements that are in response to the closest match
        response_list = self.chatbot.storage.filter(
            in_response_to__contains=closest_match.text
        )
        if response_list:
            self.logger.info(
                'Selecting response from {} optimal responses.'.format(
                    len(response_list)
                )
            )
            response = self.select_response(input_statement, response_list)
            response.confidence = closest_match.confidence
            self.logger.info('Response selected. Using "{}"'.format(response.text))
        else:
            response = self.chatbot.storage.get_random()
            self.logger.info(
                'No response to "{}" found. Selecting a random response.'.format(
                    closest_match.text
                )
            )

            # Set confidence to zero because a random response is selected
            response.confidence = 0
        print("Confidence",response,response.confidence)
        return response.confidence, response

    def __tokenize(self,text):
        import re
        punctuations = (r"\.", r":", r";", r"\?", ",", "!")
        tokens = []
        text = text.lower().strip()
        # processed = re.sub(r'<.*>', '', text)
        for p in punctuations:
            text = re.sub(p, " " + p.replace("\\", ""), text)
        tokens += [t for t in re.split(" +", text) if t != ""]
        return tokens

#
# adapter = VectorLogicAdapter()
# text1 = Question("Yapay Anlayışın Temelleri dersinin kodu")
# text2 = Question("merhaba")
# vector1 = adapter.getVector(text1.cleanTokenized,True)
# vector2 = adapter.getVector(text2.cleanTokenized,True)
#
# import numpy as np
# numvector1 = np.array(vector1)
# numvector2 = np.array(vector2)
#
# print("hohey")
# from sklearn.metrics.pairwise import cosine_similarity
#
# asd = cosine_similarity(numvector1.reshape(1,-1),numvector2.reshape(1,-1))
# print("Sklearn",asd)
#
# import matching.comparison as COMPARE
# cosine = COMPARE.cosine_similarity(vector1,vector2)
# print("Mine", cosine)
