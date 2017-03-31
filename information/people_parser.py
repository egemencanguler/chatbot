
path = "../conversation_data/info.txt"
file = open(path,"r")

person = {}
lines = file.readlines()

titles = [lines[i].strip() for i in range(len(lines)) if lines[i].find("Doçent") != -1 or lines[i].find("Profesör") != -1]
mailes = [lines[i+1].replace("[at]","@").strip() for i in range(len(lines)) if lines[i].find("E-Posta") != -1]
tels = [lines[i+1].strip() for i in range(len(lines)) if lines[i].find("Tel :") != -1]
offices = [lines[i+1].strip() for i in range(len(lines)) if lines[i].find("Ofis") != -1]
webSites = [lines[i+1].strip() for i in range(len(lines)) if lines[i].find("Web Sitesi") != -1]
researchAreas = [lines[i].split("Araştırma Alanları :")[1].strip() for i in range(len(lines)) if lines[i].find("Araştırma Alanları") != -1]

for title,mail,tel,office,webSite,research in zip(titles,mailes,tels,offices,webSites,researchAreas):
    # print(title)
    name = ""
    if title.find("Doçent") != -1:
        name = title.split("Doçent")[1].strip()
    else:
        name = title.split("Profesör")[1].strip()
    person[name] = {}
    person[name]["title"] = title
    person[name]["mail"] = mail
    person[name]["tel"] = tel
    person[name]["office"] = office
    person[name]["website"] = webSite
    person[name]["research"] = research

print(person)
file.close()