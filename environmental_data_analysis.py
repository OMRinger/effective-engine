
import random
import datetime

# Simulate environmental data collection
def collect_environmental_data():
    """Simulate collecting environmental data from sensors."""
    data = {
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'air_quality': random.randint(0, 500),
        'water_quality': round(random.uniform(6.5, 9.0), 2),
        'temperature': round(random.uniform(15, 35), 1),
        'humidity': random.randint(30, 90)
    }
    return data

def analyze_data(data):
    """Basic analysis of collected environmental data."""
    print(f"Data collected at {data['timestamp']}")
    print(f"Air Quality Index: {data['air_quality']} (0-500)")
    print(f"Water Quality pH Level: {data['water_quality']} (6.5-9.0 is safe)")
    print(f"Temperature: {data['temperature']}°C")
    print(f"Humidity: {data['humidity']}%")

if __name__ == "__main__":
    data = collect_environmental_data()
    analyze_data(data)
