import time
import json
import requests

# Mock function to simulate reading from a sensor
def read_sensor_data():
    # In a real application, this function would interface with your sensor.
    # Here we're simulating temperature and humidity readings.
    temperature = 25.0  # degrees Celsius
    humidity = 40.0     # percentage
    return temperature, humidity

def send_data_to_server(temperature, humidity):
    # Placeholder URL for sending data to a server or cloud platform
    server_url = "http://yourserver.com/api/sensor-data"
    headers = {"Content-Type": "application/json"}
    
    # Prepare the data payload as a JSON object
    data_payload = json.dumps({
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": time.time()
    })
    
    try:
        response = requests.post(server_url, headers=headers, data=data_payload)
        if response.status_code == 200:
            print("Data successfully sent to server.")
        else:
            print(f"Failed to send data. Server responded with status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while sending data: {e}")

def main():
    while True:
        temperature, humidity = read_sensor_data()
        print(f"Temperature: {temperature} C, Humidity: {humidity} %")
        
        # Send data to server or cloud for storage and analysis
        send_data_to_server(temperature, humidity)
        
        # Wait for a specified interval before reading again
        time.sleep(60)  # Wait for 1 minute (60 seconds)

if __name__ == "__main__":
    main()
pip install requests
{
  "sensor_id": "temp_sensor_01",
  "type": "temperature",
  "value": 22.5,
  "unit": "C",
  "timestamp": "2023-09-21T15:45:00Z"
}
import json
import time

def get_sensor_data():
    # Simulate reading data
    sensor_data = {
        "sensor_id": "temp_sensor_01",
        "type": "temperature",
        "value": 22.5,  # This would be replaced with a real sensor reading
        "unit": "C",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    return json.dumps(sensor_data)
