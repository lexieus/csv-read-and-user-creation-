# csv-read-and-user-creation-
Python script to read a CSV file and create user accounts.
👤 User Account Creator from CSV
This script automates the creation of user accounts by reading data from a CSV file and sending HTTP POST requests to an API endpoint.

📄 Features
Reads user data from a CSV file (users.csv).

Sends a POST request for each valid user to a mock API.

Skips rows with missing required fields (e.g., missing email).

Logs errors and failed user creations to error_log.txt.

Uses modular code structure for maintainability.

🛠️ Requirements
Python 3.x

requests module (Install via pip install requests)

📦 Installation
bash
Copy
Edit
git clone <your-repo-url>
cd <project-directory>
pip install requests
📁 CSV Format
Input CSV file (users.csv) should have the following columns:

c
Copy
Edit
name,email,role
Alice,alice@example.com,admin
Bob,,user
Charlie,charlie@example.com,moderator
Rows with missing email will be skipped and logged.

🚀 Usage
bash
Copy
Edit
python create_users.py
Make sure your users.csv file is in the same directory or update the script with the correct file path.

📂 Files
create_users.py: Main Python script.

users.csv: Sample input CSV file.

error_log.txt: Log file where failed user creation attempts are stored.

🧪 Example Output
Terminal:

bash
Copy
Edit
Failed to create user: bob@example.com
error_log.txt:

txt
Copy
Edit
2025-07-30 10:23:45,123 - Failed to create user bob@example.com - Status code: 400
2025-07-30 10:23:45,456 - Skipping row due to missing required fields: {'name': 'Bob', 'email': '', 'role': 'user'}
💡 Suggestions for Improvement
Add command-line argument support for custom file paths.

Validate email format using regex.

Log successful creations optionally.

Retry logic for transient API failures.

