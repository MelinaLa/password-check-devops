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

# ////

def test_long_password():
	assert is_valid_password('Abcdef1!' * 10) == True

def test_password_with_spaces():
	assert is_valid_password('Abc def1!') == True

def test_only_special_chars():
	assert is_valid_password('!@#$%^&*') == False

def test_only_digits():
	assert is_valid_password('12345678') == False

def test_only_letters():
	assert is_valid_password('Abcdefgh') == False

def test_unicode_characters():
	assert is_valid_password('Äbcdef1!') == True

def test_empty_string():
	assert is_valid_password('') == False

