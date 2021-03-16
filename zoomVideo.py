import cv2

scale=500
cam = cv2.VideoCapture('/home/pi/Downloads/04.avi')
while True:
        ret_val, image = cam.read()

        image = cv2.flip(image, 1)

        #get the webcam size
        height, width, channels = image.shape

        #prepare the crop
        centerX,centerY=int(height/2),int(width/2)
        radiusX,radiusY= int(scale*height/100),int(scale*width/100)

        minX,maxX=centerX-radiusX,centerX+radiusX
        minY,maxY=centerY-radiusY,centerY+radiusY

        cropped = image[minX:maxX, minY:maxY]
        resized_cropped = cv2.resize(cropped, (width, height))

        cv2.imshow('my webcam', resized_cropped)
        if cv2.waitKey(1) == 27:
            break  # esc to quit

        #add + or - 5 % to zoom

        if cv2.waitKey(1) == 0:
            scale += 5  # +5

        if cv2.waitKey(1) == 1:
            scale = 5  # +5

cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()