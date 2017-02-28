import re
import random

class Eliza:
    reflections = {
        "am": "are",
        "was": "were",
        "i": "you",
        "i'd": "you would",
        "i've": "you have",
        "i'll": "you will",
        "my": "your",
        "are": "am",
        "you've": "I have",
        "you'll": "I will",
        "your": "my",
        "yours": "mine",
        "you": "me",
        "me": "you"
    }

    psychobabble = [

        [r'\bSelam\b|\bMerhaba\b.*',
         ["Merhaba.. Nasılsın?",
          "Selam, bugün kendini nasıl hissediyorsun?"]],

        [r'.*Nasılsın.*',
         ["İyiyim. Teşekkür ederim?"]],

        [r'(.*) ihtiyacım var',
         ["Neden {0} ihtiyacın var?",
          "{0} sana gerçekten iyi gelecek mi?",
          "{0} ihtiyacın olduğuna emin misin?"]],

        [r'Neden ([^\?]*)m.yorsun\??',
         ["Gerçekten {0}madığımımı düşünüyorsun?",
          "Belki sonunda {0}urum.",
          "Gerçekten {0}mamımı istiyorsun?"]],

        [r'Neden ([^\?]*).m.yorum\??',
         ["{0}abilmen gerektiğinimi düşünüyorsun?",
          "Eğer {0}abilseydin, ne yapardın?",
          "Bilmiyorum neden {0}amıyorsun?",
          "Gerçekten denedin mi?"]],

        [r'(.*).m.yorum',
         ["{0}amadığını nereden biliyorsun?",
          "Belkide denersen {0}abilirsin.",
          "{}man için ne gerekiyor?"]],

        [r'([^\?]*)m.s.n\??',
         ["{0} olup olmamam önemli mi?",
          "{0} olmamamı tercih ederdin?",
          "Belkide {0} olduğuma inanıyorsundur.",
          "{0} olabilirim. Sen ne düşünüyorsun?"]],

        [r'(.*).m',
         ["Buraya {0} olduğun için mi geldin?",
          "Ne kadar zamandır {0}sin?",
          "{0} olmakla ilgili ne düşünüyorsun?",
          "{0} olmak sana kendini nasıl hissettiriyor?"]],

        [r'Ne (.*)',
         ["Bu soruyo neden soruyorsun?",
          "Bu soruya cevap vermem sana nasıl yardımcı olacak?",
          "Sen ne düşünüyorsun"]],

        [r'Nasıl (.*)',
         ["Sen nasıl olduğunu düşünüyorsun?",
          "Belki kendi soruna kendin yanıt verebilirsin",
          "Gerçekten sormak isteğin ne?"]],

        [r'Çünk[iü] (.*)',
         ["Gerçek nedeni bumu?",
          "Başka ne tür nedenler aklına geliyor",
          "Eğer {0}san, başka ne gibi şeyler doğru?"]],

        [r'(.*) üzgünüm (.*)',
         ["Özür dilemeni gerektirmeyen zamanlar vardır.",
          "Özür dilerken ne hissediyorsun?"]],

        [r'I think (.*)',
         ["Do you doubt {0}?",
          "Do you really think so?",
          "But you're not sure {0}?"]],

        [r'(.*) friend (.*)',
         ["Tell me more about your friends.",
          "When you think of a friend, what comes to mind?",
          "Why don't you tell me about a childhood friend?"]],

        [r'Evet',
         ["Kendinden çok emin görünüyorsun.",
          "Tamam, ama biraz daha açıklayabilir misin?"]],

        [r'(.*) computer(.*)',
         ["Are you really talking about me?",
          "Does it seem strange to talk to a computer?",
          "How do computers make you feel?",
          "Do you feel threatened by computers?"]],

        [r'Is it (.*)',
         ["Do you think it is {0}?",
          "Perhaps it's {0} -- what do you think?",
          "If it were {0}, what would you do?",
          "It could well be that {0}."]],

        [r'It is (.*)',
         ["You seem very certain.",
          "If I told you that it probably isn't {0}, what would you feel?"]],

        [r'Can you ([^\?]*)\??',
         ["What makes you think I can't {0}?",
          "If I could {0}, then what?",
          "Why do you ask if I can {0}?"]],

        [r'Can I ([^\?]*)\??',
         ["Perhaps you don't want to {0}.",
          "Do you want to be able to {0}?",
          "If you could {0}, would you?"]],

        [r'You are (.*)',
         ["Why do you think I am {0}?",
          "Does it please you to think that I'm {0}?",
          "Perhaps you would like me to be {0}.",
          "Perhaps you're really talking about yourself?"]],

        [r'You\'?re (.*)',
         ["Why do you say I am {0}?",
          "Why do you think I am {0}?",
          "Are we talking about you, or me?"]],

        [r'I don\'?t (.*)',
         ["Don't you really {0}?",
          "Why don't you {0}?",
          "Do you want to {0}?"]],

        [r'I feel (.*)',
         ["Good, tell me more about these feelings.",
          "Do you often feel {0}?",
          "When do you usually feel {0}?",
          "When you feel {0}, what do you do?"]],

        [r'I have (.*)',
         ["Why do you tell me that you've {0}?",
          "Have you really {0}?",
          "Now that you have {0}, what will you do next?"]],

        [r'I would (.*)',
         ["Could you explain why you would {0}?",
          "Why would you {0}?",
          "Who else knows that you would {0}?"]],

        [r'Is there (.*)',
         ["Do you think there is {0}?",
          "It's likely that there is {0}.",
          "Would you like there to be {0}?"]],

        [r'My (.*)',
         ["I see, your {0}.",
          "Why do you say that your {0}?",
          "When your {0}, how do you feel?"]],

        [r'You (.*)',
         ["We should be discussing you, not me.",
          "Why do you say that about me?",
          "Why do you care whether I {0}?"]],

        [r'Why (.*)',
         ["Why don't you tell me the reason why {0}?",
          "Why do you think {0}?"]],

        [r'I want (.*)',
         ["What would it mean to you if you got {0}?",
          "Why do you want {0}?",
          "What would you do if you got {0}?",
          "If you got {0}, then what would you do?"]],

        [r'(.*) mother(.*)',
         ["Tell me more about your mother.",
          "What was your relationship with your mother like?",
          "How do you feel about your mother?",
          "How does this relate to your feelings today?",
          "Good family relations are important."]],

        [r'(.*) father(.*)',
         ["Tell me more about your father.",
          "How did your father make you feel?",
          "How do you feel about your father?",
          "Does your relationship with your father relate to your feelings today?",
          "Do you have trouble showing affection with your family?"]],

        [r'(.*) child(.*)',
         ["Did you have close friends as a child?",
          "What is your favorite childhood memory?",
          "Do you remember any dreams or nightmares from childhood?",
          "Did the other children sometimes tease you?",
          "How do you think your childhood experiences relate to your feelings today?"]],

        [r'(.*)\?',
         ["Bunu neden sordun?",
          "Belki de soruna kendin cevap verebilirsin.",
          "Belki de cevap senin içinde saklı?",
          "Neden sen söylemiyorsun?"]],

        [r'quit',
         ["Thank you for talking with me.",
          "Good-bye.",
          "Thank you, that will be $150.  Have a good day!"]],

        [r'(.*)',
         ["Lütfen biraz daha anlat.Please tell me more.",
          "Konuyu birazcık değiştirelim. Bana biraz ailenden bahset.",
          "Biraz daha açıklayabilir misin?",
          "Neden bunu söyledin?",
          "Anlıyorum.I see.",
          "Çok ilginç.",
          "Bu sana kendini nasıl hissettiriyor?",
          "Bunu söylediğinde ne düşünüyorsun?"]]
    ]


    def reflect(self,fragment):
        tokens = fragment.lower().split()
        for i, token in enumerate(tokens):
            if token in self.reflections:
                tokens[i] = self.reflections[token]
        return ' '.join(tokens)


    def analyze(self,statement):
        for pattern, responses in self.psychobabble:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = responses[0]
                print("Response:", response)
                return response.format(*[self.reflect(g) for g in match.groups()])

    def toNeg(root):
        pass


