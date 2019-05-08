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


def realfruit(ctrname):
    realnames = ['ガスガスの実', 'ユキユキの実', 'ウシウシの実', 'ヒトヒトの実', 'トリトリの実', 'イヌイヌの実', 'モグモグの実', 'ウマウマの実', 'ネコネコの実', 'ゾウゾウの実', 'ヘビヘビの実', 'サラサラの実', 'ムシムシの実', 'カメカメの実', 'リュウリュウの実', 'ゴムゴムの実', 'バラバラの実', 'スベスベの実', 'ボムボムの実', 'キロキロの実', 'ドルドルの実', 'バクバクの実', 'マネマネの実', 'ハナハナの実', 'スパスパの実', 'トゲトゲの実', 'オリオリの実', 'バネバネの実', 'ノロノロの実', 'ドアドアの実', 'アワアワの実', 'ベリベリの実', 'サビサビの実', 'シャリシャリの実', 'ヨミヨミの実', 'カゲカゲの実', 'ホロホロの実', 'スケスケの実', 'ニキュニキュの実', 'メロメロの実', 'ドクドクの実', 'ホルホルの実', 'チョキチョキの実',
                 'グラグラの実', 'キラキラの実', 'ウォシュウォシュの実', 'フワフワの実', 'マトマトの実', 'オペオペの実', 'フクフクの実', 'ブキブキの実', 'グルグルの実', 'ズシズシの実', 'バリバリの実', 'ヌイヌイの実', 'ギロギロの実', 'アトアトの実', 'ジャケジャケの実', 'イトイトの実', 'ホビホビの実', 'スイスイの実', 'ベタベタの実', 'ヒラヒラの実', 'イシイシの実', 'パムパムの実', 'トントンの実', 'ナギナギの実', 'チユチユの実', 'シロシロの実', 'ペロペロの実', 'ミラミラの実', 'ソルソルの実', 'ビスビスの実', 'バタバタの実', 'ブクブクの実', 'クリクリの実', 'シボシボの実', 'メモメモの実', 'タマタマの実', 'モチモチの実', 'ホヤホヤの実', 'ネツネツの実', 'ククククの実', 'ゴチャゴチャの実', 'オシオシの実', 'コブコブの実', 'ワラワラの実', 'トキトキの実']
    for realname in realnames:
        if realname == ctrname:
            return 'ある'
    return ''


def juddingstring(jstr, strlsts):
    for strlst in strlsts:
        if jstr == strlst:
            return True

    return False


if __name__ == "__main__":
    aa = fruitname()

    print(fruitname())
    if realfruit(fruitname):
        print('ある')
