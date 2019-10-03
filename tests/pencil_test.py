import unittest

from pencil_durability.paper import Paper
from pencil_durability.pencil import Pencil


class PencilTests(unittest.TestCase):
    def test_pencil_writes_text_to_paper(self):
        pencil = Pencil()
        paper = Paper()

        pencil.write('Sally sells sea shells', paper)

        self.assertEqual('Sally sells sea shells', paper.text)

    def test_pencil_appends_to_text_already_on_paper(self):
        pencil = Pencil()
        paper = Paper('Sally sells sea shells')

        pencil.write(' down by the sea shore', paper)

        self.assertEqual('Sally sells sea shells down by the sea shore', paper.text)


if __name__ == '__main__':
    unittest.main()
