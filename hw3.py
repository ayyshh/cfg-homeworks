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
