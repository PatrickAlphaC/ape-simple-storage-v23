from scripts.deploy_simple_storage import deploy_simple_storage
import pytest
import ape

SIMPLE_STORAGE_CONTRACT_LOCATION = "contracts/SimpleStorage.vy"


@pytest.fixture
def simple_storage_contract_ape() -> ape.contracts.base.ContractInstance:
    return deploy_simple_storage()
