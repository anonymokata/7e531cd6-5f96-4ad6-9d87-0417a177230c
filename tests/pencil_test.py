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
        self.assertEqual(20, self.pencil.durability)

    def test_pencil_created_with_negative_durability_has_zero_durability(self):
        pencil = Pencil(durability=-1)

        self.assertEqual(0, pencil.durability)

    def test_writing_lower_case_letters_decreases_durability_by_one(self):
        self.pencil.write('a', Paper())

        self.assertEqual(19, self.pencil.durability)

    def test_writing_multiple_lower_case_letters_decreases_durability_for_each_letter(self):
        self.pencil.write('aaa', Paper())

        self.assertEqual(17, self.pencil.durability)

    def test_writing_upper_case_letters_decreases_durability_by_two(self):
        self.pencil.write('A', Paper())

        self.assertEqual(18, self.pencil.durability)

    def test_writing_multiple_upper_case_letters_decreases_durability_by_two_for_each_letter(self):
        self.pencil.write('AAA', Paper())

        self.assertEqual(14, self.pencil.durability)

    def test_text_that_requires_one_more_durability_than_available_uses_a_space_for_remaining_letter(self):
        pencil = Pencil(durability=5)
        paper = Paper()

        pencil.write('Aasdf', paper)

        self.assertEqual('Aasd ', paper.text)

    def test_writing_spaces_does_not_affect_durability(self):
        self.pencil.write('   ', Paper())

        self.assertEqual(20, self.pencil.durability)

    def test_writing_new_lines_does_not_affect_durability(self):
        self.pencil.write('\n', Paper())

        self.assertEqual(20, self.pencil.durability)

    def test_text_that_requires_multiple_more_durability_than_available_uses_spaces_for_remaining_letters(self):
        paper = Paper()

        self.pencil.write('THIS IS A REALLY HIGH COST PHRASE', paper)

        self.assertEqual('THIS IS A REA                    ', paper.text)

    def test_sharpening_a_pencil_restores_its_original_durability(self):
        self.pencil.write('AAAAAA', Paper())
        self.pencil.sharpen()

        self.assertEqual(20, self.pencil.durability)

    def test_sharpening_a_pencil_with_custom_initial_durability_restores_pencil_to_initial_durability(self):
        pencil = Pencil(durability=54)
        pencil.write('AAA', Paper())

        pencil.sharpen()

        self.assertEqual(54, pencil.durability)

    def test_pencil_length_defaults_to_ten(self):
        self.assertEqual(10, self.pencil.length)

    def test_sharpening_a_pencil_reduces_the_length_by_one(self):
        self.pencil.sharpen()

        self.assertEqual(9, self.pencil.length)

    def test_sharpening_a_short_pencil_does_not_change_durability(self):
        pencil = Pencil(length=0, durability=10)
        pencil.write('AAAA', Paper())

        pencil.sharpen()

        self.assertEqual(2, pencil.durability)

    def test_sharpening_a_pencil_with_negative_length_does_not_change_durability(self):
        pencil = Pencil(length=-1, durability=10)
        pencil.write('A', Paper())

        pencil.sharpen()

        self.assertEqual(8, pencil.durability)

    def test_erasing_text_from_paper_replaces_the_text_with_spaces(self):
        paper = Paper('This is some text')

        self.pencil.erase('text', paper)

        self.assertEqual('This is some     ', paper.text)


if __name__ == '__main__':
    unittest.main()
