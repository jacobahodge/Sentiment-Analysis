# 1.) Clone the project repository
git clone https://github.com/ibm-developer-skills-network/zzrjt-practice-project-emb-ai.git practice_project # run this in the terminal.
cd practice_project # This is assuming you made a folder named practice_project already. 

# 2.) Create a sentiment analysis application using Watson NLP library
import requests

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header)
    return response.text
--
python3.11 # Run in the terminal
--
from sentiment_analysis import sentiment_analyzer # run this in the terminal 
--
sentiment_analyzer("I love this new technology") # run from the terminal to make sure it is working.

# 3.) Format the output of the application
import requests # Run in the terminal
import json # Run in the terminal
--
response = sentiment_analyzer("I love this new technology") # Run in the terminal
--
formatted_response = json.loads(response) # Run in the terminal
print(formatted_response) # Run in the terminal
--
label = formatted_response['documentSentiment']['label']  # Run in the terminal
# test this by running "label" in the terminal 
score = formatted_response['documentSentiment']['score']  # Run in the terminal
# test this by running "score" in the terminal  
---
# Now update the python file...
import requests
import json # This is an addition

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text) # This is new
    label = formatted_response['documentSentiment']['label'] # This is new
    score = formatted_response['documentSentiment']['score'] # This is new
    return {'label': label, 'score': score} # This is updated
--
# Test the updated function in the terminal 
sentiment_analyzer("I love this new technology")

# 4.) Package the application
# 5.) Run Unit tests on your application
# 6.) Deploy as web application using Flask
# 7.) Incorporate Error handling
# 8.) Run static code analysis
