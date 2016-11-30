import cv2

img = []
cnt=0
while cnt>=0:
	tmpimg = cv2.imread('./frames/frame'+str(cnt)+'.jpg')
	if tmpimg is None:
		break
	img.append(tmpimg)
	if cnt%100 is 0:
		print(str(cnt) + 'loaded')
	cnt = cnt+1

height , width , layers =  img[0].shape
print(str(height) + ',' + str(width) + ',' + str(layers))

video = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('m','p','4','2'),15,(width,height))

# video = cv2.VideoWriter('output.avi',-1,30,(width,height))
if video.isOpened():
	print("ok!")
i=0
for i in range(0,cnt-1):
	video.write(img[i])

cv2.destroyAllWindows()
video.release()
