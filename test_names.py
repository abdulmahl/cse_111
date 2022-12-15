# Import modules 'names' and 'pytest'
# so that they can be used in this
# program.
from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Busta" , "Moon") == "Moon; Busta"
    assert make_full_name("Stanley" , "Tucci") == "Tucci; Stanley"
    assert make_full_name("Brain" , "Cage") == "Cage; Brain"
    assert make_full_name("Steff" , "Curry") == "Curry; Steff"
   
def test_extract_family_name():
    assert extract_family_name("Moon; Bobby") == "Moon"
    assert extract_family_name("Tucci; Stanley") == "Tucci"
    assert extract_family_name("Cage; Brain") == "Cage"
    assert extract_family_name("Curry; Steff") == "Curry"
   
def test_extract_given_name():
    assert extract_given_name("Moon; Bobby") == "Bobby"
    assert extract_given_name("Tucci; Stanley") == "Stanley"
    assert extract_given_name("Curry; Steff") == "Steff"

pytest.main(["-v", "--tb=line", "-rN", __file__])

