import numpy as np
from keras.models import load_model

# Load the trained model
model = load_model('my_model.h5')

def predict_emotions(input_data):
    # Reshape the input data to have shape (1, 136)
    input_data = np.array(input_data).reshape(1, 136)
    
    # Make predictions
    y_pred = model.predict(input_data)
    
    # Get the predicted emotion
    emotions = ['anger', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
    predicted_emotion = emotions[np.argmax(y_pred)]
    
    # Print the predicted emotion
    print("Predicted emotion:", predicted_emotion)


# def generate_random_data(n_samples, n_features):
#     X = np.random.randn(n_samples, n_features)
#     return X.tolist()


# input_data = generate_random_data(1, 136)

#predict_emotions(input_data)


