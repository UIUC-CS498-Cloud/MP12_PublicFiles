# ============================================================================
# DO NOT MODIFY THIS FILE.
# This file is part of the MP: Two-Tier Microservice Architecture for ML Inference for CS 498CCA at UIUC.
# It serves as the interface between the Autograder and your Kubernetes deployment.
# ============================================================================
# Before submission, ensure that:
# Run this `grader_interface.py` file on your EC2 instance (used to set up your Kubernetes deployment) to start the Interface flask server on port 5000.

from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def get_latest_completed_pod(namespace, prefix):
    try:
        pods_output = subprocess.check_output([
            'kubectl', 'get', 'pods', '-n', namespace,
            '--field-selector=status.phase=Succeeded',
            '--sort-by=.metadata.creationTimestamp',
            '-o', 'jsonpath={.items[*].metadata.name}'
        ], stderr=subprocess.STDOUT).decode('utf-8')

        pod_names = [name for name in pods_output.split() if name.startswith(prefix)]

        if not pod_names:
            print(f"[DEBUG] No completed pods found with prefix '{prefix}'")
            return None

        return pod_names[-1]

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Kubectl error: {e.output.decode('utf-8')}")
        return None


def get_pod_logs(namespace, pod_name):
    try:
        container_name = subprocess.check_output([
            'kubectl', 'get', 'pod', pod_name, '-n', namespace,
            '-o', 'jsonpath={.spec.containers[0].name}'
        ], stderr=subprocess.STDOUT).decode('utf-8')
        print(f"[LOGS] Fetching logs from pod: {pod_name}, container: {container_name}")
        logs = subprocess.check_output([
            'kubectl', 'logs', pod_name, '-c', container_name, '-n', namespace
        ], stderr=subprocess.STDOUT).decode('utf-8')
        return logs

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error fetching logs: {e.output.decode('utf-8')}")
        return None

@app.route('/free/logs', methods=['GET'])
def get_free_logs():
    namespace = 'free-service'
    pod_name = get_latest_completed_pod(namespace, 'free-job-template')

    if not pod_name:
        return jsonify({"error": "No completed pods found for free-service."}), 404

    logs = get_pod_logs(namespace, pod_name)
    if logs is None:
        return jsonify({"error": "Failed to retrieve logs for free-service pod."}), 500

    return logs, 200

@app.route('/premium/logs', methods=['GET'])
def get_premium_logs():
    namespace = 'premium-service'
    pod_name = get_latest_completed_pod(namespace, 'premium-job-template')

    if not pod_name:
        return jsonify({"error": "No completed pods found for premium-service."}), 404

    logs = get_pod_logs(namespace, pod_name)
    if logs is None:
        return jsonify({"error": "Failed to retrieve logs for premium-service pod."}), 500

    return logs, 200

@app.route('/free/resource-quota', methods=['GET'])
def resource_quota():
    try:
        output = subprocess.check_output(
            ['kubectl', 'describe', 'quota', '-n', 'free-service'],
            stderr=subprocess.STDOUT
        )
        return output.decode('utf-8'), 200
    except subprocess.CalledProcessError as e:
        return f"Error fetching resource quota: {e.output.decode('utf-8')}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
