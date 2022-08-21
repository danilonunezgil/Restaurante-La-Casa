import sys
from django.conf import settings
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AXwEU9R8QFdtHbiWdvVteT-7qaWvmJZ-xBq7J5ymkf8cO6RZhHabV2RVLyxJ06VmA5hvKCl6uE4Pmm9Q"
        self.client_secret = "EEPBZ92xOdFa81ozDzxUJY2zscwWyqXby-Gz62EMGkDAvoVrAm5auuDYuIxBcrsPoNokTbZAt6BDyw4r"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
