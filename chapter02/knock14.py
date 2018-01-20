'''
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
'''
import sys

def head(f, n):
  print(f[:n])
    


if __name__ == '__main__':
  f = open('hightemp2.txt').readlines()
  n = sys.argv[1]
  head(f, n)
