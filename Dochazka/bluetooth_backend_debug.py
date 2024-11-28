# app.py (Flask Backend)

from flask import Flask, request

# Initialize the Flask app
app = Flask(__name__)

# Define a route to handle POST requests at /bluetooth
@app.route('/bluetooth', methods=['POST'])
def bluetooth_data():
    # Extract the JSON data sent in the POST request
    data = request.json
    if data:
        print("Received Bluetooth data:", data)  # Print the received data (for debugging)
        # Do something with the data (e.g., store it, process it)
        return 'Data received successfully', 201  # Respond with HTTP Status 201 (Created)
    else:
        return 'Invalid JSON data', 400  # Respond with HTTP Status 400 if no data or invalid JSON

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

