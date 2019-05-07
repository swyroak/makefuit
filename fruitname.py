import random


def fruitname():
    tgt = chr(random.randrange(12449, 12534)) + \
        chr(random.randrange(12449, 12534))
    return tgt + tgt + "の実"


if __name__ == "__main__":
    print(fruitname())
