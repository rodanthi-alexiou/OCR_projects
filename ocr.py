import os
import sys
import time
import requests
import json



from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential



key_text_analytics = "75cf08bf13504aceba120c8f923d3d71"
endpoint_text_analytics = "https://summary.cognitiveservices.azure.com/"

def authenticate_client():
    ta_credential = AzureKeyCredential(key_text_analytics)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint_text_analytics, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

artists = []

def entity_recognition_example(client,text):

    try:
        documents = text
        result = client.recognize_entities(documents = documents)[0]

        for entity in result.entities:
            if(entity.category == "Person"):
                name = entity.text
                artists.append(name.lower())

    except Exception as err:
        print("Encountered exception. {}".format(err))
        






subscription_key = "ee04441c8db64d068bb75db82dd985fe"
endpoint = "https://gettext.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))




print("Reading text from book page")



images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "")
# Get image path
read_image_path = os.path.join (images_folder, "song4.jpg")
# Open the image
read_image = open(read_image_path, "rb")



# Call API with image and raw response (allows you to get the operation location)
read_response = computervision_client.read_in_stream(read_image, raw=True)



# Get the operation location (URL with an ID at the end) from the response
read_operation_location = read_response.headers["Operation-Location"]
# Grab the ID from the URL
operation_id = read_operation_location.split("/")[-1]

# Call the "GET" API and wait for it to retrieve the results 
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)





if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            names = []
            names.append(line.text)
            entity_recognition_example(client,names)
        




characters = ["daisy", "billy","simone","warren","chuck","camila","eddie","karen"]
print(artists)
temp = [x for x in artists if x not in characters]
print(temp)
wrong = []
wrong_name = input("Enter artists:")
wrong.append(wrong_name.lower())
new = [x for x in temp if x not in wrong]
print(new)




