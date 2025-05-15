import requests
import json

url = "https://5t72crzbtelmzcnqp36yt5i2cm0tygzs.lambda-url.us-east-1.on.aws/"

payload = {
    "submitterEmail": '<YOUR_EMAIL@illinois.edu>',  # Your Coursera-registered email
    "secret": '<YOUR_COURSERA_SECRET_TOKEN>',       # Your Coursera assignment token (valid for 30 mins)
    "lbaddress": 'http://<LB_DNS>.us-east-1.elb.amazonaws.com',                 # LB External IP 
    "ipaddress": 'http://<EC2_IP>:5000',            # EC2 public IPv4 and port (running grader_interface.py) 

}

print("\n========== MP Two-Tier Microservice Architecture Submission ==========")
print("Submitting your deployment details to the Coursera autograder...")
print("This process may take up to a minute. Please wait for your results.\n")

response = requests.post(
    url,
    data=json.dumps(payload),
    headers={"Content-Type": "application/json"}
)

print(response.status_code, response.reason)
print(response.text)