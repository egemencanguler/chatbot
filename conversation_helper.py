import io

def generateFromTerminal():
    filePath = "conversation.txt"

    line = ""
    while line != "yes":
        print("Please enter a file path")
        filePath = input()
        print("File path is ", filePath)
        print("Write yes to continue anything else to reenter the file path")
        line = input()

    print("Now, you can start to enter the conversation, type * to end the conversation and type end to exit the program")
    file = open(filePath, "w", encoding= "utf-8")
    line = ""
    conversation = []
    while line != "end":
        line = input()
        if line == "*":
            print(conversation)
            file.writelines(conversation)
            file.write("\n")
            conversation = []
        else:
            conversation.append(line + "\n")
    file.close()



def importConversations(filePath):
    file = open(filePath,"r",encoding="utf-8")
    conversations = []
    con = []
    for l in file:
        if l == "\n":
            conversations.append(con)
            con = []
        else:
            con.append(l)
    file.close()
    if len(conversations) == 0:
        conversations.append(con)
    return conversations

def exportConversations(filePath,conversations):
    file = open(filePath, "w", encoding="utf-8")
    for c in conversations:
        file.writelines(c)
        file.write("\n")
    file.close()
