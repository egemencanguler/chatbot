# Dependencies
  - Install python driver of mongodb https://docs.mongodb.com/ecosystem/drivers/python/
  - Install chatterbot http://chatterbot.readthedocs.io/en/stable/setup.html
  - Install flask http://flask.pocoo.org/
  - Download word vectors from http://people.csail.mit.edu/karthikn/data/vectors_gencor.tur.txt

# Setup
  - open setup.py and change the VECTOR_PATH variable to the path of the vector file you have downloaded
- Start mongodb
- Run setup.py. Be patient it's going to take a while. You can follow the process from output.
- Run train.py. It trains the bot with the questions inside questions.txt which is located under conversation_data folder
- Run test.py. Type your question and bot will return an answer with debug information
- Run app.py and open the address prompted. It’s a simple web interface. Ask a question and test if everything is working.
# How Does It Work
First, read the chatterbot’s documentation http://chatterbot.readthedocs.io/en/stable/
There are 3 logic adapters; fixed,no answer and vector. In our case most important one is the vector logic adapter. It compares the users’ questions with all the questions in our database. It sums up word vectors for each word inside the question. Then it calculates normalized cosine similarities and levenstein distance between the asked question and the questions inside the database. It uses a two level comparison logic. First compare the cosine similarities if the differences between cosine similarities is not significant compare levenshtein similarities and returns the closest match.

# Questions
In order to add new questions. Open the conversation_data/questions.txt and add questions in the following format

```

#Comment
<Question>
<Answer>
*

```
Use place holders for similar questions. Don’t type
```
D1 dersliği hangi katta?
Bodrum katta
*
D2 dersliği hangi katta?
Bodrum katta
*
```
Instead use
```
<Classroom> dersliği hangi katta?
<ClassroomLoc> katta
```
You can find all the placeholders and corresponding informations under the information.py. You can also add your own place holders and change the conversation helper's multiply function accordingly. There is no easier way yet but it can be implemented.

# Information Extraction
There are two parser available; people and course parsers. They don’t have a specified structure.They are just implemented to parse course and people infos from http://www.cs.hacettepe.edu.tr/index_tr.html

# Web Implementation
```
POST {base_url}/ask
Response = "<Question></><Answer>"
```
Send question data inside request body with key “question”. Split response text with "</>" fist part is the question asked second part is the answer.

# Problems:
Question with same structures but different answers
Example Question Database:
```
Burcu hocanın telefon numarası ney?
0312********
*
Bölüme nasıl ulaşırım?
Çayyolu metrosu
*
```

If user asks the question “Burcu hocaya nasıl ulaşırım?”
Our bot thinks, the question matches better with "Bölüme nasıl ulaşırım". It might be because of the named entities. Vectors training data is not trained for our purpose, thus word “Burcu” don’t have a useful vector.

---
There is no structured way to extract and update information. There is also a need to update placeholders after updating the information data.

---
No user interface to edit and update question database.

---

Spelling correction and text normalization is missing. People tend to asks very short questions so every word is very important for us. Even a single mistyped word can affect the result dramatically.

---
Bot does not  have a mechanishm to store the unanswered questions. We can store a question if we don’t have the answers for it. It helps us to understand users need and act accordingly in the future development.
