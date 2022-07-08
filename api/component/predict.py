

import numpy as np
import onnxruntime as rt

sess = rt.InferenceSession("mnist_knneighbours_classifier.onnx")
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name


def predict(digit_image: np.ndarray):
    prediction = sess.run(
        [label_name], {input_name: [digit_image]})[0]
    return prediction
