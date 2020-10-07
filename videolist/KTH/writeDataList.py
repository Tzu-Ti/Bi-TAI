import random

filename = 'val_data_list_K=F=7.txt'
f = open(filename, 'r')
videolist = []
previousName = 'qwetrdfastg'
for line in f:
    data = line.split(' ')
    videoname = data[0]
    if videoname not in videolist:
        videolist.append(videoname)
    previousName = videoname
f.close()
    
for name in videolist:
    print(name)

clipnumbers = []
f = open('dataclips.txt', 'r')
for line in f:
    clipnumbers.append(line[-4:-1])
f.close()

f = open('val_data_list_K=F=5.txt', 'w')
for index, num in enumerate(clipnumbers):
    num = int(num)
    maxElevenMultiRange = num / 11
    videoname = videolist[index]
    print(videoname)
    for multi_index in range(maxElevenMultiRange):
        start_index = multi_index * 11 + 1
        end_index = start_index + 11 - 1
        print(start_index, end_index)
        dataString = '%s %d-%d\n' %(videoname, start_index, end_index)
        f.write(dataString)
    
f.close()
    