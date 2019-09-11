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

#分音符の音価を求める式たち(符尾・連桁の数を求めるために必要)
maxima_time = int(whole_note_time) *8 #指定BPMでのマキシマの音価(ms)
longa_time = int(whole_note_time) *4 #指定BPMでのロンガの音価(ms)
double_whole_note_time = int(whole_note_time) *2 #指定BPMでの倍全音符の音価(ms)
half_note_time = int(whole_note_time) / 2 #指定BPMでの2分音符の音価(ms)
quarter_note_time = int(whole_note_time) / 4 #指定BPMでの4分音符の音価(ms)
eighth_note_time = int(whole_note_time) / 8 #指定BPMでの8分音符の音価(ms)
sixteenth_note_time = int(whole_note_time) / 16 #指定BPMでの16分音符の音価(ms)
thirty_second_note_time = int(whole_note_time) / 32 #指定BPMでの32分音符の音価(ms)
sixty_fourth_note_time = int(whole_note_time) / 64 #指定BPMでの64分音符の音価(ms)
hundred_twenty_eighth_note_time = int(whole_note_time) / 128 #指定BPMでの128分音符の音価(ms)
two_hundred_fifty_sixth_note_time = int(whole_note_time) / 256 #指定BPMでの256分音符の音価(ms)
five_hundred_twelfth_note_time = int(whole_note_time) / 512 #指定BPMでの512分音符の音価(ms)
thousand_twenty_fourth_note_time = int(whole_note_time) / 1024 #指定BPMでの1024分音符の音価(ms)

#n分音符の音価≒単純音符部分の音価(ms)を求める式 [全音符の音価÷n]
dieresis_note_time = float(whole_note_time) / int(note_type)

#符点部分の音価(ms)を求める式...[n分音符の音価×((2^d)-1)/(2^d)]
dot_time = float(dieresis_note_time) * ((2 ** (int(dotted_note_type)) - 1) / (2 ** int(dotted_note_type))) 

#★音価(ms)を求める式★...[(n分音符の音価＋符点部分の音価)÷連符(t)]
note_time = (float(dieresis_note_time) + float(dot_time)) / float(tuplet_type)

#符点部分を除いた音価(ms)を求める式
note_time_without_dot = float(note_time) - float(dot_time)

#"分音符"の種類を求める式
dieresis_note = float(whole_note_time)/float(note_time)

#log2(X)の対数関数に分音符の音価を分音符で割ったものを代入したものの整数部分(小数部分は切り捨て)
log_number = math.trunc(math.log2(float(dieresis_note)))

#連符を考える時、符尾・連桁の数とリンクした分音符の"数字"を求める式に必要
ratio_number = 2 ** int(log_number)

#連符の比の分音符の個数
ratio = (int(dieresis_note_time)+int(dot_time))/(int(whole_note_time)/int(ratio_number)) 

#符尾・連桁の数を求める
flag_count = int(log_number) - 2

flag_number = 2 ** int(log_number)

flag_number_minusone = 2 ** int(log_number-1)

#符点音符の連符を符点音符のみ表記に変換
dotted_note = int(note_type)*int(tuplet_type)*(1^(int(dotted_note_type)-1))

#-----------------以下出力のプログラム-----------------

print("------------------------------------------------------------------------------------------")

#音価の表示--------------------------------------------

#全音符の場合の符点音符
if int(note_type) == 1 and int(tuplet_type) == 1 and int(dotted_note_type) == 0:
    print("BPMが"+ str(input_bpm) + "のとき「全音符」の音価は" + str(note_time) + "msです。\n")

elif int(note_type) == 1 and int(tuplet_type) == 1 and int(dotted_note_type) == 1:
    print("BPMが"+ str(input_bpm) + "のとき「符点全音符」の音価は" + str(note_time) + "msです。\n")

elif int(note_type) == 1 and int(tuplet_type) == 1 and int(dotted_note_type) == 2:
    print("BPMが"+ str(input_bpm) + "のとき「複符点全音符」の音価は" + str(note_time) + "msです。\n")

elif int(note_type) == 1 and int(tuplet_type) == 1 and int(dotted_note_type) >= 3:
    print("BPMが"+ str(input_bpm) + "のとき「"+ str(dotted_note_type) + "重符点全音符」の音価は" + str(note_time) + "msです。\n")
#全音符意外の場合の符点音符
elif int(note_type) >= 2 and int(tuplet_type) == 1 and int(dotted_note_type) == 0:
    print("BPMが"+ str(input_bpm) +"のとき「" + str(note_type) + "分音符」の音価は" + str(note_time) + "msです。\n")

elif int(note_type) >= 2 and int(tuplet_type) == 1 and int(dotted_note_type) == 1:
    print("BPMが"+ str(input_bpm) + "のとき「符点"+ str(note_type) + "音符」の音価は" + str(note_time) + "msです。\n")

elif int(note_type) >= 2 and int(tuplet_type) == 1 and int(dotted_note_type) == 2:
    print("BPMが"+ str(input_bpm) + "のとき「複符点"+ str(note_type) + "音符」の音価は"  + str(note_time) + "msです。\n")

elif int(note_type) >= 2 and int(tuplet_type) == 1 and int(dotted_note_type) >= 3:
    print("BPMが"+ str(input_bpm) +"のとき「" + str(dotted_note_type) + "重符点" + str(note_type) + "音符」の音価は" + str(note_time) + "msです。\n")
