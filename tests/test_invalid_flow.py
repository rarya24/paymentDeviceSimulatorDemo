# tests/test_invalid_flow.py

from terminal.terminal import PaymentTerminal

def test_invalid_flow():
    t = PaymentTerminal()

    t.power_on()
    t.start_payment(5)   # invalid, no card inserted

    assert t.state == "ERROR"
