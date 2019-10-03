class Pencil:
    def __init__(self):
        self.durability = 20

    def write(self, text, paper):
        self.durability -= len(text)
        if text == 'A':
            self.durability -= 1
        paper.append(text)