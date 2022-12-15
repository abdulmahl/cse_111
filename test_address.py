from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city(" 525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("406 mlz St, Mamelodi, PTA 0122") == "Mamelodi"
    assert extract_city("432 Blue St, Honolulu, HW 55645") == "Honolulu"

def test_exatract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("406 mlz St, Mamelodi, PTA 0122") == "PTA"
    assert extract_state("432 Blue St, Honolulu, HW 55645") == "HW"

def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("406 mlz St, Mamelodi, PTA 0122") == "0122"
    assert extract_zipcode("432 Blue St, Honolulu, HW 55645") == "55645"

pytest.main(["-v", "--tb=line", "-rN", __file__])