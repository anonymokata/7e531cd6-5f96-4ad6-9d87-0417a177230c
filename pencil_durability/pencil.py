class Pencil:
    def __init__(self):
        self.durability = 20

    def write(self, text, paper):
        paper.append(text)