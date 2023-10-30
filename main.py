class String:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]

    def count_words(self):
        return len(self.string.split())

    def capitalize(self):
        return self.string.capitalize()

    def is_palindrome(self):
        temp_string = self.string.lower().replace(" ", "")
        return temp_string == temp_string[::-1]

    def concatenate(self, other_string):
        return self.string + other_string

    def find_common_characters(self, other_string):
        common_chars = set(self.string) & set(other_string)
        return "".join(common_chars)

    def find_unique_characters(self, other_string):
        unique_chars = set(self.string) - set(other_string)
        return "".join(unique_chars)

    def count_occurrences(self, sub_string):
        return self.string.count(sub_string)

