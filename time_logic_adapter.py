from chatterbot.logic.logic_adapter import LogicAdapter
from datetime import datetime

class TimeLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(TimeLogicAdapter, self).__init__(**kwargs)
        from nltk import NaiveBayesClassifier

        self.positive = [
            'Saat kaç?',
            'Saatin kaç olduğunu söyleyebilir misin?',
            'Saatin kaç olduğunu biliyor musun?'
        ]

        self.negative = [
            'Zaman ne kadar da çabuk geçiyor',
            'Kaç yaşındasın',
            'Zamanın var mı?',
            'Saatin var mı?',
            "Ders kaçta başlıyor"
            "Bölüm mail adresimi söyleyebilir misin?"
        ]

        labeled_data = (
            [(name, 0) for name in self.negative] +
            [(name, 1) for name in self.positive]
        )
        # train_set = apply_features(self.time_question_features, training_data)
        train_set = [(self.time_question_features(n), text) for (n, text) in labeled_data]
        self.classifier = NaiveBayesClassifier.train(train_set)

    def time_question_features(self, text):
        """
        Provide an analysis of significan features in the string.
        """
        features = {}
        # extract fetures, whether contains the word, has the letter
        all_words = " ".join(self.positive + self.negative).split()
        for word in text.split():
            features['contains({})'.format(word)] = (word in all_words)

        for letter in 'abcçdefgğhıijklmnoöprsştuüvyz':
            features['count({})'.format(letter)] = text.lower().count(letter)
            features['has({})'.format(letter)] = (letter in text.lower())

        return features

    def process(self, statement):
        from chatterbot.conversation import Statement

        now = datetime.now()

        time_features = self.time_question_features(statement.text.lower())
        confidence = self.classifier.classify(time_features)
        response = Statement('Saat ' + now.strftime('%H:%M'))

        return confidence, response