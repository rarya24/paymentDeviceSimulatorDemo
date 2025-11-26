# terminal/terminal.py

import logging

class PaymentTerminal:
    def __init__(self):
        self.state = "OFF"
        logging.info("Terminal created. State=OFF")

    def power_on(self):
        self.state = "READY"
        logging.info("Power ON → READY")

    def insert_card(self):
        if self.state == "READY":
            self.state = "CARD_INSERTED"
            logging.info("Card inserted → CARD_INSERTED")
        else:
            self._error("Cannot insert card when not READY")

    def enter_pin(self):
        if self.state == "CARD_INSERTED":
            self.state = "PIN_ENTERED"
            logging.info("PIN Entered → PIN_ENTERED")
        else:
            self._error("Cannot enter PIN now")

    def start_payment(self, amount):
        if self.state == "PIN_ENTERED":
            self.state = "PROCESSING"
            logging.info(f"Processing {amount}…")
        else:
            self._error("Cannot start payment now")

    def acquirer_response(self, result):
        if self.state != "PROCESSING":
            self._error("Unexpected acquirer response")
            return

        if result == "APPROVED":
            self.state = "APPROVED"
        else:
            self.state = "DECLINED"
        logging.info(f"Result → {self.state}")

    def _error(self, msg):
        logging.error(msg)
        self.state = "ERROR"
        logging.info("State → ERROR")
