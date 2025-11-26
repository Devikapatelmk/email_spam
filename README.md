📧 Email Spam Detection – Python + Flask + HTML
This project is a simple Email Spam Detection Web App built using:
Python (Flask)
Machine Learning (Naive Bayes)
HTML + JavaScript frontend
The model detects whether a message is Spam or Not Spam based on the text provided by the user.

🚀 Features
Simple and clean UI
Real-time spam detection
Flask backend API
Machine Learning model (Naive Bayes)
Easy to run in PyCharm or any Python environment
Includes training script to generate the model

📂 Project Structure
email-spam/
│── app.py
│── train_model.py
│── requirements.txt
│── README.md
│── models/
│     ├── spam_model.pkl
│     └── vectorizer.pkl
└── static/
      └── index.html

🧠 Machine Learning Model
The model uses:
CountVectorizer to convert text → numbers
Multinomial Naive Bayes classifier
The model is trained on a small sample dataset (can be expanded anytime).

🧪 Sample Spam Messages
Use these to test:
"Congratulations! You won a free prize!"
"Claim your ₹10,000 reward now"
"Click here to get free recharge"
"Your bank account is blocked, verify now"

🔧 Customization
You can:
Add a better dataset in train_model.py
Improve UI inside static/index.html
Deploy to Render/Heroku/AWS
