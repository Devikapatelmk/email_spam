import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Sample training data (you can add more)
data = {
    'text': [
        "Win a free iPhone now!",
        "Congratulations you won",
        "Claim your prize",
        "Hello, how are you?",
        "Let's meet tomorrow",
        "Are you coming to the office?"
    ],
    'label': [1, 1, 1, 0, 0, 0]  # 1 = spam, 0 = ham
}

df = pd.DataFrame(data)

cv = CountVectorizer()
X = cv.fit_transform(df['text'])
y = df['label']

model = MultinomialNB()
model.fit(X, y)

# Save model & vectorizer
joblib.dump(model, "models/spam_model.pkl")
joblib.dump(cv, "models/vectorizer.pkl")

print("Model saved!")
