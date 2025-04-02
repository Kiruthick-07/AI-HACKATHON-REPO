import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords

nltk.download('stopwords')
dataset_path = r"E:\vs code\AI HACKATHON\AI-HACKATHON-REPO\refined_news_dataset.csv"

df = pd.read_csv(dataset_path)

news_texts = df["Headline"].astype(str).tolist()
news_labels = df["Category"].astype(str).tolist()
vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
X_train = vectorizer.fit_transform(news_texts)

model = MultinomialNB()
model.fit(X_train, news_labels)

while True:
    new_news = input("\nEnter a news headline to classify (or type 'exit' to quit): ")
    if new_news.lower() == 'exit':
        break
    

    X_new = vectorizer.transform([new_news])
    prediction = model.predict(X_new)
    
    print("Predicted Category:", prediction[0])
