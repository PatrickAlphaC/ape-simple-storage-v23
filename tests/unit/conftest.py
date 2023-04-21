import pytest
import boa

SIMPLE_STORAGE_CONTRACT_LOCATION = "contracts/SimpleStorage.vy"


@pytest.fixture
def simple_storage_boa() -> boa.vyper.contract.VyperContract:
    return boa.load(SIMPLE_STORAGE_CONTRACT_LOCATION)
