# Write a function that can take a string and return a list of bigrams.

sentence = "Have free hours and love children? Drive kids to school, soccer practice and other activities."

# output = [('have', 'free'),
#  ('free', 'hours'),
#  ('hours', 'and'),
#  ('and', 'love'),
#  ('love', 'children?'),
#  ('children?', 'drive'),
#  ('drive', 'kids'),
#  ('kids', 'to'),
#  ('to', 'school,'),
#  ('school,', 'soccer'),
#  ('soccer', 'practice'),
#  ('practice', 'and'),
#  ('and', 'other'),
#  ('other', 'activities.')]

def create_bigram(sentence):
    words = sentence.lower().split()
    return [(word_1, word_2) for word_1, word_2 in zip(words, words[1:])]

print(create_bigram(sentence))