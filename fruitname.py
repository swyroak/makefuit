import random


def fruitname():
    smallletterlists = [12449, 12451, 12453, 12455, 12457,
                        12483, 12515, 12517, 12519, 12526, 12533, 12534]
    rejectletterlists = [12528, 12529, 12530]
    nguss = [12531]

    str1 = random.randrange(12449, 12534)

    while juddingstring(str1, smallletterlists + rejectletterlists + nguss) is True:
        str1 = random.randrange(12449, 12534)

    str2 = random.randrange(12449, 12534)

    while juddingstring(str2, rejectletterlists) is True or str2 == str1:
        str2 = random.randrange(12449, 12534)

    str3 = random.randrange(12449, 12534)

    while juddingstring(str3, rejectletterlists) is True or str3 == str2:
        str3 = random.randrange(12449, 12534)

    while juddingstring(str2, smallletterlists) is True and juddingstring(str3, smallletterlists) is True:
        str3 = random.randrange(12449, 12534)

    if juddingstring(str3, smallletterlists) is True:
        return chr(str1) + chr(str2) + chr(str3) + chr(str1) + chr(str2) + chr(str3) + "の実"
    elif juddingstring(str2, smallletterlists) is True:
        return chr(str1) + chr(str2) + chr(str3) + chr(str1) + chr(str2) + chr(str3) + "の実"
    else:
        return chr(str1) + chr(str2) + chr(str1) + chr(str2) + "の実"


def juddingstring(jstr, strlsts):
    for strlst in strlsts:
        if jstr == strlst:
            return True

    return False


if __name__ == "__main__":
    print(fruitname())
