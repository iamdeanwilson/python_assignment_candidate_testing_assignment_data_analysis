# TODO 2: modify your quiz app to ask 5 questions

# TODO 1.2a: Assign question, correct_answer, and candidate_answer
# question = "Who was the first American woman in space? "
# correct_answer = "Sally Ride"
# candidate_answer = ""
questions = ["Who was the first American woman in space? ", "True or false: 5 kilometer == 5000 meters? ", "(5 + 3)/2 * 10 = ? ", "Given the list [8, 'Orbit', 'Trajectory', 45], what entry is at index 2? ", "What is the minimum crew size for the ISS? "]
correct_answers = ["Sally Ride", "true", "40", "Trajectory", "3"]
candidate_answers = []


def ask_for_name():
  # TODO 1.1: Ask for candidate's name
  candidate_name = input("What is your name? ")
  return candidate_name

def ask_question():
  # TODO 1.2b: Ask candidate the question and assign the response as candidate_answer
  for index in range(len(questions)):
    candidate_answers.append(input(f"\n{questions[index]}"))
  return candidate_answers

def grade_quiz(candidate_answers, candidate_name):
  correct_answers_total = 0
  print(f"\nCandidate Name: {candidate_name}\n")
  # TODO 1.2c: Let the candidate know if they have answered the question correctly or incorrectly 
  for index in range(len(candidate_answers)):
    print(f"{index +1}) {questions[index]} \nYour Answer: {candidate_answers[index]} \nCorrect Answer: {correct_answers[index]}\n")
    if candidate_answers[index].lower() == correct_answers[index].lower():
      correct_answers_total += 1

  grade = ((correct_answers_total / (len(questions))) * 100)

  print(f">>> Overall Grade: {grade}% ({correct_answers_total} of {len(questions)} responses correct) <<<")

  if grade >= 80:
    print(">>> Status: PASSED <<<")
  else:
    print(">>> Status: FAILED <<<")

  return grade


def run_program():
  candidate_name = ask_for_name()
  # TODO 1.1b: Ask for candidate's name and greet them by their name
  print(f"Hello, {candidate_name}")
  ask_question()
  grade_quiz(candidate_answers, candidate_name)
