# Statement tokens
STOKEN_STUDENT_NO = "{StudentNo}"
STOKEN_COURSE_CODE = "{CourceCode}"
STOKEN_COURSE_NAME = "{CourseName}"
STOKEN_CLASSROOM = "{Classroom}"

STATEMENT_TOKENS = [STOKEN_STUDENT_NO, STOKEN_COURSE_CODE, STOKEN_COURSE_NAME, STOKEN_CLASSROOM]

# Answer tokens
ATOKEN_COURCE_INFO = "{CourseInfo}"
ATOKEN_CLASSROOM_FLOOR_INFO = "{ClassroomFloor}"

ANSWER_TOKENS = [ATOKEN_COURCE_INFO, ATOKEN_CLASSROOM_FLOOR_INFO]

INFOS = {"d1":"bodrum", "d2": "bodrum", "d3": "bodrum", "d4": "bodrum",
                 "d5": "zemin", "d6": "zemin", "d7": "zemin",
                 "d8": "1.", "d9":"1.",
                 "d10": "2."}

class InformationManager:
    # Singleton
    __instance = None
    def __new__(cls):
        if InformationManager.__instance is None:
            InformationManager.__instance = object.__new__(cls)
            InformationManager.__instance.statementTokens = {}
        return InformationManager.__instance

    def putTokenValue(self,statementToken, value):
        self.statementTokens[statementToken] = value

    def getTokenValue(self,statementToken):
        if statementToken in self.statementTokens:
            return self.statementTokens[statementToken]
        return None

    def getInfo(self,answerToken):
        if answerToken == ATOKEN_CLASSROOM_FLOOR_INFO:
            return INFOS[self.getTokenValue(STOKEN_CLASSROOM)]
        return "INFO"


