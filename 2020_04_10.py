# -*- coding: utf-8 -*-
"""2020-04-10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eW3DxT3dNK2tCKV97gORhSfegSdCnU5r
"""

last_id_digit = input('請輸入身分證字號的尾數:') #隨堂作業
last_id_digit = int(last_id_digit)
remainder = last_id_digit % 2
if remainder == 0:
    ans = "偶數"
else:
    ans = "奇數"
print("身分證字號尾數除以2的餘數為:{}，因此為{}".format(remainder, ans))

