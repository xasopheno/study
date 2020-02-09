from typing import List


def lcs(seq1, seq2):
    m, n = len(seq1), len(seq2)
    table = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif seq1[i - 1] == seq2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table, table[m][n]


# Driver program to test the above function
seq1 = "AGGTAB"
seq2 = "GXTXAYB"

table, length = lcs(seq1, seq2)
print("longest_len:", length)


def find_max_seq(table: List[List[int]]):
    for row in table:
        print(row)

    m = len(seq1)
    n = len(seq2)

    result = ""

    # while current != 0:
    while True:
        print(m, n)
        current = table[m][n]
        if current == 0:
            break
        if table[m - 1][n] != current and table[m][n - 1] != current:
            result += seq1[m - 1]
            m -= 1
            n -= 1
            print("result", result)
        elif table[m - 2][n] > table[m][n - 2]:
            m -= 1
        else:
            n -= 1


find_max_seq(table)

