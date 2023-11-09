import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from text_analysis_lib import get_labels
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import numpy as np

x_mat = pd.read_csv('why_response_vectors.csv')
pca = PCA(n_components=3)
pca_result = pca.fit_transform(x_mat)

x_mat2 = pd.DataFrame(data=pca_result, columns=['pca1', 'pca2', 'pca3'])
response_df = pd.read_csv('data.csv')

program_responses = response_df['What program are you in?'].tolist()
compsci_labels = get_labels()


# compsci_df = x_mat2[compsci_labels]
# not_compsci_df = x_mat2[[not i for i in compsci_labels]]

X_train, X_test, y_train, y_test = train_test_split(x_mat, compsci_labels, test_size=0.3, random_state=42)
y_train = np.array(y_train)
y_test = np.array(y_test)

# Define the model
model = Sequential([
    # Add a densely-connected layer with 64 units to the model:
    Dense(64, activation='sigmoid', input_shape=(769,)),
    # Add another:
    Dense(64, activation='sigmoid'),
    # Add a softmax layer with 1 output units:
    Dense(1, activation='sigmoid'),
])

# Compile the model
model.compile(
    # Optimizer
    optimizer='adam',  
    # Loss function to minimize
    loss='binary_crossentropy',
    # List of metrics to monitor
    metrics=['accuracy'],
)

# Train the model
model.fit(
    X_train, 
    y_train, 
    epochs=100, 
    batch_size=32,
    validation_data=(X_test, y_test)
)

# Evaluate the model
model.evaluate(X_test, y_test, batch_size=32)

# Make predictions
predictions = model.predict(X_train[:5])
