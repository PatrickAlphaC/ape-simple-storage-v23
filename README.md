
# Getting Started

It's recommended that you've gone through the [apeworx getting started documentation](https://docs.apeworx.io/ape/stable/userguides/quickstart.html) before proceeding here. 


## Requirements

- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  - You'll know you did it right if you can run `git --version` and you see a response like `git version x.x.x`
- [Python](https://www.python.org/downloads/)
  - You'll know you've installed python right if you can run:
    - `python --version` or `python3 --version` and get an ouput like: `Python x.x.x`
- [pip](https://pypi.org/project/pip/)
  - You'll know you did it right if you can run `pip --version` or `pip3 --version` and get an output like `pip x.x from /some/path/here (python x.x)`
- [poetry](https://python-poetry.org/docs/)
  - You'll know you did it right if you can run `poetry --version` and get an output like `Poetry version (x.x.x)`

## Quickstart 

1. Clone the repo

```bash
git clone https://github.com/patrickalphac/ape-simple-storage-v23
cd ape-simple-storage-v23
```

2. Install dependencies

```bash
poetry install 
```

3. Run unit tests

```
poetry run pytest
```