order = 0
goodness = 0

question1 = {
    'question': 'You are on a walk with your dog, and they take a crap.',
    'answers': {
        'a': ["Leave it.", 0, 0],
        'b': ["Pick it up, throw it away.", 2, 2],
        'c': ["Throw it at someone.", -1, -1],
        'd': ['Eat it.', -2, 0]
    }
}

question2 = {
    'question': "You have hit someone's car with yours, do you...",
    'answers': {
        'a': ["Park somewhere else.", -1, -1],
        'b': ["Leave a note.", 2, 2],
        'c': ["Leave a blank note.", -1, -1],
        'd': ['Hit it again for good measure.', -2, -2]
    }
}

question3 = {
    'question': "Someone calls you stupid. What do you do?",
    'answers': {
        'a': ['Explain calmly why they are mistaken.', 2, 2],
        'b': ['Punch them right in the face.', -1, -2],
        'c': ['Report them to the authorities.', 1, 0],
        'd': ['Let them know that they are way more stupid.', 0, -1]
    }
}

question4 = {
    'question': "You have tasted someone's food and it's awful. They ask your opinion. Uh oh. What do you do?",
    'answers': {
        'a': ['This food is so awful, and you should be ashamed,', 1, -2],
        'b': ['This food is okay. You could improve like this.', 1, 2],
        'c': ['This food is amazing! I want more.', -1, 2],
        'd': ['Here, you try it. *throw the food at them*', -2, -2]
    }
}

def output_string(question):
    rubric = question['answers']
    result = "\n"
    for key in rubric:
        result += f"{key} {rubric[key][0]}\n"
    return result

def parse_question(question):
    rubric = question['answers']
    prompt = question['question']
    answer = input(prompt + output_string(question)).lower()
    while answer not in rubric.keys():
        print("Please choose of the answer letters")
        answer = input(prompt + output_string(question)).lower()
    global order
    global goodness
    order += rubric[answer][1]
    goodness += rubric[answer][2]

def parse_alignment():
    result = ""
    global order
    global goodness
    if -1 <= order and order <= 1:
        result += 'Neutral '
    elif order < -1:
        result += 'Chaotic '
    elif order > 1:
        result += 'Lawful '

    if -1 <= goodness and goodness <= 1:
        result += 'Neutral'
    elif goodness < -1:
        result += 'Evil'
    elif goodness > 1:
        result += 'Good'

    if result == "Neutral Neutral":
        result = "True Neutral"

    return result

if __name__ == "__main__":
    parse_question(question1)
    parse_question(question2)
    parse_question(question3)
    parse_question(question4)
    print(f"Your alignment is {parse_alignment()}")
    print(order, goodness)

