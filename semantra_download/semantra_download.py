from flask import Flask, render_template, request, jsonify  # Import necessary Flask modules
import requests  # Import requests module to make HTTP requests
import json  # Import json module for handling JSON data
import os  # Import os module for file operations

# Initialize Flask application with specified template and static folders
app = Flask(__name__, template_folder="templates", static_folder="static")

# Define a default port for the API communication
DEFAULT_PORT = 8080  # Default Semantra port

@app.route("/", methods=["GET", "POST"])  # Define the route for the home page and allow GET and POST requests
def index():
    if request.method == "POST":  # Check if the request is a POST request
        query_text = request.form.get("query")  # Retrieve the user's query from the form
        save_location = request.form.get("save_location")  # Retrieve the save location from the form
        port_number = request.form.get("port") or str(DEFAULT_PORT)  # Use user-provided port or default to 8080

        # Validate input: Ensure query is provided
        if not query_text:
            return jsonify({"status": "error", "message": "Query cannot be empty!"})
        
        # Validate input: Ensure save location is provided
        if not save_location:
            return jsonify({"status": "error", "message": "Save location is required!"})

        # Ensure the save directory exists; create it if it does not
        os.makedirs(save_location, exist_ok=True)

        # Prepare the query data payload for the API request
        query_data = {
            "queries": [{"query": query_text, "weight": 1.0}],  # List of queries with weights
            "preferences": []  # Empty preferences list (optional customization parameter)
        }

        # Construct the API URL with the specified port
        api_url = f"http://127.0.0.1:{port_number}/api/query"

        try:
            # Send a POST request to the API with the query data
            response = requests.post(api_url, json=query_data)

            # Check if the request was successful (HTTP status 200)
            if response.status_code == 200:
                results = response.json()  # Parse the JSON response
                output_path = os.path.join(save_location, "query_results.json")  # Define file path

                # Save the results to a JSON file
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(results, f, indent=4, ensure_ascii=False)  # Pretty-print the JSON data

                return jsonify({"status": "success", "message": f"✅ Results saved to: {output_path}"})
            else:
                # Handle API errors
                return jsonify({"status": "error", "message": f"❌ Error {response.status_code}: {response.text}"})

        except requests.exceptions.RequestException as e:
            # Handle request failures (e.g., connection errors)
            return jsonify({"status": "error", "message": f"❌ Request failed: {str(e)}"})

    # Render the index.html template for GET requests, passing the default port as a variable
    return render_template("index.html", default_port=DEFAULT_PORT)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for development (shows errors in the browser)
