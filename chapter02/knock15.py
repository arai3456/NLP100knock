'''
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち後ろのN行だけを表示せよ．確認にはtailコマンドを用いよ．
'''
import sys

def head(f, n):
  print(''.join(f[-n:]))
    


if __name__ == '__main__':
  f = open('hightemp2.txt').readlines()
  print(sys.argv)
  n = int(sys.argv[1])
  head(f, n)
