class Pencil:
    def __init__(self, durability=20):
        self.durability = durability

    def write(self, text, paper):
        for char in text:
            self._write_character(char, paper)

    def _write_character(self, char, paper):
        cost = Pencil._determine_cost_of_character(char)

        character_to_append = ' '
        if self._can_afford_character(cost):
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

    def _can_afford_character(self, cost):
        return self.durability >= cost

