import boto3
import json

# Create IoT data client
iot_data = boto3.client("iot-data", region_name="us-east-1")

# Define the message
message = {
    "status": "online",
    "device": "Test Message from Vijay"
}

# Convert message to JSON (without Base64 encoding)
payload = json.dumps(message)

# Publish the message to AWS IoT
response = iot_data.publish(
    topic="test/topic",
    qos=1,
    payload=payload  # Send as JSON directly
)

print(f"Message published: {message}")
print(f"Response: {response}")
