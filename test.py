import information as Info

# im = Info.InformationManager()
#
#
# preTests = [
#     ["21228357",Info.STOKEN_STUDENT_NO, "21228357"]
#     ,["bbm203", Info.STOKEN_COURSE_CODE, "bbm203"]
#     ,["fiz137", Info.STOKEN_COURSE_CODE, "fiz137"]
#     ,["tkd103", Info.STOKEN_COURSE_CODE, "tkd103"]
#     ,["BEB 650", Info.STOKEN_COURSE_CODE, "beb650"]
#
#     ,[r'd3',Info.STOKEN_CLASSROOM, "d3"]
#     ,[r'd 3', Info.STOKEN_CLASSROOM, "d3"]
#     ,[r'derslik 3', Info.STOKEN_CLASSROOM, "d3"]
# ]
# for inputStatement, expectedToken, expectedTokenValue in preTests:
#     token = preprocessor.process(inputStatement)
#     tokenValue = im.getTokenValue(expectedToken)
#     if expectedToken != token or expectedTokenValue != tokenValue:
#         print("Error in preprocessor test case:")
#         print("Input: ", inputStatement)
#         print("Expected token: ", expectedToken)
#         print("False token: ", token)
#         print("Expected token value: ",expectedTokenValue )
#         print("False token value: ", tokenValue)
#         print("------")
#
# from postprocessor import Postprocessor
#
# postProcessor = Postprocessor()
# postTests = [
#     [Info.STOKEN_STUDENT_NO, "21228357"]
#     ,[Info.STOKEN_COURSE_CODE, "beb650"]
#     ,[Info.STOKEN_CLASSROOM, "d3"]
#
#     ,[Info.ATOKEN_CLASSROOM_FLOOR_INFO, "bodrum"]
# ]
#
# for postIn, postOut in postTests:
#     out = postProcessor.process(postIn)
#     if postOut != out:
#         print("Error in post processor test case:")
#         print("In:", postIn, " Out:", postOut)
#         print("False out", out)