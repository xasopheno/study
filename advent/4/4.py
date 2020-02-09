# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).


def dup(i: int) -> bool:
    s = str(i)
    t1 = [s[0] == s[1] and s[0] != s[2]]
    t2 = [
        s[j] == s[j - 1] and s[j] != s[j - 2] and s[j] != s[j + 1]
        for j in range(2, len(s) - 1)
    ]
    t3 = [s[4] == s[5] and s[3] != s[4]]
    return any(t1 + t2 + t3)


def inc(i: int) -> bool:
    s = str(i)
    r = [int(s[j]) >= int(s[j - 1]) for j in range(1, len(s))]
    return all(r)


result = [i for i in range(264793, 803935 + 1) if all([dup(i), inc(i)])]

print(result)

print(len(result))


