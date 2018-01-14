import sys
def n_gram(sequence, n):
  n_gram_list = list()
  for i in range(len(sequence)-(int(n)-1)):
    n_gram = sequence[i: i + int(n)]

    n_gram_list.append(n_gram)
  return n_gram_list

if __name__ == '__main__':
  sequence = "I am an NLPer"
  print(sys.argv)
  n = sys.argv[1]
  word = sequence.strip().split()
  print('単語:', n_gram(word, n), '\n', '文字:', n_gram(sequence, n))

