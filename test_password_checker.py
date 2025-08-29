# test_password_checker.py
import pytest
from password_checker import is_valid_password

def test_valid_password():
	assert is_valid_password('Abcdef1!') == True

def test_too_short():
	assert is_valid_password('Ab1!') == False

def test_no_digit():
	assert is_valid_password('Abcdefgh!') == False

def test_no_uppercase():
	assert is_valid_password('abcdef1!') == False

def test_no_lowercase():
	assert is_valid_password('ABCDEF1!') == False

def test_no_special_char():
	assert is_valid_password('Abcdef12') == False

