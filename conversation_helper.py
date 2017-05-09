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
    # Replace placeholders
    question = con[0]
    answer = con[1]
    qMatch = re.search("(<[^>]*>)",question)
    aMatch = re.search("(<[^>]*>)",answer)
    if qMatch:
        qPlaceHolder = qMatch.group(1)
        variations = []
        if qPlaceHolder == INFO.Q_NAME:
            for name in INFO.PEOPLE.keys():
                a = answer
                if aMatch:
                    aPlaceHolder = aMatch.group(1)
                    a = answer.replace(aPlaceHolder,INFO.PEOPLE[name][aPlaceHolder])
                variations.append([question.replace(INFO.Q_NAME, name), a])
            return variations
        elif qPlaceHolder == INFO.Q_COURSE_NAME:
            variations = []
            for name in INFO.COURSES.keys():
                a = answer
                if aMatch:
                    aPlaceHolder = aMatch.group(1)
                    a = answer.replace(aPlaceHolder, INFO.COURSES[name][aPlaceHolder])
                variations.append([question.replace(INFO.Q_COURSE_NAME, name), a])
            return variations
        elif qPlaceHolder == INFO.Q_COURSE_CODE:
            variations = []
            for name, code in [[x, INFO.COURSES[x]["<CourseCode>"]] for x in INFO.COURSES.keys()]:
                a = answer
                if aMatch:
                    aPlaceHolder = aMatch.group(1)
                    a = answer.replace(aPlaceHolder, INFO.COURSES[name][aPlaceHolder])
                variations.append([question.replace(INFO.Q_COURSE_CODE, code), a])
            return variations
        elif qPlaceHolder == INFO.Q_CLASSROOM:
            variations = []
            for classroom in INFO.LOCATIONS.keys():
                a = answer
                if aMatch:
                    aPlaceHolder = aMatch.group(1)
                    a = answer.replace(aPlaceHolder, INFO.LOCATIONS[classroom])
                variations.append([question.replace(INFO.Q_CLASSROOM, classroom), a])
                print(variations)
            return variations
    return [con]


# con = importConversations("./conversation_data/questions.txt")
# for c in con:
#     print(c)