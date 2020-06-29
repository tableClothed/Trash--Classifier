from tensorflow.keras.models import load_model
import tensorflowjs as tfjs
import tensorflow as tf

def convert():
	m = load_model("models/g_model.h5")
	tfjs.converters.save_keras_model(m, "model_js")

if __name__ == "__main__":
	convert()