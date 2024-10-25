from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to serve the index.html file
@app.route('/')
def index():
		return render_template('index.html')

# Route to handle the POST request from the client
@app.route('/save_email', methods=['POST'])
def save_email():
		# Get the email from the POST request
		email = request.json.get('email')

		# Store the email in a text file (append mode)
		with open('emails.txt', 'a') as file:
				file.write(email + '\n')

		# You can perform additional actions here if needed

		# Return a JSON response indicating success
		return jsonify({'message': 'Email saved successfully'})

app.run(host='0.0.0.0', port=8080)

