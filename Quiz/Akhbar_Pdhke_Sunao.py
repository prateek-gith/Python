import requests
import json
from win32com.client import Dispatch

# function for speaking
def speak(str):
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)

# fetch Api For Speaking
my_api="https://newsapi.org/v2/everything?q=tesla&from=2024-06-24&sortBy=publishedAt&apiKey=dc7aaae6bf95493bb8a03e1c607cff18"

# responce the API
response = requests.get(my_api)

#convert Into python Dict.
response_json = response.json()
print(type(response_json))

# we fetch only articles from dict. and store in the variable 
vart=response_json["articles"]

# loop for every artcle
for article in vart:
    # feth title from every article and send to speak function
    speak(article['title'])




# second Method

# convert dict file into json/str
# result_first = json.dumps(response_json)
# print(result_first)



# if __name__=='__main__':
#     speak(result_first)
import collections
b=collections.Counter([2,2,3,4,4,4])
b.most_common(1)