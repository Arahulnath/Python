# Import libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Load dataset (digits dataset similar to MNIST)
digits = datasets.load_digits()

X = digits.data      # features (pixel values)
y = digits.target    # labels (0–9)

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------
# SVM Classifier
# -------------------------
svm_model = SVC(kernel='rbf')

svm_model.fit(X_train, y_train)

svm_pred = svm_model.predict(X_test)

print("SVM Accuracy:", accuracy_score(y_test, svm_pred))
print("SVM Classification Report:\n", classification_report(y_test, svm_pred))

# -------------------------
# KNN Classifier
# -------------------------
knn_model = KNeighborsClassifier(n_neighbors=5)

knn_model.fit(X_train, y_train)

knn_pred = knn_model.predict(X_test)

print("KNN Accuracy:", accuracy_score(y_test, knn_pred))
print("KNN Classification Report:\n", classification_report(y_test, knn_pred))


# -------------------------
# Display some predictions
# -------------------------
plt.figure(figsize=(10,4))

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(X_test[i].reshape(8,8), cmap='gray')
    plt.title("Pred: " + str(knn_pred[i]))
    plt.axis('off')

plt.show()