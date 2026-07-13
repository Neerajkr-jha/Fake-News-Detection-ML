import streamlit as st
import pickle
import re
import string

# Load model and vectorizer
model = pickle.load(open("logistic_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))


def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\w*\d\w*', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="centered"
)

st.title("📰 Fake News Detection")

st.write("Paste a news article below and click **Check News**.")

news = st.text_area("News Article", height=250)

if st.button("Check News"):

    if news.strip() == "":
        st.warning("Please enter some news.")
    else:

        cleaned = wordopt(news)

        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)

        probability = model.predict_proba(vector)

        if prediction[0] == 1:
            st.success("NOT FAKE NEWS")
            st.write(f"Confidence : {probability[0][1]*100:.2f}%")
        else:
            st.error("FAKE NEWS")
            st.write(f"Confidence : {probability[0][0]*100:.2f}%")