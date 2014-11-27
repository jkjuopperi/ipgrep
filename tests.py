# ipgrep tests
#
# To run:
#
# pip install pytest
# py.test tests.py
#
# OR tests python 2.7 and 3.4 in one go:
#
# tox

from ipgrep import parse_addr, check_ip, grep


def test_check_ip_identical():
    assert check_ip("127.0.0.1", "127.0.0.1") is True


def test_check_ip_no_match():
    assert check_ip("127.0.0.2", "127.0.0.1") is False


def test_check_ip_by_slash_mask():
    assert check_ip("127.0.0.0/8", "127.0.0.1") is True


def test_check_ip_by_m_mask():
    assert check_ip("127.0.0.0m8", "127.0.0.1") is True


def test_check_ip_by_m_mask_without_match():
    assert check_ip("127.0.0.0m8", "128.0.0.0") is False
