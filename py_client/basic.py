import pip._vendor.requests 

# endpoint = "https://www.httpbin.org/status/200"
# endpoint = "https://www.httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"



get_response = pip._vendor.requests.get(endpoint) 

print(get_response.json())
