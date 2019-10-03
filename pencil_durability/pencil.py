class Pencil:
    def __init__(self, durability=20):
        self.durability = durability

    def write(self, text, paper):
        for char in text:
            self._write_character(char, paper)

    def _write_character(self, char, paper):
        cost = Pencil._determine_cost_of_character(char)
        character_to_append = ' '
        if char.isspace():
            character_to_append = char
        elif char.isupper() and self.durability >= 2:
            character_to_append = char
        elif self.durability >= 1:
            character_to_append = char

        paper.append(character_to_append)
        self.durability -= cost

    @staticmethod
    def _determine_cost_of_character(char):
        if char.isspace():
            return 0

        if char.isupper():
            return 2

        return 1

