import requests
import json

url = "https://vh4xhmjk3lw2ibz5k6sa4i6fym0ltkqv.lambda-url.us-east-1.on.aws/"

payload = {
            "submitterEmail": ' ', # Your Email Id as it appears in the coursera instruction page.
            "secret": ' ', # Your token as it appears in the coursera instruction page. This token will only be valid for 30 mins.
            "ipaddress": '<IPv4>:<Port>' # Public IPv4 address which you can find on the EC2 instance home page. Add port number on which your server is running (5000).
    }


print("Running the autograder. This might take several seconds...")

r = requests.post(url, data=json.dumps(payload), headers = {"Content-Type": "application/json"})

print(r.status_code, r.reason)
print(r.text)
