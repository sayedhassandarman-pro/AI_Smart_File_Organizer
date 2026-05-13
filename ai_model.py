from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

class AIModel:
    def __init__(self):
        data = [
            ("invoice pdf bill document txt", "Documents"),
            ("photo image jpg png selfie pic", "Images"),
            ("movie video clip film", "Videos"),
            ("music song mp3 audio", "Audio"),
        ]

        X = [i[0] for i in data]
        y = [i[1] for i in data]

        self.model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        self.model.fit(X, y)

    def predict(self, text):
        return self.model.predict([text])[0]