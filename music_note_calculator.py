import math

#-----------------以下入力のプログラム-----------------

input_bpm = input('BPMを入力してください。→') #BPMの入力
note_type = input("分音符の種類を(できれば2の累乗の数で)入力してください。(全音符の場合は1を入力してください。)→") #「n」分音符の入力
dotted_note_type = input("符点音符を入力したい場合は、符点の数を入力してください。(無しの場合は0を入力してください。)→")  #符点の数「d」の入力
tuplet_type = input("連符を入力したい場合は、連符の種類を入力してください。(無しの場合は1を入力してください。)→") #連符による分割数「t」の入力

#-----------------以下計算処理のプログラム-----------------

one_minutes = 60000 #1分の秒数(ms)
common_beat_time = int(one_minutes) / int(input_bpm) #指定BPMでの基本的な「1拍」の音価であり,4分音符の音価(ms)
whole_note_time = float(common_beat_time) * 4 #指定BPMでの全音符の音価(ms)
common_beat_time = int(one_minutes) / int(input_bpm) #指定BPMでの基本的な1拍の音価であり,4分音符の音価(ms)

#n分音符の音価≒単純音符部分の音価(ms)を求める式 [全音符の音価÷n]
dieresis_note_time = float(whole_note_time) / int(note_type)

#符点部分の音価(ms)を求める式...[n分音符の音価×((2^d)-1)/(2^d)]
dot_time = float(dieresis_note_time) * ((2 ** (int(dotted_note_type)) - 1) / (2 ** int(dotted_note_type))) 

#★この音符の音価(ms)を求める式★...[(n分音符の音価＋符点部分の音価)÷連符(t)]
note_time = (float(dieresis_note_time) + float(dot_time)) / float(tuplet_type)

#"x分音符"の種類を求める式
dieresis_note = float(whole_note_time)/float(note_time)

#log2(X)の対数関数に"x分音符"の値を代入したものの整数部分(このあと小数部分は切り捨てる)
log_number = math.trunc(math.log2(float(dieresis_note)))

#連符の比の調整に使う...[2^{連符の分割数+(符点の数-連符の分割数)]
Adjustment_number = 2 ** ((int(tuplet_type) + (int(dotted_note_type) - int(tuplet_type))))

#連符を考える時、符尾・連桁の数とリンクした"連符で分割する前の分音符の数字"を求める式
ratio_number = (2 ** int(log_number))*(int(Adjustment_number))

#連符の比の"連符で分割する前の分音符の個数"を求める式
ratio = ((int(dieresis_note_time)+int(dot_time))/(int(whole_note_time)/(int(ratio_number)/(int(Adjustment_number)))))*(int(Adjustment_number))

#符尾・連桁の数とその根拠となる「(2の累乗)分音符」の種類
flag_count = int(log_number) - 2
flag_number = 2 ** int(log_number)
flag_number_minusone = 2 ** int(log_number-1)

#符点音符の連符を符点音符のみ表記に変換する式[n×t×{1^(d-1)}]
dotted_note = int(note_type)*int(tuplet_type)*(1^(int(dotted_note_type)-1))

#-----------------以下出力のプログラム-----------------

print("------------------------------------------------------------------------------------------")

#音価の表示--------------------------------------------

import sys

sys.stdout.write("BPMが"+ str(input_bpm) + "のとき「")

if int(dotted_note_type) == 1:
    sys.stdout.write("符点")
elif int(dotted_note_type) == 2:
    sys.stdout.write("複符点")
elif int(dotted_note_type) >= 3:
    sys.stdout.write(str(dotted_note_type) + "重符点")
else:
    sys.stdout.write("")

if int(note_type) == 1:
    sys.stdout.write("全音符")
elif int(note_type) >= 2:
    sys.stdout.write(str(note_type)  + "分音符")
else:
    sys.stdout.write("")

if int(note_type) >= 2:
    sys.stdout.write("の" + str(note_type)  + "連符")
else:
    sys.stdout.write("")

sys.stdout.write("」の音価は" + str(note_time) + "msです。\n")

#/音価の表示----------------------------------------

#音価についてのコメント
if int(note_time) <= 10:
    print( "この音符の音価は10ms以下です。人間には知覚が難しいと思われます。\n" )
elif int(note_time) == 1000:
    print( "この音符の音価は1000msです。秒針の速さと同じリズムですね。\n" )
else:
    print("")

#連符の比の表記
if int(note_type) >= 1 and int(tuplet_type) >=2:
    print("この音価は、" + str(ratio_number) + "分音符が"+ str(ratio)+"個分の音価を"+str(tuplet_type)+"個に分割しています。\nよって、この" +str(tuplet_type)+ "連符と"+ str(ratio_number) + "分音符との比は「"+ str(tuplet_type)+"：" +str(ratio) +"」で表すことができます。\n" )
else:
    sys.stdout.write("")

 #符尾・連桁の数を表示する
if int(flag_count) < 1: #指定BPMでの8分音符より、「符点を含めない音価」が長い場合
    print("この音符の音価は、このBPMの8分音符より長いため、符尾・連桁の数は\"0本\"で記述されます。\n")
elif int(flag_count) >= 1:
    print("この音符の音価は、このBPMの" + str(flag_number) + "分音符より長く、" + str(flag_number_minusone) + "分音符より短いため、符尾・連桁の数は" + str(flag_count) + "で記述されます。\n")
else:
    print("符尾・連桁の数が分かりません。\n")

#分音符だけで表した時の表記
if int(note_type) >=1 and int(tuplet_type) >=1 and int(dotted_note_type) >=0:
    print( "「分音符」だけを使った表記を考えた場合、これは「"+  str(dieresis_note) + "分音符」であるとも言えます。\n" )
else:
    sys.stdout.write("")

#「符点音符の2の冪連符」を「符点音符」のみ表記にした場合
if int(note_type) & (int(note_type) - 1) == 0 and int(tuplet_type) & (int(tuplet_type) - 1) == 0 and int(dotted_note_type) == 1:
    print("これは、このBPMでの「符点"+ str(dotted_note) + "分音符」と同じ音価です。\n")
else:
    sys.stdout.write("")

#「〇拍〇連」表記の有無
if int(note_type) == 1 and int(tuplet_type) >=3 and int(dotted_note_type) == 0:
    print( "また、この場合「4拍" + str(tuplet_type) + "連」とも言います。\n" )
elif int(note_type) == 2 and int(tuplet_type) >=3 and int(dotted_note_type) == 0:
    print( "また、この場合「2拍" + str(tuplet_type) + "連」とも言います。\n" )
elif int(note_type) == 4 and int(tuplet_type) >=3 and int(dotted_note_type) == 0:
    print( "また、この場合「1拍" + str(tuplet_type) + "連」とも言います。\n" )
elif int(note_type) == 8 and int(tuplet_type) >=3 and int(dotted_note_type) == 0:
    print( "また、この場合「半拍" + str(tuplet_type) + "連」とも言います。\n" )
else:
    sys.stdout.write("")

#・メトリックモジュレーションの提案
print("------------------------------------------------------------------------------------------")
print("・メトリックモジュレーションの提案")
print( "この音符はBPM" + str(int(one_minutes)/(float(note_time)*12/4)) + "の「1拍3連」と同じ音価を持ちます。" )
print( "この音符はBPM" + str(int(one_minutes)/(float(note_time)*16/4)) + "の「16分音符」と同じ音価を持ちます。" )
print( "この音符はBPM" + str(int(one_minutes)/(float(note_time)*20/4)) + "の「1拍5連」と同じ音価を持ちます。" )