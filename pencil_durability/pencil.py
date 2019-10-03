class Pencil:
    def __init__(self, durability=20):
        self.durability = durability

    def write(self, text, paper):
        for char in text:
            if char.isspace():
                paper.append(char)
            elif char.isupper() and self.durability >= 2:
                paper.append(char)
                self.durability -= 2
            elif self.durability >= 1:
                paper.append(char)
                self.durability -= 1
            else:
                paper.append(' ')
        # paper.append(text)

