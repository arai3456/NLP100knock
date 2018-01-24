'''
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ
'''
def type(f):
  words_list = list()
  for line in f:
    words = line.strip().split('\t')
    words_list.append(words[0])
  word_1 = set(words_list)
  return word_1

if __name__ == '__main__':
  f = open('hightemp2.txt').readlines()
  print(type(f))

