class Pencil:
    def __init__(self, durability=20):
        self.durability = durability

    def write(self, text, paper):
        durability_cost = Pencil._get_durability_cost_of_text(text)
        if durability_cost > self.durability:
            text = text[:-1] + ' '

        self.durability -= durability_cost
        paper.append(text)

    @staticmethod
    def _get_durability_cost_of_text(text):
        cost = 0
        for char in text:
            if char == ' ':
                pass
            elif char.isupper():
                cost += 2
            else:
                cost += 1
        return cost
