import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy


def inference_model():
	model= Sequential([
	    Dense(units=32, input_shape=(8,), activation='relu'),
	    Dropout(0.2),
	    Dense(units=64, activation='relu'),
	    Dropout(0.2),
	    Dense(units=128, activation='relu'),
	    Dropout(0.2),
	    Dense(units=2, activation='softmax')
	])
	return model
	
tf.config.experimental.set_memory_growth(tf.config.experimental.list_physical_devices('GPU')[0], True)

st.title("Wildfire Detection App")

st.write("I like trains")


check=st.button("Predict")

if check:
	infer_model=inference_model()
	infer_model.load_weights("../weights/prototype.h5")
	output=infer_model.predict(x= )
	final_class=np.argmax(output, axis=1)[0]
	st.write("Prediction: ",getmap(final_class))
