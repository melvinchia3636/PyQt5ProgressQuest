from .conf import conf
from datetime import datetime

K = conf.K
Random = conf.Random
Pick = conf.Pick
GenerateName = conf.GenerateName

def RoughTime(s):
    if s < 120:
        return str(s) + " seconds"
    elif s < (60 * 120):
        return str(s // 60) + " minutes"
    elif s < (60 * 60 * 48):
        return str(s // 3600) + " hours"
    elif s < (60 * 60 * 24 * 60):
        return str(s // (3600 * 24)) + " days"
    elif s < (60 * 60 * 24 * 30 * 24):
        return str(s // (3600 * 24 * 30)) + " months"
    else:
        return str(s // (3600 * 24 * 30 * 12)) + " years"


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

    while (_rome(1000, "M")):
        ...
    _rome(900, "CM")
    _rome(500, "D")
    _rome(400, "CD")
    while (_rome(100, "C")):
        ...
    _rome(90, "XC")
    _rome(50, "L")
    _rome(40, "XL")
    while (_rome(10, "X")):
        ...
    _rome(9, "IX")
    _rome(5, "V")
    _rome(4, "IV")
    while (_rome(1, "I")):
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
    return s[RandomLow(s.length)]

def Copy(s, b, l):
    return s[b - 1:l]

def Ends(s, e):
    return Copy(s, 1 + len(s) - len(e), len(e)) == e

def Plural(s):
    if Ends(s, "y"):
        return Copy(s, 1, s.length - 1) + "ies"
    elif Ends(s, "us"):
        return Copy(s, 1, s.length - 2) + "i"
    elif Ends(s, "ch") or Ends(s, "x") or Ends(s, "s") or Ends(s, "sh"):
        return s + "es"
    elif Ends(s, "f"):
        return Copy(s, 1, s.length - 1) + "ves"
    elif Ends(s, "man") or Ends(s, "Man"):
        return Copy(s, 1, s.length - 2) + "en"
    else:
        return s + "s"

def Split(s, field, separator=None):
    return s.split(separator or "|")[field]

def Indefinite(s, qty):
    if qty == 1:
        if Pos(s[0], "AEIOU�aeiou�") > 0:
            return "an " + s
        else:
            return "a " + s
    else:
        return str(qty) + " " + Plural(s)

def Definite(s, qty):
    if qty > 1:
        s = Plural(s)
    return "the " + s

def Sick(m, s):
    m = 6 - abs(m)
    return prefix(
        ["dead", "comatose", "crippled", "sick", "undernourished"],
        m,
        s
    )


def Young(m, s):
    m = 6 - abs(m)
    return prefix(
        ["foetal", "baby", "preadolescent", "teenage", "underage"],
        m,
        s
    )


def Big(m, s):
    return prefix(["greater", "massive", "enormous", "giant", "titanic"], m, s)


def Special(m, s):
    if Pos(" ", s) > 0:
        return prefix(["veteran", "cursed", "warrior", "undead", "demon"], m, s)
    else:
        return prefix(
            ["Battle-", "cursed ", "Were-", "undead ", "demon "],
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
        Pick(K["ImpressiveTitles"]) +
        (" of the " + Pick(K["Races"])
         if Random(2) else " of " + GenerateName())
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

    return GenerateName() + " the " + result

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
    return InterestingItem() + " of " + Pick(K["ItemOfs"])


def InterestingItem():
    return Pick(K["ItemAttrib"]) + " " + Pick(K["Specials"])


def BoringItem():
    return Pick(K["BoringItems"])