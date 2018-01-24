'''
自然数Nをコマンドライン引数などの手段で受け取り，，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマドで実現せよ．


'''
import sys

def split(f, n):
  x,y = divmod(len(f), n)
  x_list = list()
  X_list = list()
  i = 0
  while i < len(f):
    x_list.append(f[i])
    if len(x_list) == x:
      if y != 0:
        x_list.append(f[i+1])
        i += 1
        y -= 1
      X_list.append(x_list)
      x_list = list()
    i += 1
  return X_list


if __name__ == '__main__':
  f = open('hightemp2.txt').readlines()
  print(sys.argv)
  n = int(sys.argv[1])
  for x_list in split(f,n):
    print(''.join(x_list))
