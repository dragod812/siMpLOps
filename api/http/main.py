from http.client import BAD_REQUEST
from fastapi import APIRouter
from api.component.predict import predict
from api.http.digit import Digit
from api.http.digit_image import DigitImage

api = APIRouter()


@api.post("/predict", response_model=Digit)
def post_predict(
    digit_image: DigitImage,
):
    predict_response = predict(digit_image.to_numpy())
    if len(predict_response) == 0:
        raise BAD_REQUEST
    return Digit(digit=int(predict_response[0]))
