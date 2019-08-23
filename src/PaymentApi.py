
from data.Config import Config
import stripe

class PaymentApi:
	def __init__(self, paymentInfo):
		self.paymentInfo = paymentInfo
		stripe.api_key = Config.stripe_sk

	def sendPayment(self):
		charge = stripe.Charge.create(
		    amount=int(self.paymentInfo['paymentAmount']),
		    currency='usd',
		    description='Beach House Rental Charge',
		    source=self.paymentInfo['tokenId'],
		    receipt_email=self.paymentInfo['receiptEmail']
		)

	
