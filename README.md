# 📰 Fake News Detection System Using Machine Learning

A Machine Learning-powered web application that classifies news articles as **FAKE** or **NOT FAKE** using Natural Language Processing (NLP). The system preprocesses raw news text, converts it into numerical features using **TF-IDF Vectorization**, and predicts its authenticity using a trained **Logistic Regression** model through an interactive **Streamlit** interface.

---

##  Features

-  Classify news articles as **Fake** or **Not Fake** in real time.
-  Fast prediction using a pre-trained Machine Learning model.
-  Automatic text preprocessing (removes URLs, punctuation, HTML tags, numbers, and special characters).
-  TF-IDF based feature extraction for efficient text representation.
-  Interactive and user-friendly Streamlit web interface.
-  Pre-trained model and vectorizer loaded using Pickle for instant predictions.
-  High classification accuracy on benchmark fake news datasets.

---

##  Tech Stack

- **Programming Language:** Python
- **Machine Learning:** Scikit-Learn
- **Natural Language Processing:** TF-IDF Vectorization
- **Data Processing:** Pandas, NumPy
- **Frontend:** Streamlit
- **Model Serialization:** Pickle
- **Development Environment:** Visual Studio Code

---

##  Project Structure

```text
Fake-News-Detection-ML/
│
├── Dataset/
│   ├── Fake.csv
│   └── True.csv
│
├── app.py                     # Streamlit web application
├── fake_news_detection.ipynb  # Model training notebook
├── fake_news_model.pkl        # Trained Logistic Regression model
├── tfidf_vectorizer.pkl       # Trained TF-IDF Vectorizer
├── requirements.txt           # Required Python packages
├── README.md                  # Project documentation
└── .gitignore                 # Git ignored files
```

---

##  Dataset

The model is trained on the **Fake and Real News Dataset** available on Kaggle.

### Dataset Statistics

- **Fake News Articles:** 23,481
- **Real News Articles:** 21,417
- **Total Articles:** 44,898+

The dataset primarily consists of political and world news articles, enabling the model to learn linguistic patterns associated with fake and genuine news.

---

##  Machine Learning Pipeline

```text
Raw News Article
        │
        ▼
Text Preprocessing
        │
        ▼
TF-IDF Vectorization
        │
        ▼
Logistic Regression Model
        │
        ▼
Prediction
        │
        ▼
FAKE NEWS / NOT FAKE NEWS
```

---

##  How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Neerajkr-jha/Fake-News-Detection-ML.git

cd Fake-News-Detection-ML
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the Streamlit Application

```bash
streamlit run app.py
```

### 4. Open the Application

If the browser does not open automatically, visit:

```text
http://localhost:8501
```

---

##  Screenshots

### Home Screen

<img width="1918" height="1025" alt="image" src="https://github.com/user-attachments/assets/decb67a7-e047-42a9-aeac-2a62a050da43" />



### Prediction Result

# Fake News

<img width="1918" height="1020" alt="image" src="https://github.com/user-attachments/assets/1db18f59-2e55-4556-ac1e-f73171687015" />


# Real news 

<img width="1918" height="1026" alt="image" src="https://github.com/user-attachments/assets/dfbcbb9e-e354-4412-922a-ec8358e74d26" />



---

##  Model Information

| Attribute | Value |
|-----------|-------|
| Model | Logistic Regression |
| Feature Extraction | TF-IDF Vectorizer |
| Problem Type | Binary Text Classification |
| Class 0 | Fake News |
| Class 1 | Not Fake News |

---

##  Limitations

- The model predicts news authenticity based on learned linguistic patterns from historical datasets.
- It does **not** perform live fact-checking or verify current events.
- Performance may decrease on articles covering recent events or topics significantly different from the training data.
- Predictions should be considered as Machine Learning-based assessments rather than definitive verification.

---

##  Future Improvements

- Integrate Transformer-based models such as **BERT**, **RoBERTa**, or **DistilBERT**.
- Add URL-based news verification.
- Implement Explainable AI (XAI) by highlighting influential words.
- Integrate real-time fact-checking APIs.
- Continuously retrain the model using updated datasets.

---
