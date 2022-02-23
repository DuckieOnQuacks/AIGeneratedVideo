import cv2

infile = "C:\\Users\\jojop\\Desktop\\Oliver Tree - Cowboys Don't Cry [Music Video] (1).mp4"
in1 = "C:\\Users\\jojop\\Desktop\\INPUT"

vidcap = cv2.VideoCapture(infile)
success,image = vidcap.read()
count = 0
success = True

while success:
  success,image = vidcap.read()
  cv2.imwrite(in1+"\\" + "%d.jpg" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1