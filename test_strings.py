from nose2.tools import such  # type: ignore
from strings import String

with such.A("String") as it:

    @it.should("test for palindrome")
    def test_palendrome():
        input = "Madam I'm Adam"
        palindrome = String(input).is_palindrome()
        it.assertEqual(palindrome, True)

        input = "asdf"
        palindrome = String(input).is_palindrome()
        it.assertEqual(palindrome, False)

        input = "Madam I'm Adam"
        palindrome = String(input).is_palindrome_manual()
        it.assertEqual(palindrome, True)

        input = "asdf"
        palindrome = String(input).is_palindrome_manual()
        it.assertEqual(palindrome, False)

    @it.should("remove duplicates")
    def test_remove_duplicates():
        input = String("aabccdddefggaa")
        expected = "abcdefg"
        it.assertEqual(input.dedupe(), expected)

    @it.should("reverse substrings at tokens")
    def test_reverse_substrings_at_token():
        input = String("abc def hi")
        expected = "cba fed ih"
        result = input.reverse_substring_at_token(" ")
        it.assertEqual(result, expected)

        input = String("abc/def/hi")
        expected = "cba/fed/ih"
        result = input.reverse_substring_at_token("/")
        it.assertEqual(result, expected)

    @it.should("reverse substrings in groups")
    def test_reverse_substrings_in_groups():
        input = String("abcdefhi")
        expected = "cbafedih"
        result = input.reverse_substring_in_group(3)
        it.assertEqual(result, expected)


it.createTests(globals())
