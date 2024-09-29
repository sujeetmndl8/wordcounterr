import os
import bcrypt
import getpass
from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Get the username and password from environment variables
stored_username = os.getenv("FLASK_USERNAME")
stored_password = os.getenv("FLASK_PASSWORD")

if not stored_username or not stored_password:
    print("Error: Environment variables for username or password are not set.")
    exit(1)

# Hash the stored password (this will be done the first time, when setting up)
stored_hashed_password = bcrypt.hashpw(stored_password.encode('utf-8'), bcrypt.gensalt())

def verify_credentials():
    # Ask for the username and password
    entered_username = input("Enter your username: ")
    entered_password = getpass.getpass("Enter your password: ")

    # Compare the entered credentials with stored credentials
    if entered_username == stored_username and bcrypt.checkpw(entered_password.encode('utf-8'), stored_hashed_password):
        print("Access granted.")
        
    else:
        print("Access denied.")
        exit(1)  # Exit if the credentials are incorrect

# Verify credentials before starting the app
verify_credentials()

@app.route('/')
def index():
    return render_template('index.html')  # Render the main HTML page

@app.route('/count_words_and_characters', methods=['POST'])
def count_words_and_characters():
    text = request.json['text']  # Get the text from the JSON request
    word_count = len(text.split())  # Count the number of words
    char_count = len(text)  # Count the number of characters

    # Simulating a delay for the loading animation
    time.sleep(3)

    # Return the counts as JSON
    return jsonify({'word_count': word_count, 'char_count': char_count})

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
    exit(1)
