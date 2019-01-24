import pytest
import random

@pytest.fixture()
def random_id_generator():
    return random.randint(1,21)

