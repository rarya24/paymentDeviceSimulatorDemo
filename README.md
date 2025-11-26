A payment terminal device simulator combined with a Pytest-based firmware automation suite, designed to demonstrate:

-Firmware-style device state machine design
-Python OOP concepts
-Automated happy path , negative, and end-to-end testing
-Python logging (firmware-style log generation)
-CI/CD integration using GitHub Actions

Project Overview

Firmware devices such as payment terminals and network cards follow a state-machine-driven workflow.

This project recreates a small portion of that behaviour through:

✔ A Python-based Payment Terminal Simulator

Models device states like:

OFF → READY → CARD_INSERTED → PIN_ENTERED → PROCESSING → APPROVED/DECLINED

Enforces valid vs invalid device actions

Produces firmware-style logs

Used for automated testing and CI

✔ A Pytest Automation Suite

Includes:

Happy-path tests

Declined transactions

Invalid/negative scenarios

End-to-end flow

✔ Logging

All actions are written to:

logs/terminal.log


Simulating real firmware log output.

✔ CI/CD

A GitHub Actions pipeline runs all tests automatically on every push/PR.
