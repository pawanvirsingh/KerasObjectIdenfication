from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
import numpy as np
from keras.preprocessing.image import load_img

def load_model():
    """Loading model"""
    model = VGG16()
    return model

def load_image(image):
	"""Loading image"""
	im = load_img(image, target_size=(224, 224))
	return im
def extend_size(image):
	image = np.expand_dims(image, axis=0)
	return image

model = load_model()
test_img = "car.jpg"
"""
target_x = 244
target_y = 244
resize_pixels = [target_x, target_y]
"""
def findtheobject(test_img = "bik.jpeg"):
	model = load_model()

	image = load_image(test_img)
	image = img_to_array(image)
	image = preprocess_input(image)
	#image = load_image(test_img, )
	image = extend_size(image)
	y_pred = model.predict(image)
	label = decode_predictions(y_pred)
	print (label)
	return label

# a= findtheobject(test_img = "pus.jpg")