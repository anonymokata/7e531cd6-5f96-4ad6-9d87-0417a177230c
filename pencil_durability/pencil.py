class Pencil:
    def __init__(self):
        self.durability = 20

    def write(self, text, paper):
        self.durability -= self._get_durability_cost_of_text(text)

        paper.append(text)

    def _get_durability_cost_of_text(self, text):
        cost = len(text)
        if text == 'A':
            cost += 1
        return cost