import pytest
from app import is_prime


def test_is_prime_negative_and_zero_and_one():
    assert is_prime(-10) is False
    assert is_prime(-1) is False
    assert is_prime(0) is False
    assert is_prime(1) is False


def test_is_prime_small_primes():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(11) is True


def test_is_prime_small_non_primes():
    assert is_prime(4) is False
    assert is_prime(6) is False
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(10) is False


def test_is_prime_large_prime_and_composite():
    assert is_prime(104729) is True   # 10000th prime
    assert is_prime(104730) is False


if __name__ == "__main__":
    pytest.main(["-v"])
