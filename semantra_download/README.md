# README: Semantra Download Utility


https://github.com/user-attachments/assets/0deb6b20-7ce1-4470-86bd-317907f527d6


This utility provides a simple way to search your indexed documents (via Semantra) and save the semantic results to a local file.

## Prerequisites

### Semantra Installed & Running
- You must have Semantra installed.
- Run Semantra in a separate terminal session using its default command (e.g., `semantra doc.pdf`), or with your preferred options (e.g., a custom port using `--port 9000`).

### Python 3 Environment
- Confirm you have Python 3 installed (version ≥ 3.9 is recommended).
- Ensure you have Flask and requests installed:
  ```bash
  pip install flask requests
  ```

## How It Works

### Search in Semantra
1. Use Semantra’s native web interface to confirm your documents are indexed and to preview relevant text.
2. Semantra typically launches a local website at `http://127.0.0.1:8080` (or whatever port you specified).

### Start the Download Utility
1. In a separate terminal or command prompt, navigate to the folder containing `semantra_download.py`.
2. Run the script:
   ```bash
   python3 semantra_download.py
   ```
3. By default, this script will start a small Flask server at `http://127.0.0.1:5000`.

### Access the Download Interface
1. Open `http://127.0.0.1:5000` in your browser. You will see a simple form with the following fields:
   - **Search Query**: The text you want Semantra to search for.
   - **Save Location**: A valid folder path on your system where the JSON file should be saved (e.g., `/Users/yourname/Desktop`).
   - **Semantra Port**: The port where Semantra is running. Defaults to `8080` if you didn’t change Semantra’s default. Adjust this if you ran Semantra on a different port.

### Download Your Results
1. Enter your search text, the directory for saving results, and confirm Semantra’s port.
2. Click **Search & Save** (or "Download").
3. The utility will:
   - Send your query to Semantra’s `/api/query` endpoint.
   - Receive a JSON response of matching passages, their filenames, and similarity scores.
   - Write these search results to a file called `query_results.json` in the specified save directory.

### Check Your Download
- Once the query completes, the web page will display a success or error message.
- If successful, navigate to the **Save Location** folder you provided to find `query_results.json`.
- **Important**: If you plan to run a new search and keep your old results, consider renaming (or moving) your existing `query_results.json` before you do another download. Otherwise, the file will be overwritten with new data.

## Example Workflow

### Run Semantra (in one terminal):
```bash
semantra doc.pdf
# Semantra starts and serves at http://127.0.0.1:8080
```

### Run Download Utility (in a different terminal):
```bash
python3 semantra_download.py
```
You should see:
```text
Serving Flask app 'semantra_download'
* Debug mode: on
WARNING: This is a development server. ...
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### Open `http://127.0.0.1:5000` and fill in:
- **Search Query**: e.g., "regulation policy"
- **Save Location**: e.g., `/Users/yourname/Desktop`
- **Semantra Port**: `8080` (or another if you changed it)
- Click **Search & Save**.

### Locate Results
- Look for `query_results.json` in the folder you specified.
- Rename or relocate this file if you wish to preserve these results when you perform a new search.

## Troubleshooting

### Connection Errors:
- Ensure Semantra is running on the correct port and that the port in this utility matches.

### Insufficient Permissions:
- Verify you have permission to write to your chosen save location.

### No Results:
- Confirm that Semantra has finished indexing your files.
- Ensure that the query text is spelled correctly.
