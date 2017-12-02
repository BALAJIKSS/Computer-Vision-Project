import cv2

inputFile = "vidfin.mp4"

w = 10
g = 25
v = 8
batchSize = 200
lamdaS = 10
lamdaA = 10


outptFile = inputFile.split('.')[0] + "_naive" + '.mp4'

cap = cv2.VideoCapture(inputFile)
ret, frame = cap.read()
fCount = 0
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')

size = (frame.shape[1], frame.shape[0])
vid = cv2.VideoWriter(outptFile, fourcc, 30, size, True)

while ret:
    if fCount % v == 0:
        vid.write(frame)
    temp = 0
    ret, frame = cap.read()
    while temp < 5 and ret == False:
        ret, frame = cap.read()
        print temp
        temp += 1
    print fCount, temp, ret
    fCount += 1

print "Done"
cap.release()
vid.release()
