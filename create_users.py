import csv
import requests
import logging

# Configure logging to write errors to a file
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(message)s')

def is_valid_user(row):
    """
    Check if the required fields are present in the row.
    Currently only checks for a non-empty email field.
    """
    return row.get("email") not in (None, "")

def create_user(user_data):
    """
    Send a POST request to create a user.
    Returns True if successful, False otherwise.
    """
    try:
        response = requests.post("https://example.com/api/create_user", json=user_data)
        if response.status_code == 201:
            return True
        else:
            # Log failed attempt with status code
            logging.error(f"Failed to create user {user_data.get('email')} - Status code: {response.status_code}")
            return False
    except requests.RequestException as e:
        # Log exception error
        logging.error(f"Exception occurred while creating user {user_data.get('email')}: {e}")
        return False

def create_users(file_path):
    """
    Read users from a CSV file and attempt to create each one.
    Skips rows with missing required fields.
    """
    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Skip invalid rows (e.g., missing email)
                if not is_valid_user(row):
                    logging.error(f"Skipping row due to missing required fields: {row}")
                    continue
                # Attempt to create the user
                success = create_user(row)
                if not success:
                    print(f"Failed to create user: {row.get('email')}")
    except FileNotFoundError:
        logging.error(f"CSV file not found: {file_path}")
        print(f"File not found: {file_path}")
    except Exception as e:
        logging.error(f"Unexpected error while processing file {file_path}: {e}")
        print(f"Unexpected error: {e}")

# Entry point
if __name__ == "__main__":
    create_users("users.csv")
