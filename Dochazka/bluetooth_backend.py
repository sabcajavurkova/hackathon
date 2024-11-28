import bluetooth

def scan_bluetooth_devices():
    print("Scanning for Bluetooth devices...")
    
    # Adjusted to remove unsupported argument 'lookup_oui'
    while True:
        nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
        if nearby_devices:
                print(f"Found {len(nearby_devices)} device(s):")
                for addr, name in nearby_devices:
                    print(f"Device Address: {addr}, Device Name: {name}")
        else:
            print("No devices found.")

if __name__ == "__main__":
    scan_bluetooth_devices()
