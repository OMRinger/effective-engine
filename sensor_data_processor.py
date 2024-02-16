# Sample Python Script for IoT Sensor Data Processing

import json
import requests

def fetch_sensor_data(sensor_endpoint):
    # Example function to fetch data from a sensor
    response = requests.get(sensor_endpoint)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return None

def process_sensor_data(data):
    # Example function to process sensor data
    processed_data = {
        'air_quality': data['AQI'],
        'water_quality': data['WQI'],
        # Add more processing logic as needed
    }
    return processed_data

# Example usage
if __name__ == "__main__":
    sensor_data = fetch_sensor_data('http://example-sensor-api.com/data')
    if sensor_data:
        print("Fetched Sensor Data:", sensor_data)
        processed_data = process_sensor_data(sensor_data)
        print("Processed Sensor Data:", processed_data)
    else:
        print("Failed to fetch sensor data.")