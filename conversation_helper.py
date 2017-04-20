import re
import information.information as INFO
def checkPlaceHolders(line):
    placeHolders = INFO.QUESTION_PLACEHOLDERS + INFO.ANSWER_PLACEHOLDERS
    for p in re.findall("(<[^<>]*>)",line):
        if p not in placeHolders:
            print("*****Undefined placeholder*****",p)


def importConversations(filePath):
    # Conversations
    conversations = []
    file = open(filePath,"r",encoding="utf-8")
    line = file.readline()
    type = ""
    con = []
    while line:
        if line.startswith("#"):
            print("\n" + line.strip())
        elif line.startswith("*"):
            # End of a question answer pair
            print("New Conversation", con)
            conversations.extend(multiplyConversation(con))
            con = []
        else:
            checkPlaceHolders(line)
            con.append(line.strip())
        line = file.readline()
    print(conversations)
    return conversations

def multiplyConversation(con):
    question = con[0]
    if question.find(INFO.Q_NAME) != -1:
        variations = []
        for name in INFO.PEOPLE.keys():
            variations.append([question.replace(INFO.Q_NAME,name),con[1]])
        return variations
    if question.find(INFO.Q_COURSE_NAME) != -1:
        variations = []
        for name in INFO.COURSES.keys():
            variations.append([question.replace(INFO.Q_COURSE_NAME, name), con[1]])
        return variations
    if question.find(INFO.Q_COURSE_CODE) != -1:
        variations = []
        for name in [INFO.COURSES[x]["code"] for x in INFO.COURSES.keys()]:
            variations.append([question.replace(INFO.Q_COURSE_CODE, name), con[1]])
        return variations
    return [con]