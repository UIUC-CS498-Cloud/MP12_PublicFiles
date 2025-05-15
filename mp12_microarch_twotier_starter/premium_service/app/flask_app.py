"""
Premium Tier Flask API service.

This module provides a minimal Flask application that exposes an endpoint to launch
Kubernetes jobs in the 'premium-service' namespace.

Students should extend this code to add additional endpoints, error handling,
or business logic as required by the assignment.
"""

from kubernetes import client, config
from flask import Flask, request

# Load Kubernetes configuration 
try:
    config.load_incluster_config() 
except config.config_exception.ConfigException:
    config.load_kube_config()  

# Initialize Flask app
v1 = client.CoreV1Api()
app = Flask(__name__)

# TODO: Define a POST endpoint that:
#   - Parses the incoming JSON for the 'dataset' parameter
#   - Loads the job YAML template
#   - Injects the dataset value into the job spec
#   - Generates a unique job name
#   - Submits the job to the Kubernetes cluster
#   - Returns a success or error response
@app.route('<your_path_here>', methods=['POST'])
def post_premium():
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)