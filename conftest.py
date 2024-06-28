import pytest

@pytest.fixture(scope="module")
def base_url():
    return 'https://espo.spartan-soft.com/api/v1'
