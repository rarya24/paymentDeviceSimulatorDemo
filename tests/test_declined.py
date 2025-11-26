# tests/test_declined.py

from terminal.terminal import PaymentTerminal

def test_declined_payment():
    t = PaymentTerminal()

    t.power_on()
    t.insert_card()
    t.enter_pin()
    t.start_payment(20)
    t.acquirer_response("DECLINED")

    assert t.state == "DECLINED"
