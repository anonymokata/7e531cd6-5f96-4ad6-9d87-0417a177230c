from pencil_durability.string_utilities import reverse_string_replace


class Paper:
    def __init__(self, text=''):
        self.text = text

    def append(self, text):
        self.text = self.text + text

    def replace_last_with(self, old, new):
        self.text = reverse_string_replace(self.text, old, new, 1)
