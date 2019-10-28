from pencil_durability.string_utilities import reverse_string_replace


class Paper:
    def __init__(self, text=''):
        self.text = text

    def append(self, text):
        self.text = self.text + text

    def replace_last_with(self, old, new):
        self.text = reverse_string_replace(self.text, old, new, 1)

    def insert(self, text_to_insert, start_index):
        self.text = self.text[:start_index] + text_to_insert + self.text[start_index + len(text_to_insert):]
