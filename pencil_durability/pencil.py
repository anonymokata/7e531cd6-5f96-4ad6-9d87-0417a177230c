class Pencil:
    def __init__(self, durability=20):
        self.durability = durability

    def write(self, text, paper):
        for char in text:
            self._write_character(char, paper)

    def _write_character(self, char, paper):
        cost = Pencil._determine_cost_of_character(char)
        if char.isspace():
            paper.append(char)
        elif char.isupper() and self.durability >= 2:
            paper.append(char)
        elif self.durability >= 1:
            paper.append(char)
        else:
            paper.append(' ')

        self.durability -= cost

    @staticmethod
    def _determine_cost_of_character(char):
        if char.isspace():
            return 0

        if char.isupper():
            return 2

        return 1

