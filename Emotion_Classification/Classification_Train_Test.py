import numpy as np
from keras.models import Sequential
from keras.layers import Dense
#from keras.models import load_model

# Define the input and output dimensions
input_dim = 136
output_dim = 7

# Define the model architecture
model = Sequential()
model.add(Dense(256, input_dim=input_dim, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(output_dim, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Generate some dummy data for training and validation
X_train = np.random.rand(1000, input_dim)
y_train = np.random.rand(1000, output_dim)
X_val = np.random.rand(100, input_dim)
y_val = np.random.rand(100, output_dim)

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))
# Save the model to a file
model.save('my_model.h5')

# Evaluate the model
score = model.evaluate(X_val, y_val, batch_size=32)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
