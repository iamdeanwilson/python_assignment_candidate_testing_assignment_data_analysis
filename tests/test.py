import unittest
import re

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from candidatetesting import *

class TestCandidateQuiz(unittest.TestCase):

	# PART 1

   # question tests

   def test_question(self):
      self.assertIs(type(question), str)

   def test_question_correct(self):
      test = re.search("^(?:W|w)ho was the first (?:A|a)merican woman in space\? ", question)
      self.assertTrue(test)
      # self.assertEqual(question, "Who was the first American woman in space? ")

   # correct_answer tests

   def test_correct_answer(self):
      self.assertIs(type(correct_answer), str)

   def test_answer_correct(self):
      # self.assertEqual(correct_answer, "Sally Ride")
      test = re.search("^(?:S|s)ally.(?:R|r)ide$", correct_answer)
      self.assertTrue(test)

   # candidate_answer tests

   def test_candidate_answer(self):
      self.assertIs(type(candidate_answer), str)

   # PART 2
   # questions tests

   def test_quiz_contains_5(self):
      self.assertEqual(len(questions), 5)

   def test_quiz_contains_question_1(self):
      test = "^(?:W|w)ho was the first (?:A|a)merican woman in space\? "
      question_check = False
      for q in questions:
         check = re.search(test, q)
         if check:
            question_check = True
      
      self.assertTrue(question_check)

   def test_quiz_contains_question_2(self):
      test = "^(?:T|t)rue or false: 5 kilometer == 5000 meters\? "
      question_check = False
      for q in questions:
         check = re.search(test, q)
         if check:
            question_check = True
      
      self.assertTrue(question_check)

   def test_quiz_contains_question_3(self):
      # (5 + 3)/2 * 10 = ? 
      test = "\(5 \+ 3\)/2 \* 10 = \? "
      question_check = False
      for q in questions:
         check = re.search(test, q)
         if check:
            question_check = True
      
      self.assertTrue(question_check)

   def test_quiz_contains_question_4(self):
      test = "^(?:G|g)iven the list \[8, 'Orbit', 'Trajectory', 45\], what entry is at index 2\? "
      question_check = False
      for q in questions:
         check = re.search(test, q)
         if check:
            question_check = True
      
      self.assertTrue(question_check)   

   def test_quiz_contains_question_5(self):
      test = "^(?:W|w)hat is the minimum crew size for the (?:I|i)(?:S|s)(?:S|s)\? "
      question_check = False
      for q in questions:
         check = re.search(test, q)
         if check:
            question_check = True
      
      self.assertTrue(question_check)

   def test_correct_answers_contains_5(self):
      self.assertEqual(len(correct_answers), 5)

   def test_quiz_contains_answer_1(self):
      test = "^(?:S|s)ally.(?:R|r)ide$"
      answer_check = False
      for a in correct_answers:
         check = re.search(test, a)
         if check:
            answer_check = True
      
      self.assertTrue(answer_check)

   def test_quiz_contains_answer_2(self):
      test = "^(?:T|t)rue"
      answer_check = False
      for a in correct_answers:
         check = re.search(test, a)
         if check:
            answer_check = True
      
      self.assertTrue(answer_check)

   def test_quiz_contains_answer_3(self):
      test = "40"
      answer_check = False
      for a in correct_answers:
         check = re.search(test, a)
         if check:
            answer_check = True
      
      self.assertTrue(answer_check)

   def test_quiz_contains_answer_4(self):
      test = "^(?:T|t)rajectory"
      answer_check = False
      for a in correct_answers:
         check = re.search(test, a)
         if check:
            answer_check = True
      
      self.assertTrue(answer_check)

   def test_quiz_contains_answer_5(self):
      test = "3"
      answer_check = False
      for a in correct_answers:
         check = re.search(test, a)
         if check:
            answer_check = True
      
      self.assertTrue(answer_check)

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
