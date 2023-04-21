def test_deploy_simple_storage(simple_storage_boa):
    assert simple_storage_boa.retrieve() == 0


def test_store(simple_storage_boa):
    simple_storage_boa.store(15)
    assert simple_storage_boa.retrieve() == 15
