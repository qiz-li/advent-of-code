# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i for i in file.read().split('\n\n')]
answered = 0
for group in puzzle_input:
    ques_answered = set()
    # Add all questions answered to a set.
    # Duplicates are avoided by using a set.
    for question in group.replace('\n', ''):
        ques_answered.add(question)
    answered += len(ques_answered)
print(answered)
