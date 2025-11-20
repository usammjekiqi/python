import requests


uri= "https://www.wikipedia.org/"

try:
    requests = requests.get(uri)
    requests.raise_for_status()  
    print(requests.text)
except requests.exceptions.RequestException as e:
    print(f"http error occurred: {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Connection error occurred: {e}")