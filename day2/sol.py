with open('input.txt') as f:
    lines = f.readlines()

"""
A - Rock, B - Paper, C - Scissors
X - Rock (1), Y - Paper (2), Z - Scissors (3)

"""
score_lut = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

total_score = 0
for line in lines:
    line = line.strip()
    total_score += score_lut[line]

print("Problem 1: Total Score:", total_score)

# Part 2
points_vals = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 0,
    "Y": 3,
    "Z": 6
}

sum = 0
for line in lines:
    parsed = line.split()
    # parsed[0] - Opponent pick
    # X - lose, Y - same, Z - win
    # losing is 2 more, winning is one more indexwise
    # ord() and chr()
    # A - 65
    sum += points_vals[parsed[1]]
    if parsed[1] == "X":
        sum += points_vals[chr(((2+ord(parsed[0])) % 65) % 3 + 65)]
    elif parsed[1] == "Y":
        sum += points_vals[parsed[0]]
    else:
        sum += points_vals[chr(((1+ord(parsed[0])) % 65) % 3 + 65)]

print("Problem 2: Total Score:", sum)