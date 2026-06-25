# questions to ask and to answer
dict_questions = {"What is capital of India?" : "new delhi", 
"In which state Mumbai is located?": "maharashtra", 
"What is data type of 5?" : "int",
"Which computer language is used in AI/ML?" : "python",
"Who is the founder of python language?" : "guido von rossum",
"Which country has the highest population?" : "india",
"Currently, who is the richest man in the world?" : "elon musk",
"Who is the founder of C language?" : "dennis ritchie",
"What is best time to sleep?" : "night",
"Who is the CEO of chatGPT?" : "sam altman",
"What is the minimum age in India to be eligible for voting?" : "18", 
"What type of language is python in HLL/LLL?" : "HLL"
}

import sys
import random
import statistics
def start_quiz(quiz : dict):
    introduce()
    st = input('').lower()
    if st == "start":
        quests = list(quiz.keys())[0:7]
        random.shuffle(quests)
        
        grade_list = []
        ask_question(grade_list, quests, quiz)
        print("\u2103 Your Random Reward! : ",random.randint(5,10))

        report(grade_list)
    else:
        print("Restart Please!")

def introduce():
    if len(sys.argv) > 1:
        print("Hello,",sys.argv[1],"!")
    else:
        print("Guest")
    print("Welcome to the quiz.")
    print("""
    Before we start the quiz let me remind you of the quiz rules:
    • First, the spelling of the words should be correct and there should be only one space between words.
    • Each question wil be of 5 marks, and in result you will recieve your average score in 5.
    • And you will also get to know about the number of correct answers and incorrect answers typed by you.

    Type start if you're ready -
    """)

def ask_question(mark_list : list, q : list, quiz : dict):
    for i,quest in enumerate(q):
        ans = ""
        if i <= 4:
           print(f"{i+1}. {quest}")
        elif 5 <= i <= 6:
            print(f"Bonus question {i-4}: ",quest)
        ans = input("Answer: ")
        if ans.lower() == quiz[quest]:
            mark_list.append(5)
        else:
            mark_list.append(0)
        
def report(grades : list):
    print(f"""
    =====================================================================
                            QUIZ RESULTS
    =====================================================================
          \u2022 The average marks received: {round(statistics.mean(grades), 2)}/5
          \u2022 No of correct answers: {grades.count(5)}
          \u2022 No of incorrect or no answers: {grades.count(0)}
    =====================================================================
    """)

start_quiz(dict_questions)