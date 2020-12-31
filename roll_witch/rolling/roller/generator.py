import random
from os import urandom


_instance = None


class RandomNumberGenerator:
    def __init__(self) -> None:
        super().__init__()
        random.seed(urandom(15))

    def get_int(self, less_than):
        return random.randint(1, less_than)


def get_instance():
    global _instance
    if not _instance:
        _instance = RandomNumberGenerator()

    return _instance