#連符
elif int(note_type) == 1 and int(tuplet_type) >=2 and int(dotted_note_type) == 0:
    print( "BPMが" + str(input_bpm) + "のとき「全音符の" + str(tuplet_type) + "連符」の音価は" + str(note_time) + "msです。\n" )

elif int(note_type) >= 2 and int(tuplet_type) >=2 and int(dotted_note_type) == 0:
    print( "BPMが" + str(input_bpm) + "のとき「" + str(note_type) + "分音符の" + str(tuplet_type) + "連符」の音価は" + str(note_time) + "msです。\n" )

elif int(note_type) >= 2 and int(tuplet_type) >=2 and int(dotted_note_type) ==1:
    print( "BPMが" + str(input_bpm) + "のとき「符点" + str(note_type) + "分音符の" + str(tuplet_type) + "連符」の音価は" + str(note_time) + "msです。\n" )

elif int(note_type) >= 2 and int(tuplet_type) >=2 and int(dotted_note_type) ==2:
    print( "BPMが" + str(input_bpm) + "のとき「複符点" + str(note_type) + "分音符の" + str(tuplet_type) + "連符」の音価は" + str(note_time) + "msです。\n" )

elif int(note_type) >= 2 and int(tuplet_type) >=2 and int(dotted_note_type) >=3:
    print( "BPMが" + str(input_bpm) +"のとき「" + str(dotted_note_type) + "重符点" + str(note_type) + "分音符の" + str(tuplet_type) + "連符」の音価は" + str(note_time) + "msです。\n" )
#全部乗せ表記
elif int(note_type) == 1 and int(tuplet_type) >=2 and int(dotted_note_type) == 1:
    print( "BPMが" + str(input_bpm) + "のとき「符点全音符の" + str(tuplet_type) + "連符」の音価は" + str(note_time) + "msです。\n" )

elif int(note_type) == 1 and int(tuplet_type) >=2 and int(dotted_note_type) == 2:
    print( "BPMが" + str(input_bpm) + "のとき「複符点全音符の" + str(tuplet_type) + "連符」の音価は" + str(note_time) + "msです。\n" )

elif int(note_type) == 1 and int(tuplet_type) >=2 and int(dotted_note_type) >=3:
    print( "BPMが" + str(input_bpm) + "のとき「" + str(dotted_note_type) + "重符点全音符の" + str(tuplet_type) + "連符」の音価は" + str(note_time) + "msです。\n" )

elif int(note_type) >= 2 and int(tuplet_type) >=2 and int(dotted_note_type) >=3:
    print( "BPMが" + str(input_bpm) + "のとき「" + str(dotted_note_type) + "重符点" + str(note_type) + "分音符の" + str(tuplet_type) + "連符」の音価は" + str(note_time) + "msです。\n" )

else:
    print("音符の種類が分かりません。音価は" + str(note_time) + "msです。\n")
#/音価の表示----------------------------------------

#音価についてのコメント
if int(note_time) < 10 :
    print( "この音符の音価は10ms以下です。人間には知覚が難しいと思われます。\n" )

elif int(note_time) == 1000:
    print( "この音符の音価は1000msです。秒針の速さと同じリズムですね。\n" )
else:
    print()

#連符の比の表記
if int(note_type) >= 1 and int(tuplet_type) >=3:
    print("この音価は、" + str(ratio_number) + "分音符が"+ str(ratio)+"個分の音価を"+str(tuplet_type)+"個に分割しています。\nよって、この" +str(tuplet_type)+ "連符と"+ str(ratio_number) + "分音符との比は「"+ str(tuplet_type)+"：" +str(ratio) +"」で表すことができます。\n" )

elif int(note_type) >= 1 and int(tuplet_type) ==2:
    print("この音価は、" + str(float(ratio_number)*2) + "分音符が"+ str(float(ratio)*2)+"個分の音価を"+str(tuplet_type)+"個に分割しています。\nよってこの" +str(tuplet_type)+ "連符と"+ str(float(ratio_number)*2) + "分音符との比は「"+ str(tuplet_type)+"：" +str(float(ratio)*2) +"」で表すことができます。\n" )

else:
    print()

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
    print()

#「符点音符の2の冪連符」を「符点音符」のみ表記にした場合
if int(note_type) & (int(note_type) - 1) == 0 and int(tuplet_type) & (int(tuplet_type) - 1) == 0 and int(dotted_note_type) == 1:
    print("これは、このBPMでの「符点"+ str(dotted_note) + "分音符」と同じ音価です。\n")

else:
    print()

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
    print()

#メトリックモジュレーションの提案

print("------------------------------------------------------------------------------------------")
print("メトリックモジュレーションの提案")
print( "この音符はBPM" + str(int(one_minutes)/(float(note_time)*12/4)) + "の「1拍3連」と同じ音価を持ちます。" )
print( "この音符はBPM" + str(int(one_minutes)/(float(note_time)*16/4)) + "の「16分音符」と同じ音価を持ちます。" )
print( "この音符はBPM" + str(int(one_minutes)/(float(note_time)*20/4)) + "の「1拍5連」と同じ音価を持ちます。" )

