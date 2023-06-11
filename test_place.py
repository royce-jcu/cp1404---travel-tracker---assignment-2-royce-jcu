"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    assert new_place.name == "Malagar"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert not new_place.is_visited

    # TODO: Write tests to show this initialisation works
    # Test setting new values
    print("Test setting new values:")
    new_place.name = "Barcelona"
    new_place.country = "Spain"
    new_place.priority = 2
    new_place.is_visited = True
    assert new_place.name == "Barcelona"
    assert new_place.country == "Spain"
    assert new_place.priority == 2
    assert new_place.is_visited

    # TODO: Add more tests, as appropriate, for each method
    # Test __str__() method
    print("Test __str__() method:")
    place_str = str(new_place)
    assert place_str == "Place: Barcelona, Country: Spain, Priority: 2, Visited: True"


run_tests()
