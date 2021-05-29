import pytest
from challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter

# add new animals (dog or cat)
def test_1 (Shelter):
    Shelter.enqueue('cat')
    actual = Shelter.__str__()
    expected = ' - dog - cat - dog - cat'
    assert actual == expected

# add new animals (not dog or cat)
def test_2 (Shelter):
    Shelter.enqueue('lion')
    actual = Shelter.__str__()
    expected = ' - dog - cat - dog'
    assert actual == expected

# dequeue from front
def test_3 (Shelter):
    Shelter.dequeue('dog')
    actual = Shelter.__str__()
    expected = ' - cat - dog'
    assert actual == expected

# dequeue from middle
def test_4 (Shelter):
    Shelter.dequeue('cat')
    actual = Shelter.__str__()
    expected = ' - dog - dog'
    assert actual == expected

@pytest.fixture
def Shelter():
    dogCat = AnimalShelter()
    dogCat.enqueue('dog')
    dogCat.enqueue('cat')
    dogCat.enqueue('dog')

    return dogCat

