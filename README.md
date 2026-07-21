# 📧 Email/SMS Spam Classifier

A Machine Learning web application that classifies Email and SMS messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) and a TF-IDF + Multinomial Naive Bayes model. The application is built with **Python** and **Streamlit** and provides instant predictions through a simple web interface.

## 🚀 Live Demo

🔗 https://spam-classifier-by-aayush-naithani.streamlit.app

---

## 📌 Features

- Detects Spam and Ham messages instantly
- Text preprocessing using NLP techniques
- TF-IDF Vectorization
- Machine Learning classification using Multinomial Naive Bayes
- Interactive Streamlit web interface
- Fast and lightweight deployment

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Pickle

---

## 📂 Project Structure

```
EmailSMS-Spam-Classifier/
│
├── Dataset/
│   └── spam.csv
│
├── Model/
│   ├── model.pkl
│   └── Vectorizer.pkl
│
├── app.py
├── sms_classifier.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 Machine Learning Pipeline

1. Data Cleaning
2. Text Preprocessing
   - Lowercase Conversion
   - Tokenization
   - Stopword Removal
   - Punctuation Removal
   - Stemming
3. TF-IDF Vectorization
4. Model Training using Multinomial Naive Bayes
5. Model Evaluation
6. Streamlit Deployment

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Aayush-Naithani/Spam-Classifier.git
```

Move into the project directory

```bash
cd Spam-Classifier
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📊 Model Performance

- Text Vectorization: TF-IDF
- Algorithm: Multinomial Naive Bayes
- NLP Preprocessing:
  - Lowercasing
  - Tokenization
  - Stopword Removal
  - Stemming

---

## 💡 Example

### Input

```
Congratulations! You have won a FREE iPhone. Click the link below to claim your prize.
```

### Prediction

```
Spam Message
```

---

## 📸 Application Preview

<img width="1323" height="676" alt="image" src="https://github.com/user-attachments/assets/69ca5e17-3a96-4554-8bec-a64f23f3278f" />

---

## 📚 Future Improvements

- Deep Learning (LSTM/BERT)
- Email Attachment Analysis
- URL Detection
- Confidence Score
- Multi-language Spam Detection

---

## 👨‍💻 Author

**Aayush Naithani**

- GitHub: https://github.com/Aayush-Naithani

---

⭐ If you found this project helpful, don't forget to star the repository!
