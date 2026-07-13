#  Fake News Detection System Using Machine Learning

A Machine Learning-powered web application that classifies news articles as **FAKE** or **NOT FAKE** using Natural Language Processing (NLP). The system preprocesses raw news text, converts it into numerical features using **TF-IDF Vectorization**, and predicts its authenticity using a trained **Logistic Regression** model through an interactive **Streamlit** interface.

---

##  Features

-  Classify news articles as **Fake** or **Not Fake** in real time.
-  Fast prediction using a pre-trained Machine Learning model.
-  Automatic text preprocessing (removes URLs, punctuation, HTML tags, numbers, etc.).
-  TF-IDF based feature extraction for textual representation.
-  Interactive and user-friendly Streamlit web interface.
-  Pre-trained model and vectorizer loaded using Pickle for instant inference.

---

##  Tech Stack

- **Language:** Python
- **Machine Learning:** Scikit-Learn
- **NLP:** TF-IDF Vectorization
- **Data Processing:** Pandas, NumPy
- **Frontend:** Streamlit
- **Model Serialization:** Pickle
- **Development Environment:** Visual Studio Code

---

## 📂 Project Structure

```text
Fake-News-Detection-ML/
│
├── Dataset/
│   ├── Fake.csv
│   └── True.csv
│
├── app.py
├── fake_news_detection.ipynb
├── fake_news_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
└── .gitignore

📊 Dataset

The model is trained using the Fake and Real News Dataset available on Kaggle.

Dataset Statistics:

Fake News: 23,481 articles
Real News: 21,417 articles
Total Articles: 44,898+
