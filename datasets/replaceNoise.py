import os
import numpy as np
import cv2

originDataset = 'KTH'
noiseDataset = 'KTH-noise'

originFolder = os.listdir(originDataset)

fourcc = cv2.VideoWriter_fourcc(*'DX50')

for filename in originFolder:
    filepath = os.path.join(originDataset, filename)
    print(filepath)
    
    # Read video and put frames in list(video_frame)
    print(os.path.isfile(filepath))
    cap = cv2.VideoCapture(filepath)
    print(cap.isOpened())
    video_frame = []
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            video_frame.append(gray)
        else:
            break
    print("Length: %d" % len(video_frame))
    
    # Replace specified frame to noise
    for index, frame in enumerate(video_frame):
        if (index % 11 == 1) or (index % 11 == 3) or (index % 11 == 7) or (index % 11 == 9):
            noise = np.random.normal(0, 255, frame.shape)
            noise = noise.astype('uint8')
            video_frame[index] = noise
            
    savename = os.path.join(noiseDataset, filename)
    print("Saving %s ..." % savename)
    out = cv2.VideoWriter(savename, fourcc, 25, (160, 120), False)
    for frame in video_frame:
        out.write(frame)
    
    cap.release()
    out.release()