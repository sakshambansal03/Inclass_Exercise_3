import pytest
from prime_palindrome_module import is_palindrome, is_prime

# ------------------------------------------
# PALINDROME SPEC-GUIDED TESTS
# ------------------------------------------

def norm(s):
    return "".join(ch.lower() for ch in s if ch.isalnum())

def test_palindrome_spec_empty_normalized():
    s = "!!! ???"
    assert norm(s) == ""
    assert is_palindrome(s) == True

def test_palindrome_spec_true_basic():
    s = "A man, a plan, a canal: Panama"
    assert norm(s) == norm(s)[::-1]
    assert is_palindrome(s) == True

def test_palindrome_spec_numeric_palindrome():
    s = "12321"
    assert norm(s) == norm(s)[::-1]
    assert is_palindrome(s) == True

def test_palindrome_spec_false_basic():
    s = "Hello"
    assert norm(s) != norm(s)[::-1]
    assert is_palindrome(s) == False

def test_palindrome_spec_case_insensitive():
    s = "RaceCar!!!"
    assert norm(s) == "racecar"
    assert is_palindrome(s) == True

def test_palindrome_spec_mixed_false():
    s = "abc123"
    assert norm(s) != norm(s)[::-1]
    assert is_palindrome(s) == False

# ------------------------------------------
# PRIME SPEC-GUIDED TESTS
# ------------------------------------------

def test_prime_spec_nonpositive():
    for n in [-10, -1, 0, 1]:
        assert is_prime(n) == False

def test_prime_spec_two():
    assert is_prime(2) == True

def test_prime_spec_even_composites():
    for n in [4, 6, 8, 10, 100]:
        assert is_prime(n) == False

def test_prime_spec_odd_primes():
    for n in [3, 5, 7, 11, 13, 17, 19]:
        assert is_prime(n) == True

def test_prime_spec_composite_odd():
    for n in [9, 15, 21, 25, 27, 33]:
        assert is_prime(n) == False

def test_prime_spec_large_values():
    assert is_prime(97) == True
    assert is_prime(99) == False
