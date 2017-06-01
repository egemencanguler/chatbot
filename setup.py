VECTOR_PATH = "/Users/macbook/Desktop/vectors_gencor.tur.txt"

file = open(VECTOR_PATH,"r")

from database.database import DataBase
db = DataBase()
# print(db.getVector("</s>"))
#
NUMBER_OF_VECTORS = 725674.0
counter = 0
lines = []
for line in file:
    tokens = line.split(" ")
    word = tokens[0]
    vector = []
    for i in range(1,201):
        data = tokens[i].strip()
        vector.append(float(data))
    db.insertVector(word,vector)
    print((counter/NUMBER_OF_VECTORS) * 100)
    counter += 1
file.close()