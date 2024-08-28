import pytest

def pass_test():
    raise SystemExit(1)

def fail_test():
    assert 1 == 0