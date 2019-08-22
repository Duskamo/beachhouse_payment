
from data.Config import Config
import stripe

class PaymentApi:
	def __init__(self, tokenId):
		self.tokenId = tokenId
		stripe.api_key = Config.stripe_sk

	def sendPayment(self, amount):
		charge = stripe.Charge.create(
		    amount=int(amount),
		    currency='usd',
		    description='Beach House Rental Charge',
		    source=self.tokenId,
		)

	
