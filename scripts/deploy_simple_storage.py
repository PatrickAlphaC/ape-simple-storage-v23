from ape import project
from scripts.helper_functions import get_account


def deploy_simple_storage(unlock_password=None) -> project.SimpleStorage:
    account = get_account(unlock_password=unlock_password)
    simple_storage = account.deploy(project.SimpleStorage)
    return simple_storage


def main():
    deploy_simple_storage()
