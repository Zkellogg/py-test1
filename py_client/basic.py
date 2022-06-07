import pip._vendor.requests


# endpoint = "https://httpbin.org/status/200"

# endpoint = "https://httpbin.org/anything"

endpoint = "http://127.0.0.1:8000"

get_response = pip._vendor.requests.get(endpoint, json={"query": "Hello World"})
print(get_response.status_code)
























# import pip._vendor.requests 

# # endpoint = "https://www.httpbin.org/status/200"
# # endpoint = "https://www.httpbin.org/anything"
# endpoint = "http://127.0.0.1:8000/api/"



# get_response = pip._vendor.requests.get(endpoint) 

# print(get_response.json())
