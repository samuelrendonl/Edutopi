import unittest
from decimal import Decimal

from app.learning_content import ACTIVITIES, activity_for_grade, public_activity


class LearningContentTests(unittest.TestCase):
    def test_catalog_has_three_lessons_and_two_games(self):
        self.assertEqual(len(ACTIVITIES), 7)
        self.assertEqual(sum(item["kind"] == "Aprendizaje" for item in ACTIVITIES), 5)
        self.assertEqual(sum(item["kind"] == "Juego" for item in ACTIVITIES), 2)

    def test_each_grade_gets_ten_math_questions_with_valid_answers(self):
        for grade in range(1, 6):
            with self.subTest(grade=grade):
                item = next(item for item in ACTIVITIES if item["key"] == "math-sums")
                questions = activity_for_grade(item, grade)["questions"]
                self.assertEqual(len(questions), 10)
                for question in questions:
                    self.assertEqual(len(question["options"]), 3)
                    self.assertIn(question["answer"], range(3))
                    first, operator, second = question["prompt"].split()[:3]
                    left = Decimal(first.replace(",", "."))
                    right = Decimal(second.replace(",", "."))
                    expected = {
                        "+": left + right,
                        "−": left - right,
                        "×": left * right,
                        "÷": left / right,
                    }[operator]
                    marked = Decimal(question["options"][question["answer"]].replace(",", "."))
                    self.assertEqual(marked, expected)

    def test_public_catalog_does_not_send_answer_keys(self):
        for grade in range(1, 6):
            with self.subTest(grade=grade):
                for item in ACTIVITIES:
                    public = public_activity(item, grade)
                    self.assertEqual(len(public["questions"]), 10)
                    self.assertTrue(all("answer" not in question for question in public["questions"]))

    def test_content_adapts_to_grade(self):
        math = next(item for item in ACTIVITIES if item["key"] == "math-sums")
        early_math = activity_for_grade(math, 1)["questions"][0]["prompt"]
        advanced_math = activity_for_grade(math, 5)["questions"][0]["prompt"]
        self.assertNotEqual(early_math, advanced_math)

        words = next(item for item in ACTIVITIES if item["key"] == "words-syllables")
        advanced_words = activity_for_grade(words, 5)["questions"][0]["prompt"]
        self.assertIn("extraordinario", advanced_words)

        story = next(item for item in ACTIVITIES if item["key"] == "reading-story")
        self.assertNotEqual(public_activity(story, 1)["passage"], public_activity(story, 5)["passage"])


if __name__ == "__main__":
    unittest.main()
