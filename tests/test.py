import unittest

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from candidatetesting import *

class TestCandidateQuiz(unittest.TestCase):

	# PART 1
	# candidate_name tests

   def test_candidate_name(self):
      self.assertIs(type(candidate_name), str)

   # question tests

   def test_question(self):
      self.assertIs(type(question), str)

   def test_question_correct(self):
      self.assertEqual(question, "Who was the first American woman in space? ")

   # correct_answer tests

   def test_correct_answer(self):
      self.assertIs(type(correct_answer), str)

   def test_answer_correct(self):
      self.assertEqual(correct_answer, "Sally Ride")

   # candidate_answer tests

   def test_candidate_answer(self):
      self.assertIs(type(candidate_answer), str)


   # PART 2
   # questions tests

   def test_quiz_contains_5(self):
      self.assertEqual(len(questions), 5)

   def trailing_spaces(self):
      self.assertIn(questions, "Who was the first American woman in space? ")
      self.assertIn(questions, "True or false: 5 kilometer == 5000 meters? ")
      self.assertIn(questions, "(5 + 3)/2 * 10 = ? ")
      self.assertIn(questions, "Given the array [8, 'Orbit', 'Trajectory', 45], what entry is at index 2? ")
      self.assertIn(questions, "What is the minimum crew size for the ISS? ")

   def test_correct_answers_contains_5(self):
      self.assertEqual(len(correct_answers), 5)

   def test_correct_answers_is_correct(self):
      self.assertIn(correct_answers, "Sally Ride")
      self.assertIn(correct_answers, "true")
      self.assertIn(correct_answers, "40")
      self.assertIn(correct_answers, "Trajectory")
      self.assertIn(correct_answers, "3")

   # PART 3
   # gradeQuiz tests

   def test_score_0_for_all_wrong(self):
      candidate_answers = ["foo", "bar", "baz", "lur", "man"]
      self.assertEqual(grade_quiz(candidate_answers), 0)

   def test_score_0_for_all_correct(self):
      candidate_answers = ["Sally Ride", "true", "40", "Trajectory", "3"]
      self.assertEqual(grade_quiz(candidate_answers), 100)

   def test_score_20_1_correct(self):
      candidate_answers = ["Sally Ride", "bar", "baz", "lur", "man"]
      self.assertEqual(grade_quiz(candidate_answers), 20)
   
   def test_score_40_2_correct(self):
      candidate_answers = ["Sally Ride", "bar", "baz", "lur", "3"]
      self.assertEqual(grade_quiz(candidate_answers), 40)

   def test_score_60_3_correct(self):
      candidate_answers = ["Sally Ride", "bar", "40", "lur", "3"]
      self.assertEqual(grade_quiz(candidate_answers), 60)

   def test_score_80_4_correct(self):
      candidate_answers = ["Sally Ride", "bar", "40", "Trajectory", "3"]
      self.assertEqual(grade_quiz(candidate_answers), 80)

   def test_case_insensitivity(self):
      candidate_answers = ["sally ride", "TRUE", "40", "TrAjEcToRy", "3"]
      self.assertEqual(grade_quiz(candidate_answers), 100)

if __name__ == '__main__':
    unittest.main()
