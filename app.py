from flask import Flask, request
import os
app = Flask(__name__)

# Data POST Requests
@app.route('/pay', methods=['POST'])
def pay():
	# Gather Data
	paymentInfo = request.json
	
	# Send payment info to paypal using api
	print(paymentInfo["cardNumber"])

	# Return status code
	return "200"

# Run app on 0.0.0.0:5001
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5003))
	app.run(host='0.0.0.0', port=port)
