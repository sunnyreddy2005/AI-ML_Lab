import numpy as np

class NaiveBayesClassifier:
    def __init__(self):
        self.prior = {}
        self.likelihoods = {}
        self.classes = []
        self.feature_probs = {}

    def fit(self, X, y):
        # X is the feature matrix (list of lists), y is the target list (class labels)
        self.classes = np.unique(y)
        n_samples, n_features = np.shape(X)
        
        for cls in self.classes:
            # Prior probability P(C)
            self.prior[cls] = np.sum(y == cls) / float(n_samples)
            
            # Create an empty dictionary for storing likelihoods
            self.likelihoods[cls] = {}
            
            for i in range(n_features):
                # Likelihood P(X|C) for each feature
                feature_vals = np.unique(X[:, i])
                self.likelihoods[cls][i] = {}
                
                for val in feature_vals:
                    self.likelihoods[cls][i][val] = np.sum((X[:, i] == val) & (y == cls)) / float(np.sum(y == cls))
    
    def predict(self, X):
        y_pred = []
        
        for sample in X:
            # Calculate the posterior for each class
            posteriors = {}
            
            for cls in self.classes:
                # Initialize with the prior P(C)
                posteriors[cls] = self.prior[cls]
                
                for i in range(len(sample)):
                    # Multiply by the likelihood P(X|C)
                    if sample[i] in self.likelihoods[cls][i]:
                        posteriors[cls] *= self.likelihoods[cls][i][sample[i]]
                    else:
                        posteriors[cls] *= 0  # If feature value not found in training, assume probability is 0
                
            # Choose the class with the highest posterior probability
            best_class = max(posteriors, key=posteriors.get)
            y_pred.append(best_class)
        
        return y_pred

# Training data (features and labels)
X_train = np.array([
    ['Yes', 'Yes'],  # Parrot
    ['Yes', 'Yes'],  # Eagle
    ['No', 'Yes'],   # Ostrich
    ['No', 'No'],    # Cat
    ['No', 'No'],    # Dog
    ['Yes', 'No']    # Bat
])

y_train = np.array(['Bird', 'Bird', 'Bird', 'Mammal', 'Mammal', 'Mammal'])

# Create the Naive Bayes classifier and train it
nb = NaiveBayesClassifier()
nb.fit(X_train, y_train)

# Predict the class for a new animal that cannot fly but lays eggs
X_test = np.array([['No', 'Yes']])
y_pred = nb.predict(X_test)

print("Predicted class:", y_pred)
