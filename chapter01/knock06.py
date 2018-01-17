from knock05 import n_gram 
'''
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''


if __name__ == '__main__':
  s1 = "paraparaparadise"
  s2 = "paragraph"
  X = set(n_gram(s1, 2))
  Y = set(n_gram(s2, 2))
  print(X.union(Y), X.intersection(Y), X.difference(Y), Y.difference(X))

  if 'se' in X.intersection(Y):
    print('Yes')
  else:
    print('No')
