import random
from magic_number import *
import pytest

def test_main():
    # Create magic_number.
    magic_number = []

    assert len(magic_number) == 0

    for guess in magic_number:
        assert isinstance(guess, int)
        assert len(guess) >= 1
   
pytest.main(["-v", "--tb=line", "-rN", __file__])
