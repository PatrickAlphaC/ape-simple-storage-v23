from ape import networks, accounts

# All local chains across "ecosystems" have the same name
LOCAL_CHAIN_NAMES = ["local", "development"]
FORKED_CHAIN_NAMES = ["mainnet-fork"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if networks.active_provider.network.name in LOCAL_CHAIN_NAMES:
        return accounts.test_accounts[0]
    if (
        networks.active_provider.chain_id == 31337
        or networks.active_provider.chain_id == 1337
    ):
        return accounts.load("local-default")
    return accounts.load("default")


def main():
    pass
