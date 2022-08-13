from collections import Counter

def generate_phrase(char, phrase):
  new_chr = char.lower()
  new_phr = phrase.lower()
  a = Counter(new_chr)
  y = Counter(new_phr)
  if a == y:
    return True
  else:
    return False

phrase = "aabbccc"
char = "cbacba"

generate_phrase(char, phrase)
generate_phrase('cbacba', 'aabbccc')


#HOMEWORK 4

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

def searching_matrix(matrix, target):
    COLUMN = len(matrix[0]) - 1
    ROW = 0

    while ROW < len(matrix) and COLUMN >= 0:
        if matrix[ROW][COLUMN] > target:
            COLUMN -= 1
        elif matrix[ROW][COLUMN] < ROW:
            ROW += 1
        else:
            return [ROW, COLUMN]
    return [-1, -1]
