# -*- coding: utf-8 -*-


import cv2
import os


def preparation_all_right(element_name, parts_h=1, parts_w=1):
    with open('./' + element_name + '/Bad.dat', 'w', encoding='utf-8') as file: file.write('')
    photos = os.listdir('./Resources/All_right/')
    index = -1
    for i in range(len(photos)):
        pic = cv2.imread('./Resources/All_right/' + photos[i])
        pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        height, width = pic.shape[0], pic.shape[1]
        for row in range(parts_h):
            for column in range(parts_w):
                index += 1
                h0, w0, h, w = row*(height//parts_h), column*(width//parts_w),\
                               (row+1)*(height//parts_h), (column+1)*(width//parts_w)
                pic_part = pic[h0:h, w0:w]
                cv2.imwrite('./' + element_name + '/Bad/' + str(index) + '.jpg', pic_part)
                with open('./' + element_name + '/Bad.dat', 'a', encoding='utf-8') as badfile:
                    badfile.write('./' + element_name + '/Bad/' + str(index) + '.jpg')
                    if not(row == (parts_h - 1) and column == (parts_w - 1) and i == (len(photos) - 1)):
                        badfile.write('\n')


def preparation_missing_element(element_name):
    with open('./' + element_name + '/Good.dat', 'w', encoding='utf-8') as file: file.write('')
    photos = os.listdir('./Resources/Missing_' + element_name + '/')
    index = -1
    for i in range(len(photos)):
        pic = cv2.imread('./Resources/Missing_' + element_name + '/' + photos[i])
        pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        height, width = pic.shape[0], pic.shape[1]
        index += 1
        pic_side = min(height, width)
        if element_name == 'capacitor': pic = pic[0:pic_side, 0:pic_side]
        cv2.imwrite('./' + element_name + '/Good/' + str(index) + '.jpg', pic)
        with open('./' + element_name + '/Good.dat', 'a', encoding='utf-8') as goodfile:
            goodfile.write('Good/' + str(index) + '.jpg 1 0 0 ' + str(pic.shape[1]) + ' ' + str(pic.shape[0]))
            if i != (len(photos) - 1): goodfile.write('\n')


def update_datasets():
    preparation_all_right('capacitor', parts_h=10, parts_w=10)
    preparation_missing_element('capacitor')

    preparation_all_right('connector', parts_h=10, parts_w=10)
    preparation_missing_element('connector')

    preparation_all_right('output', parts_h=10, parts_w=10)
    preparation_missing_element('output')


if __name__ == '__main__':
    update_datasets()
