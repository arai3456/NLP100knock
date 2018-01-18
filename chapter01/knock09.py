'''
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
'''

import random
def shuffle(s):
  words = s.strip().split()
  sentence_list = list()
  for word in words:
    if len(words) > 4:
      word_list = list(word)
      m_list = list(word[1:-1])
      random.shuffle(m_list)
      word_list[1:-1] = m_list
      word_str = ''.join(word_list)
      sentence_list.append(word_str)
    else:
      word_list = list(words)
      word_str = ''.join(word_list)
      sentence_list.append(word_str)
  return sentence_list


#      random.shuffle(word)


if __name__ == '__main__':
  s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

  print(' '.join(shuffle(s)))

