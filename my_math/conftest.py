import pytest
@pytest.fixture
def max_number():
    return 5
def pytest_generate_tests(metafunc):
    if "max_number" in metafunc.fixturenames:
    # end can be retrived from command line parameters
        end = 10
        metafunc.parametrize("max_number", range(end)