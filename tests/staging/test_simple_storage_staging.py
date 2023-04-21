from scripts.deploy_simple_storage import deploy_simple_storage
import pytest
from scripts.helper_functions import get_account


@pytest.mark.staging
def test_store(simple_storage_contract_ape):
    account = get_account()
    simple_storage_contract_ape.store(15, sender=account)
    assert simple_storage_contract_ape.retrieve() == 15
