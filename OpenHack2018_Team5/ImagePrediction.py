import os
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
 
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"
 
# Replace with a valid key
training_key = "8202cc602079498c8c0b5d002d422bc0"
prediction_key = "1bc26fdf4b984a54afae6d05074aeda4"
 
# Now there is a trained endpoint that can be used to make a prediction
 
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)
 
#test_img_url = "http://i1.adis.ws/i/jpl/bl_208555_a"
test_img_url1 = "https://www.popsci.com/sites/popsci.com/files/styles/655_1x_/public/images/2018/01/84711_fea.jpg?itok=nxNwehk-&fc=50,50"
test_img_url2 = "https://images-na.ssl-images-amazon.com/images/I/61%2BUrQmHDsL._UX679_.jpg"

project_id = "8bc27737-5835-4ba9-95f9-06984cd7d4e3"
iteration_id = "c4846c08-c001-47ae-bb5d-7c595dea16ad"

results = predictor.predict_image_url(project_id, iteration_id, url=test_img_url1)
 
# Display the results.
for prediction in results.predictions:
    print ("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))

results = predictor.predict_image_url(project_id, iteration_id, url=test_img_url2)
 
# Display the results.
for prediction in results.predictions:
    print ("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))