# tests/test_happy_path.py

from terminal.terminal import PaymentTerminal
from terminal.logger import setup_logging

def test_happy_path():
    setup_logging()
    t = PaymentTerminal()

    t.power_on()
    assert t.state == "READY"

    t.insert_card()
    assert t.state == "CARD_INSERTED"

    t.enter_pin()
    assert t.state == "PIN_ENTERED"

    t.start_payment(10)
    assert t.state == "PROCESSING"

    t.acquirer_response("APPROVED")
    assert t.state == "APPROVED"
