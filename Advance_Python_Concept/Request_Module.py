import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

# A GET request to the API
response = requests.get(url)
# print(response.text)

# Print the response
response_json = response.json()
print(type(response_json))



"""
    first Run Command In Terminal : pip install requests
"""