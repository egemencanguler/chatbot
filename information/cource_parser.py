

def clean(text):
    return text.replace("I","1").replace("II","2").replace("İ","i")\
        .replace("-","").strip()


import re
path = "../conversation_data/info.txt"
file = open(path,"r")

courses = {}

counter = 0
line = file.readline()
while line:
    match = re.match("([a-zA-ZİŞÇĞ]{3}\d{3})([^\(]*)\(([\d ]*)\)",line)
    if match:
        print(match.groups())
        counter += 1
        file.readline()
        file.readline()
        info = file.readline()
        course = {}
        course["code"] = clean(match.group(1))
        course["name"] = clean(match.group(2))
        course["credit"] = clean(match.group(3))
        course["info"] = info
        courses[course["name"]] = course
    line = file.readline()

print(courses)
print(counter)

file.close()
