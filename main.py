import pytest


class Main:

    def __init__(self):
        retcode = pytest.main()
        del [retcode]


if __name__ == "__main__":
    Main()
