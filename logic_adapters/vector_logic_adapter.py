from chatterbot.logic.logic_adapter import LogicAdapter
from database.database import DataBase
from preprocessing.preprocessor import Preprocessor
from containers.question import Question
from chatterbot.comparisons import levenshtein_distance
from chatterbot.conversation import Statement

class VectorLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(VectorLogicAdapter, self).__init__(**kwargs)
        self.db = DataBase()
        self.preprocessor = Preprocessor()

    def getVector(self,text):
        tokens = self.preprocessor.tokenize(text)
        vec = [0 for x in range(200)]
        for t in tokens:
            v = self.db.getVector(t)
            if v is None:
                v = self.db.getVector(self.preprocessor.stemmer.stem(t))
            if v is not None:
                vec = [x + y for x, y in zip(vec, v)]
        if vec  == [0 for x in range(200)]:
            print("No Vector for " + text)
            pass
        return vec

    def cosine_similarity(self,vec1, vec2):
        dot = sum(x * y for x, y in zip(vec1, vec2))
        mag1 = sum(x * x for x in vec1) ** 0.5
        mag2 = sum(y * y for y in vec2) ** 0.5
        div = mag1 * mag2
        if div == 0:
            return 0
        return dot / div

    def compare(self, text1, text2):
        text1 = text1.lower()
        text2 = text2.lower()
        vec1 = self.getVector(text1)
        vec2 = self.getVector(text2)
        return self.cosine_similarity(vec1, vec2)

    def get(self, input_statement):
        """
        Takes a statement string and a list of statement strings.
        Returns the closest matching statement from the list.
        """
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
        # Find the closest matching known statement
        for statement in statement_list:
            statement.question = self.preprocessor.process(statement.text)

            lev_similarity = levenshtein_distance(Statement(input_statement.question.processed.lower()),Statement(statement.question.processed))
            cosine_similarity = self.compare(input_statement.question.processed, statement.question.processed)

            # confidence = max(cosine_similarity,lev_similarity)
            confidence = cosine_similarity
            # if lev_similarity == 1:
            #     confidence = lev_similarity

            if confidence > closest_match.confidence:
                statement.confidence = confidence
                closest_match = statement

        return closest_match

    def process(self,input_statement):

        input_statement.question = self.preprocessor.process(input_statement.text)

        # Select the closest match to the input statement
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
