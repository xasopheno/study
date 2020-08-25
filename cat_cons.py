class Cons:
    def __init__(self, hd, tl):
        self.hd = hd
        self.tl = tl

    def __str__(self):
        return list_print(self)

    def __repr__(self):
        return str(self)


def is_cons(lis):
    return isinstance(lis, Cons)


def is_list(lis):
    return lis is None or is_cons(lis) and is_list(tail(lis))


def mklist(*elems):
    if elems:
        return cons(elems[0], mklist(*elems[1:]))
    return None


def list_print(lis):
    def s(x):
        if isinstance(x, str):
            return repr(x)
        return str(x)

    def listbody(lis):
        if lis is None:
            return ""
        elif not is_cons(lis):
            return ". " + s(lis)
        elif tail(lis) is None:
            return s(head(lis))
        else:
            return s(head(lis)) + " " + listbody(tail(lis))

    if not is_cons(lis):
        raise TypeError(f"{lis} is not a cons")
    return "(" + listbody(lis) + ")"


def cons(hd, tl):
    return Cons(hd, tl)


def head(lis):
    if lis is None:
        return None
    return lis.hd


def tail(lis):
    if lis is None:
        return None
    return lis.tl


def take(lis, n):
    if n <= 0 or lis is None:
        return None
    return cons(head(lis), take(tail(lis), n - 1))


def drop(lis, n):
    if n <= 0 or lis is None:
        return lis
    return drop(tail(lis), n - 1)
