import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------
# Linear Regression
# -----------------------------
linear_model = LinearRegression()
linear_model.fit(X_train_scaled, y_train)
y_pred_lr = linear_model.predict(X_test_scaled)

# -----------------------------
# Polynomial Regression
# -----------------------------
poly = PolynomialFeatures(degree=2)
X_poly_train = poly.fit_transform(X_train_scaled)
X_poly_test = poly.transform(X_test_scaled)

poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)
y_pred_poly = poly_model.predict(X_poly_test)

# -----------------------------
# Ridge Regression
# -----------------------------
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train_scaled, y_train)
y_pred_ridge = ridge_model.predict(X_test_scaled)

# -----------------------------
# Lasso Regression
# -----------------------------
lasso_model = Lasso(alpha=0.1)
lasso_model.fit(X_train_scaled, y_train)
y_pred_lasso = lasso_model.predict(X_test_scaled)


# -----------------------------
# Evaluation Function
# -----------------------------
def evaluate(name, y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    print(f"{name}")
    print("RMSE:", rmse)
    print("R2 Score:", r2)
    print()
    return rmse


rmse_lr = evaluate("Linear Regression", y_test, y_pred_lr)
rmse_poly = evaluate("Polynomial Regression", y_test, y_pred_poly)
rmse_ridge = evaluate("Ridge Regression", y_test, y_pred_ridge)
rmse_lasso = evaluate("Lasso Regression", y_test, y_pred_lasso)


# -----------------------------
# 📊 Function to plot graph
# -----------------------------
def plot_graph(y_true, y_pred, title):
    plt.figure()
    plt.scatter(y_true, y_pred)
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title(title)

    # Perfect prediction line
    plt.plot([min(y_true), max(y_true)], [min(y_true), max(y_true)])
    plt.show()


# -----------------------------
# 📊 Individual Graphs
# -----------------------------
plot_graph(y_test, y_pred_lr, "Linear Regression")
plot_graph(y_test, y_pred_poly, "Polynomial Regression")
plot_graph(y_test, y_pred_ridge, "Ridge Regression")
plot_graph(y_test, y_pred_lasso, "Lasso Regression")

# -----------------------------
# 📊 RMSE Comparison Graph
# -----------------------------
models = ["Linear", "Polynomial", "Ridge", "Lasso"]
rmse_values = [rmse_lr, rmse_poly, rmse_ridge, rmse_lasso]

plt.figure()
plt.bar(models, rmse_values)
plt.xlabel("Models")
plt.ylabel("RMSE")
plt.title("Model Comparison")
plt.show()