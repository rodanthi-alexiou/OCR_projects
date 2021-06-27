from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "75cf08bf13504aceba120c8f923d3d71"
endpoint = "https://summary.cognitiveservices.azure.com/"

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def entity_recognition_example(client):

    try:
        documents = ["wearing a Tommy James shirt. She"]
        result = client.recognize_entities(documents = documents)[0]

        print("Named Entities:\n")
        for entity in result.entities:
            print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory, "\n")

    except Exception as err:
        print("Encountered exception. {}".format(err))

entity_recognition_example(client)