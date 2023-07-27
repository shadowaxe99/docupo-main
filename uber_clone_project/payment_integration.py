import stripe
from schemas import PaymentSchema

stripe.api_key = "your_secret_key"

def processPayment(payment_data):
    try:
        payment_schema = PaymentSchema()
        validated_data = payment_schema.load(payment_data)

        charge = stripe.Charge.create(
            amount=validated_data['amount'],
            currency=validated_data['currency'],
            source=validated_data['source'],
            description=validated_data['description'],
        )

        return {
            'message': 'payment_success',
            'charge_id': charge.id
        }

    except Exception as e:
        return {
            'message': str(e)
        }
