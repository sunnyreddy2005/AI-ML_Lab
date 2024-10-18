import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Sample data (Hours studied vs. Pass/Fail)
X = np.array([[1], [2], [3], [4], [5], [6]])  # Hours studied
y = np.array([0, 0, 0, 1, 1, 1])              # 0 = Fail, 1 = Pass

# Create a Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X, y)

# Make predictions (probabilities)
y_prob = model.predict_proba(X)[:, 1]  # Probability of passing (1)

# Plot the results
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, y_prob, color='red', label='Logistic curve')
plt.xlabel('Hours studied')
plt.ylabel('Probability of passing')
plt.title('Logistic Regression')
plt.legend()
plt.show()

# Predict for a new value (e.g., 4.5 hours of study)
new_hours = np.array([[4.5]])
predicted_prob = model.predict_proba(new_hours)[0][1]
predicted_class = model.predict(new_hours)[0]
print(f"Predicted probability of passing for 4.5 hours of study: {predicted_prob:.2f}")
print(f"Predicted class (0 = Fail, 1 = Pass): {predicted_class}")
