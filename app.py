import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

nltk.download('punkt')

ps = PorterStemmer()
tv = pickle.load(open("Model/Vectorizer.pkl", "rb"))
model = pickle.load(open("Model/model.pkl", "rb"))


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []

    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    ps = PorterStemmer()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter your message")

if st.button("run"):
    # Preprocessing
    transformed_text = transform_text(input_sms)

    #Vectorization
    vector_input = tv.transform([transformed_text])

    #predict
    result = model.predict(vector_input)

    #display
    if result == 0:
        st.header("Not a Spam Message")
    else:
        st.header("Spam Message")