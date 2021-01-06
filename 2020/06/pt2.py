# Find this puzzle at:
# https://adventofcode.com/2020/day/6

with open('input.txt', 'r') as file:
    puzzle_input = [i for i in file.read().split('\n\n')]
answered = 0
for group in puzzle_input:
    ques_answered = []
    valid_answers = set()
    # Record all answered questions
    for question in group.replace('\n', ''):
        ques_answered.append(question)
    # Add answer only if answered by all members
    for i in ques_answered:
        if ques_answered.count(i) == len(list(group.split('\n'))):
            valid_answers.add(i)
    answered += len(valid_answers)
print(answered)
