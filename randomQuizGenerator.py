import random, os
from pathlib import Path

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':
'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'West Virginia':'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

def generate_randomized_quiz(quiz_filename: str, answer_filename: str):
    states = list(capitals.keys())
    random.shuffle(states)
    quiz_lines = []
    answer_lines = []
    for i, state in enumerate(states):            
        quiz_lines.append(str(i+1) + ". What is the capital of " + state + "?\n")
        other_states = states[:i] + states[i+1:]
        wrong_states = random.sample(other_states, 3)
        options = []
        for wrong_state in wrong_states:
            options.append(capitals[wrong_state])
        options.append(capitals[state])
        random.shuffle(options)
        correct_index = options.index(capitals[state])
        answer_lines.append(str(i+1) + ". " + chr(ord("A") + correct_index) + "\n")
        for i, option in enumerate(options):
            quiz_lines.append(chr(ord("A") + i) + ": " + option + "\n")
        quiz_lines.append("\n")
    with open(quiz_filename, "w") as quiz_file:
        quiz_file.writelines(quiz_lines)
    with open(answer_filename, "w") as answer_file:
        answer_file.writelines(answer_lines)


def generate_class_quizzes(class_name: str):
    Path(class_name).mkdir(exist_ok=True)
    os.chdir(class_name)
    Path("Quizzes").mkdir(exist_ok=True)
    Path("Answers").mkdir(exist_ok=True)
    for i in range(1, 36):
        quiz_filename = "Quizzes/student_" + str(i) + ".txt"
        answer_filename = "Answers/student_" + str(i) + ".txt"
        generate_randomized_quiz(quiz_filename, answer_filename)

generate_class_quizzes("Class_1")