from chatterbot.logic.logic_adapter import LogicAdapter
from database.database import DataBase
from preprocessing.stemmer import Stemmer
from containers.question import Question
import chatterbot.comparisons as comparisons
from chatterbot.conversation import Statement

class VectorLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(VectorLogicAdapter, self).__init__(**kwargs)
        self.db = DataBase()
        self.stemmer = Stemmer()
        self.cache = {}

    def getVector(self,tokens,info):
        vec = [0 for x in range(200)]
        for t in tokens:
            v = self.db.getVector(t)
            if v is None:
                v = self.db.getVector(self.stemmer.stem(t))
            if v is not None:
                vec = [x + y for x, y in zip(vec, v)]
            elif info:
                print("No vector for word", t,"or",self.stemmer.stem(t))
        return vec

    def cosine_similarity(self,vec1, vec2):
        dot = sum(x * y for x, y in zip(vec1, vec2))
        mag1 = sum(x * x for x in vec1) ** 0.5
        mag2 = sum(y * y for y in vec2) ** 0.5
        div = mag1 * mag2
        if div == 0:
            return 0
        return dot / div


    def get(self, input_statement):
        """
        Takes a statement string and a list of statement strings.
        Returns the closest matching statement from the list.
        """
        print("Get Response Statements")
        statement_list = self.chatbot.storage.get_response_statements()
        print("Get Response Statements End")

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
        # Find the closest matching known statement
        questionVector = self.getVector(input_statement.question.cleanTokenized,True)
        print("Comparing...")
        for statement in statement_list:
            statement.question = Question(statement.text)
            lev1 = Statement(input_statement.question.withPlaceHolders)
            lev2 = Statement(statement.question.withPlaceHolders)
            lev_similarity = comparisons.levenshtein_distance(lev1,lev2)
            vec = None
            # TODO remove hacky implementation of caching, there are better aproaches.
            if statement.question.clean in self.cache:
                vec = self.cache[statement.question.clean]
            else:
                vec = self.getVector(statement.question.cleanTokenized,False)
                self.cache[statement.question.clean] = vec
            cosine_similarity = self.cosine_similarity(questionVector,vec)
            #normalize
            cosine_similarity = (cosine_similarity + 1) / 2
            confidence = cosine_similarity
            #print(statement.text,cosine_similarity,lev_similarity)
            # print(statement.text,cosine_similarity,lev_similarity)
            if confidence > closest_match.confidence:
                statement.confidence = confidence
                closest_match = statement
        print("Comparing is done")
        return closest_match

    def process(self,input_statement):

        input_statement.question = self.chatbot.question

        # Select the closest match to the input statement
        print("Selecting closest match")
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
        print("Confidence",response.confidence)
        return response.confidence, response

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
