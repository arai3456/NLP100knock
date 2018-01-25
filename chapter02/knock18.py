'''
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）
'''
#def sort(f):
 #print(*sorted(f, key = lambda line:line.split('\t')[2]),sep='')
 #sort_f = sorted(f, key = lambda line:line.split('\t')[2])
'''
sorted関数はsortする対象を第1引数に入れる、optionでkeyを設定できる。keyにはsortする対象を選ぶ関数を入れる。
lambdaは、lineが引数でそのlineをどうするかを:以下に入れる

'''
 #print(*sort_f, sep = '')
def extract_temp(line):
  return line.strip().split('\t')[2]
if __name__ == '__main__':
  f = open('hightemp2.txt').readlines()
  #sort(f)
  print(*sorted(f, key = extract_temp), sep='')

