import pytest


def test_error_print():
	assert 1 == 2, "More message"

def test_error_message_failure():

	def fail_message():
		raise ValueError("some error")

	assert 1 == 2, f"{fail_message()}"
