import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data (Hours studied vs. Exam score)
X = np.array([[1], [2], [3], [4], [5]])  # Hours studied
y = np.array([50, 60, 70, 80, 90])       # Exam score

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Plot the results
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, y_pred, color='red', label='Regression line')
plt.xlabel('Hours studied')
plt.ylabel('Exam score')
plt.title('Linear Regression')
plt.legend()
plt.show()

# Predict for a new value (e.g., 6 hours of study)
new_hours = np.array([[6]])
predicted_score = model.predict(new_hours)
print(f"Predicted exam score for 6 hours of study: {predicted_score[0]:.2f}")
