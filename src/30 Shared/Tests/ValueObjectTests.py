import pytest
from ..DomainIds.BeerName import BeerName 

@pytest.fixture
def verify_equal():
  beerName1 = BeerName("IPA")
  beerName2 = BeerName("IPA")

  assert beerName1 == beerName2