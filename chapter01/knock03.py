

def count_characters(sentence):
  word = sentence.replace(',', '').replace('.', '').split()
  count_list = list()
  for characters in word:
    count_list.append(len(characters))
  return count_list

if __name__ == '__main__':
  
  sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
  print(count_characters(sentence))
