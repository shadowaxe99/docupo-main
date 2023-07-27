# src/multi_currency_support.py

class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {
            'USD': 1,
            'EUR': 0.85,
            'GBP': 0.75,
            'JPY': 110.53,
            # Add more currencies as needed
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError('Unsupported currency')

        from_rate = self.exchange_rates[from_currency]
        to_rate = self.exchange_rates[to_currency]

        return (amount / from_rate) * to_rate


def supportMultiCurrency(amount, from_currency, to_currency):
    converter = CurrencyConverter()
    return converter.convert(amount, from_currency, to_currency)
