import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# =========================================
# LOAD DATASET
# =========================================

data = pd.read_csv("emails.csv")

# =========================================
# FEATURES AND LABELS
# =========================================

X = data["text"]
y = data["label"]

# =========================================
# TEXT VECTORIZATION
# =========================================

vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# =========================================
# TRAIN TEST SPLIT
# =========================================

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)
# =========================================
# MODEL TRAINING
# =========================================

model = LogisticRegression()

model.fit(X_train, y_train)

# =========================================
# PREDICTIONS
# =========================================

predictions = model.predict(X_test)

# =========================================
# EVALUATION
# =========================================

accuracy = accuracy_score(y_test, predictions)

print("=" * 45)
print("   PHISHING EMAIL DETECTION MODEL")
print("=" * 45)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# =========================================
# TEST CUSTOM EMAIL
# =========================================

email = input("\nEnter Email Content:\n")

email_vector = vectorizer.transform([email])

result = model.predict(email_vector)

print("\nClassification Result:")

if result[0] == "phishing":
    print("Email is classified as: Phishing")
else:
    print("Email is classified as: Safe")