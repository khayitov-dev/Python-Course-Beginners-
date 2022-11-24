### Building a Multiple Choice Quiz

from questions import Question


question_prompts = [
    "What Color are apples\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What Color are Bananas\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What Color are strawberries\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score  += 1 
    print("Siz jami " + str(score) + "/" + str(len(questions)) + " javob berdingiz.")

run_test(questions)