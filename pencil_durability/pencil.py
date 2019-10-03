WHITESPACE_CHARACTER_COST = 0
UPPERCASE_CHARACTER_COST = 2
LOWERCASE_CHARACTER_COST = 1
DEFAULT_DURABILITY = 20
DEFAULT_LENGTH = 10


class Pencil:
    def __init__(self, durability=DEFAULT_DURABILITY, length=DEFAULT_LENGTH):
        self.initial_durability = durability
        self.durability = durability if durability >= 0 else 0
        self.length = length if length >= 0 else 0

    def write(self, text, paper):
        for char in text:
            self._write_character(char, paper)

    def _write_character(self, char, paper):
        cost = Pencil._determine_cost_of_character(char)
        self._write_character_to_paper(char, cost, paper)
        self._reduce_durability_by_character_cost(cost)

    def _reduce_durability_by_character_cost(self, cost):
        self.durability -= cost

    def _write_character_to_paper(self, char, cost, paper):
        character_to_append = ' '
        if self._can_afford_character(cost):
            character_to_append = char
        paper.append(character_to_append)

    def _can_afford_character(self, cost):
        return self.durability >= cost

    @staticmethod
    def _determine_cost_of_character(char):
        if char.isspace():
            return WHITESPACE_CHARACTER_COST

        if char.isupper():
            return UPPERCASE_CHARACTER_COST

        return LOWERCASE_CHARACTER_COST

    def sharpen(self):
        if self.length == 0:
            return

        self.length -= 1
        self.durability = self.initial_durability

    def erase(self, text, paper):
        replacement = ' ' * len(text)
        reversed_paper_text = paper.text[::-1]
        reversed_text = text[::-1]
        paper.text = reversed_paper_text.replace(reversed_text, replacement, 1)[::-1]