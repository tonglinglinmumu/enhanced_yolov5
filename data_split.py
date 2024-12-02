import os
import random

trainval_percent = 0.9
train_percent = 0.9
xmlfilepath = 'D:/yolov5-mask-42-master/data/PCBDatasets/xml/'
txtsavepath = 'D:/yolov5-mask-42-master/data/PCBDatasets/dataSet/'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('D:/yolov5-mask-42-master/data/PCBDatasets/dataSet/trainval.txt', 'w')
ftest = open('D:/yolov5-mask-42-master/data/PCBDatasets/dataSet/test.txt', 'w')
ftrain = open('D:/yolov5-mask-42-master/data/PCBDatasets/dataSet/train.txt', 'w')
fval = open('D:/yolov5-mask-42-master/data/PCBDatasets/dataSet/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()