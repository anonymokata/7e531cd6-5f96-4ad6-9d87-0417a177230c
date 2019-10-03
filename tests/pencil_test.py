import unittest

from pencil_durability.paper import Paper
from pencil_durability.pencil import Pencil


class PencilTests(unittest.TestCase):

    def setUp(self):
        self.pencil = Pencil()

    def test_pencil_writes_text_to_paper(self):
        paper = Paper()

        self.pencil.write('Sally sells sea shells', paper)

        self.assertEqual('Sally sells sea shells', paper.text)

    def test_pencil_appends_to_text_already_on_paper(self):
        paper = Paper('Sally sells sea shells')

        self.pencil.write(' down by the sea shore', paper)

        self.assertEqual('Sally sells sea shells down by the sea shore', paper.text)

    def test_pencil_durability_defaults_to_twenty(self):
        pencil = Pencil()
        self.assertEqual(20, pencil.durability)

    def test_writing_lower_case_letters_decreases_durability_by_one(self):
        pencil = Pencil()

        pencil.write('a', Paper())

        self.assertEqual(19, pencil.durability)

if __name__ == '__main__':
    unittest.main()
