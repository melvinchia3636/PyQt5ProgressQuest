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
