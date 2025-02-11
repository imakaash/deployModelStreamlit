import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a model
model = RandomForestClassifier()
model.fit(X, y)

# Save the trained model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file, protocol=pickle.HIGHEST_PROTOCOL)