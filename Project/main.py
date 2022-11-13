# -*- coding: utf-8 -*-


from preparation import *
import cv2
import datetime


# Функция вывода изображения на экран
def view_image(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def processing_image(path):
    if path == '': return

    # Считывание изображения платы
    orig_pic = cv2.imread(path)
    pic = cv2.cvtColor(orig_pic, cv2.COLOR_BGR2RGB)
    height, width = pic.shape[0], pic.shape[1]
    print('Image: h =', height, ' w =', width)

    # Обработка
    pic1 = cv2.cvtColor(pic, cv2.COLOR_RGB2GRAY)

    # Конденсатор
    cascade = cv2.CascadeClassifier('./capacitor/haarcascade/cascade.xml')
    detected_capacitors = cascade.detectMultiScale(pic1, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10))
    print(detected_capacitors)
    print(len(detected_capacitors))
    for rect in detected_capacitors:
        pic = cv2.rectangle(pic, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 0, 255), 5)

    # Разъем
    cascade = cv2.CascadeClassifier('./connector/haarcascade/cascade.xml')
    detected_connectors = cascade.detectMultiScale(pic1, scaleFactor=1.1, minNeighbors=7, minSize=(50, 120))
    print(detected_connectors)
    print(len(detected_connectors))
    for rect in detected_connectors:
        pic = cv2.rectangle(pic, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 255), 5)

    # Выход
    cascade = cv2.CascadeClassifier('./output/haarcascade/cascade.xml')
    detected_outputs = cascade.detectMultiScale(pic1, scaleFactor=1.1, minNeighbors=7, minSize=(40, 260))
    print(detected_outputs)
    print(len(detected_outputs))
    for rect in detected_outputs:
        pic = cv2.rectangle(pic, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 165, 255), 5)

    # Вывод изображения проверенной платы на кран
    view_image(cv2.resize(pic, (width//3, height//3), interpolation=cv2.INTER_AREA), 'Checked image')
    cv2.imwrite('./exported_image.jpg', pic)
    print('Checked image saved in ./exported_image.jpg')
    return detected_capacitors, detected_connectors, detected_outputs, orig_pic


print('Enter a picture path:')
(detected_capacitors, detected_connectors, detected_outputs, pic) = processing_image(input())

print('Update datasets? (Y/N)')
if input() == 'Y':
    if len(detected_capacitors) == 0 and len(detected_connectors) == 0 and len(detected_outputs) == 0:
        cv2.imwrite('./Resources/All_right/' +
                    str(datetime.datetime.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '') +
                    '.jpg', pic)
    if len(detected_capacitors) > 0:
        for obj in detected_capacitors:
            h0, w0, h, w = obj[0], obj[1], obj[0] + obj[2], obj[1] + obj[3]
            new_pic = pic[h0:h, w0:w]
            cv2.imwrite('./Resources/Missing_capacitor/' +
                        str(datetime.datetime.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '')
                        + '.jpg', new_pic)
    if len(detected_connectors) > 0:
        for obj in detected_capacitors:
            h0, w0, h, w = obj[0], obj[1], obj[0] + obj[2], obj[1] + obj[3]
            new_pic = pic[h0:h, w0:w]
            cv2.imwrite('./Resources/Missing_connector/' +
                        str(datetime.datetime.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '')
                        + '.jpg', new_pic)
    if len(detected_outputs) > 0:
        for obj in detected_capacitors:
            h0, w0, h, w = obj[0], obj[1], obj[0] + obj[2], obj[1] + obj[3]
            new_pic = pic[h0:h, w0:w]
            cv2.imwrite('./Resources/Missing_output/' +
                        str(datetime.datetime.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '')
                        + '.jpg', new_pic)
    update_datasets()
