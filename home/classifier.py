import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
def load_dataset():
    data = pd.read_csv('static/data/ice_cream_quiz_dataset.csv')
    X = data[['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']]  # Features
    y = data['Flavor']  # Target
    return X, y

# Train the classifier with a train-test split
def train_classifier():
    X, y = load_dataset()
    
    # Split dataset into 80% training and 20% testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the classifier
    classifier = DecisionTreeClassifier()
    
    # Train the classifier on the training data
    classifier.fit(X_train, y_train)
    
    # Test the classifier on the testing data (for validation)
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Validation Accuracy: {accuracy * 100:.2f}%")
    
    return classifier

# Predict the flavor based on user's answers
def predict_flavor(answers):
    classifier = train_classifier()  # Ensure classifier is trained
    return classifier.predict([answers])[0]  # Return the predicted flavor
