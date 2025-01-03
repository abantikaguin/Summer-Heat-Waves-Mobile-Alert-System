from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

def train_model(data):
    """Train the heatwave prediction model."""
    X = data[['Temperature', 'Humidity', 'Heat_Index']]
    y = data['Heatwave_Occurred']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    # Save the model
    with open('heatwave_model.pkl', 'wb') as file:
        pickle.dump(model, file)

    return model