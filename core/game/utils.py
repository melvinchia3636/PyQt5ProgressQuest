from datetime import datetime
import json
from core.game.conf import conf

with open('core/game/config.json', encoding='utf-8') as f:
    K = json.load(f)

Random = conf.Random
Pick = conf.Pick
GenerateName = conf.GenerateName

def RoughTime(s):
    if s < 120:
        return str(s) + "秒"
    elif s < (60 * 120):
        return str(s // 60) + "分"
    elif s < (60 * 60 * 48):
        return str(s // 3600) + "时"
    elif s < (60 * 60 * 24 * 60):
        return str(s // (3600 * 24)) + "日"
    elif s < (60 * 60 * 24 * 30 * 24):
        return str(s // (3600 * 24 * 30)) + "月"
    else:
        return str(s // (3600 * 24 * 30 * 12)) + "年"


def toRoman(n):
    if not n:
        return "N"
    s = ""

    def _rome(dn, ds):
        nonlocal n, s
        if (n >= dn):
            n -= dn
            s += ds
            return True
        else:
            return False

    if (n < 0):
        s = "-"
        n = -n
    while _rome(10000, 'T'): 
        ...
    _rome(9000, 'MT')
    _rome(5000, 'A')
    _rome(4000, 'MA')

    while _rome(1000, "M"):
        ...
    _rome(900, "CM")
    _rome(500, "D")
    _rome(400, "CD")
    while _rome(100, "C"):
        ...
    _rome(90, "XC")
    _rome(50, "L")
    _rome(40, "XL")
    while _rome(10, "X"):
        ...
    _rome(9, "IX")
    _rome(5, "V")
    _rome(4, "IV")
    while _rome(1, "I"):
        ...
    return s


def toArabic(s):
    n = 0
    s = s.upper()

    def _arab(ds, dn):
        nonlocal n, s
        if not s.startswith(ds):
            return False

        s = s[len(ds):]
        n += dn
        return True
    
    while _arab(10000, 'T'): 
        ...
    _arab(9000, 'MT')
    _arab(5000, 'A')
    _arab(4000, 'MA')

    while (_arab("M", 1000)):
        ...
    _arab("CM", 900)
    _arab("D", 500)
    _arab("CD", 400)
    while (_arab("C", 100)):
        ...
    _arab("XC", 90)
    _arab("L", 50)
    _arab("XL", 40)
    while (_arab("X", 10)):
        ...
    _arab("IX", 9)
    _arab("V", 5)
    _arab("IV", 4)
    while (_arab("I", 1)):
        ...

    return n

def Odds(chance, outof):
    return Random(outof) < chance

def RandSign():
    return Random(2) * 2 - 1

def RandomLow(below):
    return min([Random(below), Random(below)])

def PickLow(s):
    return s[RandomLow(len(s))]

def Copy(s, b, l):
    return s[b - 1:l]

def Ends(s, e):
    return Copy(s, 1 + len(s) - len(e), len(e)) == e

def Plural(s):
    if Ends(s, "y"):
        return Copy(s, 1, len(s) - 1) + "ies"
    elif Ends(s, "us"):
        return Copy(s, 1, len(s) - 2) + "i"
    elif Ends(s, "ch") or Ends(s, "x") or Ends(s, "s") or Ends(s, "sh"):
        return s + "es"
    elif Ends(s, "f"):
        return Copy(s, 1, len(s) - 1) + "ves"
    elif Ends(s, "man") or Ends(s, "Man"):
        return Copy(s, 1, len(s) - 2) + "en"
    else:
        return s + "s"

def Split(s, field, separator=None):
    return s.split(separator or "|")[field]

def Indefinite(s, qty):
    if qty == 1:
        if s[0].upper() in "AEIOU":
            return "一个 " + s
        else:
            return "一个 " + s
    else:
        return str(qty) + " 个 " + Plural(s)

def Definite(s, qty):
    if qty > 1:
        s = Plural(s)
    return "这个 " + s

def Sick(m, s):
    m = 6 - abs(m)
    return prefix(
        ["死亡", "昏迷", "残废", "生病", "营养不良"],
        m,
        s
    )


def Young(m, s):
    m = 6 - abs(m)
    return prefix(
        ["胎儿", "婴儿", "青春期前", "青少年", "未成年"],
        m,
        s
    )


def Big(m, s):
    return prefix(["更巨大", "庞大", "巨大", "巨型", "泰坦般"], m, s)


def Special(m, s):
    if " " in s:
        return prefix(["老兵", "被诅咒的", "战士", "不死者", "恶魔"], m, s)
    else:
        return prefix(
            ["战斗-", "被诅咒的 ", "狼化-", "不死的 ", "恶魔 "],
            m,
            s,
            ""
        )

def Pos(needle, haystack):
    return (haystack.index(needle) if needle in haystack else -1) + 1

def prefix(a, m, s, sep=" "):
    m = abs(m)
    if (m < 1 or m > len(a)):
        return s
    return a[m - 1] + sep + s

def ImpressiveGuy():
    return (
        Pick(K["令人印象深刻的头衔"]) +
        (" 来自 " + Pick(K["种族"])
         if Random(2) else " 来自 " + GenerateName())
    )

def timeGetTime():
    return round(datetime.timestamp(datetime.now()) * 1000)

def NamedMonster(level):
    lev = 0
    result = ""
    for _ in range(5):
        m = Pick(K["Monsters"])
        if not result or abs(level - int(Split(m, 1))) < abs(level - lev):
            result = Split(m, 0)
            lev = int(Split(m, 1))

    return GenerateName() + " 这个 " + result

def LPick(list, goal):
    result = Pick(list)
    for _ in range(1, 6):
        best = int(Split(result, 1))
        s = Pick(list)
        b1 = int(Split(s, 1))
        if abs(goal - best) > abs(goal - b1):
            result = s
    return result

def SpecialItem():
    return InterestingItem() + " 之 " + Pick(K["ItemOfs"])


def InterestingItem():
    return Pick(K["ItemAttrib"]) + " " + Pick(K["Specials"])


def BoringItem():
    return Pick(K["BoringItems"])