В "All_right" - поместить фотографии правильно собранных плат целиком;

Программа каждую фогографию из папки раскадрирует на множество маленьких
(на каждой из полученных маленьких фотографий НЕ БУДЕТ пропущена какая-либо деталь),
после чего полученные "кадры" переведутся в черно-белый формат и запишутся в папку "Bad".
В файл описания (Bad.dat) попадут отн. пути полученных участков снимков.


========================================================================================================================

В "Missing_capacitor" - сразу выделенные участки с пропуском конденсатора.

Фотографии из этой папки переведутся в черно-белый формат и обрежутся до квадратной формы, после чего будут помещены в
директорию "Good".
В соответствующем файле описания (Good.dat) будут записаны отн. пути к полученным "кадрам" и их размеры.



E:/programs/OpenCV/build/x64/vc14/bin/opencv_createsamples.exe -info E:/projects/PyCharm/Practice/Good.dat -vec samples.vec -w 40 -h 40

E:/programs/OpenCV/build/x64/vc14/bin/opencv_traincascade.exe
-data haarcascade -vec samples.vec -bg E:/projects/PyCharm/Practice/Bad.dat
-numStages 16 -minhitrate 0.999 -maxFalseAlarmRate 0.4 -numPos 21 -numNeg 400 -w 40 -h 40
-mode ALL -precalcValBufSize 1024 -precalcIdxBufSize 1024

E:/programs/OpenCV/build/x64/vc14/bin/opencv_traincascade.exe -data haarcascade -vec samples.vec -bg E:/projects/PyCharm/Practice/Bad.dat
-numStages 16 -maxFalseAlarmRate 0.4 -numPos 160 -numNeg 400 -w 40 -h 40 -mode ALL -precalcValBufSize 2048 -precalcIdxBufSize 2048



Для обновления каскадов ввести поочередно эти команды:

CAPACITOR
E:/programs/OpenCV/build/x64/vc14/bin/opencv_createsamples.exe -info E:/projects/PyCharm/Practice/capacitor/Good.dat -vec E:/projects/PyCharm/Practice/capacitor/samples.vec -w 40 -h 40
E:/programs/OpenCV/build/x64/vc14/bin/opencv_traincascade.exe -data E:/projects/PyCharm/Practice/capacitor/haarcascade -vec E:/projects/PyCharm/Practice/capacitor/samples.vec -bg E:/projects/PyCharm/Practice/capacitor/Bad.dat -numStages 16 -maxFalseAlarmRate 0.4 -numPos 200 -numNeg 400 -w 40 -h 40 -mode ALL -precalcValBufSize 2048 -precalcIdxBufSize 2048


CONNECTOR
E:/programs/OpenCV/build/x64/vc14/bin/opencv_createsamples.exe -info E:/projects/PyCharm/Practice/connector/Good.dat -vec E:/projects/PyCharm/Practice/connector/samples.vec -w 20 -h 55
E:/programs/OpenCV/build/x64/vc14/bin/opencv_traincascade.exe -data E:/projects/PyCharm/Practice/connector/haarcascade -vec E:/projects/PyCharm/Practice/connector/samples.vec -bg E:/projects/PyCharm/Practice/connector/Bad.dat -numStages 16 -maxFalseAlarmRate 0.4 -numPos 200 -numNeg 400 -w 20 -h 55 -mode ALL -precalcValBufSize 2048 -precalcIdxBufSize 2048


OUTPUT
E:/programs/OpenCV/build/x64/vc14/bin/opencv_createsamples.exe -info E:/projects/PyCharm/Practice/output/Good.dat -vec E:/projects/PyCharm/Practice/output/samples.vec -w 20 -h 130
E:/programs/OpenCV/build/x64/vc14/bin/opencv_traincascade.exe -data E:/projects/PyCharm/Practice/output/haarcascade -vec E:/projects/PyCharm/Practice/output/samples.vec -bg E:/projects/PyCharm/Practice/output/Bad.dat -numStages 16 -maxFalseAlarmRate 0.4 -numPos 80 -numNeg 400 -w 20 -h 130 -mode ALL -precalcValBufSize 2048 -precalcIdxBufSize 2048
