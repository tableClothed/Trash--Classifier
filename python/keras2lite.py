import tensorflow.lite as lite
from tensorflow.keras.models import load_model
import tensorflow as tf

def convert():
	keras_model = load_model("models/garbage.h5")
	tflite_name = "models/garbage_lite.tflite"

	converter = lite.TFLiteConverter.from_keras_model(keras_model)
	converter.post_training_quantize = True
	tflite_model = converter.convert()

	with tf.io.gfile.GFile(tflite_name, "wb") as f:
		f.write(tflite_model)

if __name__ == "__main__":
	convert()