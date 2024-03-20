from flask import Flask, jsonify, render_template
import boto3

app = Flask(__name__)
client = boto3.client('ec2')



def fetch_instance_status():
    response = client.describe_instance_status(IncludeAllInstances=True)
    instance_statuses = []
    for instance in response['InstanceStatuses']:
        instance_id = instance['InstanceId']
        instance_status = instance['InstanceStatus']['Status']
        system_status = instance['SystemStatus']['Status']
        instance_state = instance['InstanceState']['Name']
        instance_statuses.append({
            'instance_id': instance_id,
            'instance_state': instance_state,
            'instance_status': instance_status,
            'system_status': system_status
        })
    return instance_statuses

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/instance_status')
def instance_status():
    instance_statuses = fetch_instance_status()
    return jsonify(instance_statuses)


if __name__ == '__main__':
    app.run(debug=True)
