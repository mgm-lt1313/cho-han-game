# -*- coding: utf-8 -*-
"""kimatsu.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15JVwmT-yvCA9VH1OwRl0nXSfNs9KdVbE
"""

import random

print('二つのサイコロの出目の和が丁（偶数）か半（奇数）かを当てるゲームです')
money = int(input('所持金はいくらですか？：'))
kachi = 0
make = 0

def tyouhan():
    global money
    global kachi
    global make
    kakekin = int(input('賭ける金額を入力してください：'))
    n = input('丁か半か：')

    daisu1 = random.randint(1,6)
    daisu2 = random.randint(1,6)
    result = daisu1 + daisu2

    if ((result) % 2 == 0 and n == '丁') or ((result) % 2 == 1 and n == '半'):
        money += kakekin
        kachi += 1
        print('サイコロの出目の和：{}'.format(result))
        print('おめでとうございます！正解です')
        print('現在の所持金：{}'.format(money))
        print('')
    else:
        money -= kakekin
        make += 1
        print('サイコロの出目の和：{}'.format(result))
        print('残念！はずれです')
        print('現在の所持金：{}'.format(money))
        print('')



while True:
    x = int(input('挑戦しますか？（はい：0、いいえ：1）：'))
    if x == 0:
        print('')
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊')
        print('＊丁半ゲームを開始します＊')
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊')
        print('')
        tyouhan()

    if money <= 0:
        print('')
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊')
        print('＊丁半ゲームを終了します＊')
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊')
        print('')
        print('所持金がなくなりました')
        print('勝敗は{}勝{}敗です' .format(kachi,make))
        break

    if x == 1:
        print('')
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊')
        print('＊丁半ゲームを終了します＊')
        print('＊＊＊＊＊＊＊＊＊＊＊＊＊')
        print('')
        print('勝敗は{}勝{}敗です' .format(kachi,make))
        print('所持金は{}円になりました'.format(money))
        break