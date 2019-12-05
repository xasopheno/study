from typing import List, Set


class String:
    def __init__(self, value: str):
        self.value = value

    def clean(self):
        ignore_chars = [
            "'",
            ".",
            ",",
            " ",
        ]
        input = self.value
        input = input.lower()
        for char in ignore_chars:
            input = input.replace(char, "")

        return input

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def is_palindrome(self) -> bool:
        clean = self.clean()

        return clean == clean[::-1]

    def is_palindrome_manual(self) -> bool:
        clean = list(self.clean())

        i = 0
        j = len(clean) - 1

        while j > i:
            if clean[i] != clean[j]:
                return False
            i += 1
            j -= 1

        return True

    def dedupe(self) -> str:
        input = list(self.value)
        seen: Set[str] = set()
        result: List[str] = []
        for value in input:
            if value not in seen:
                result += [value]
                seen.add(value)

        return ("").join(result)

    def reverse_substring_at_token(self, s: str) -> str:
        result: List[str] = []
        for sub_string in self.value.split(s):
            result += [sub_string[::-1]]

        return s.join(result)

    def reverse_substring_in_group(self, n: int) -> str:

        print("\n\n")
        substrings: List[str] = []
        substring = ""
        for i in range(len(self.value)):
            substring += self.value[i]

            if (i > 0) and (i + 1) % n == 0 or i == len(self.value) - 1:
                substrings += [substring[::-1]]
                substring = ""

        return "".join(substrings)

