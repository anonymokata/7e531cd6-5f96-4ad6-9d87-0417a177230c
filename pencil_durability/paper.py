class Paper:
    def __init__(self, text=''):
        self.text = text

    def append(self, text):
        self.text = self.text + text