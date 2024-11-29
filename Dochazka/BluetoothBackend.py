import bluetooth
import requests
import time

# URL of the Flask backend
API_URL = "http://127.0.0.1:5000/bluetooth"  # Backend URL on localhost

def scan_bluetooth_devices():
    print("Starting Bluetooth scan...")

    while True:  # Infinite loop to keep scanning for Bluetooth devices
        nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)

        if nearby_devices:
            print(f"Found {len(nearby_devices)} device(s):")
            for addr, name in nearby_devices:
                print(f"Device Address: {addr}, Device Name: {name}")

                # Prepare the data to send to the Flask backend
                data = {"address": addr}

                # Send data to the backend using POST
                try:
                    response = requests.post(API_URL, json=data)

                    # Check if the request was successful
                    if response.status_code == 201:
                        print("Device data sent successfully!")
                    else:
                        print(f"Failed to send data: {response.status_code}")
                except Exception as e:
                    print(f"Error sending data: {e}")

        else:
            print("No devices found.")

# Run the Bluetooth scanning function
if __name__ == "__main__":
    scan_bluetooth_devices()
