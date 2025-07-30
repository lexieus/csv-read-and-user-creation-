📊 CSV User Account Creator
A Python script to read a CSV file and create user accounts by sending HTTP POST requests to an API endpoint.

📄 Features
Reads user data from a CSV file (users.csv)

Sends a POST request for each valid user to a mock API

Skips rows with missing required fields (e.g., missing email)

Logs failed user creations and errors to error_log.txt

Modular code structure for better readability and maintainability

🛠️ Requirements
Python 3.x

requests module (install via pip install requests)

📦 Installation
bash
Copy
Edit
git clone https://github.com/your-username/csv-user-creator.git
cd csv-user-creator
pip install -r requirements.txt
📁 CSV Format
The input CSV file (users.csv) should have the following columns:

csv
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

📂 Project Files
File	Description
create_users.py	Main Python script
users.csv	Sample input CSV file
error_log.txt	Log file for failed user creations
requirements.txt	Dependencies list

🧪 Example Output
Terminal Output:

sql
Copy
Edit
Failed to create user: bob@example.com
error_log.txt:

pgsql
Copy
Edit
2025-07-30 10:23:45,123 - Failed to create user bob@example.com - Status code: 400
2025-07-30 10:23:45,456 - Skipping row due to missing required fields: {'name': 'Bob', 'email': '', 'role': 'user'}
