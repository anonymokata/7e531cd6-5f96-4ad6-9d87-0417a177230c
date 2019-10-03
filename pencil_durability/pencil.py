class Pencil:
    def __init__(self):
        self.durability = 20

    def write(self, text, paper):
        self.durability -= Pencil._get_durability_cost_of_text(text)

        paper.append(text)

    @staticmethod
    def _get_durability_cost_of_text(text):
        cost = len(text)
        if text == 'A':
            cost += 1
        return cost