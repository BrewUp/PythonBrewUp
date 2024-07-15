import pytest

from ..DomainIds.BeerName import BeerName


def test_verify_equal():
    beerName1 = BeerName("IPA")
    beerName2 = BeerName("IPA")

    assert beerName1 == beerName2
