import cv2
import numpy as np 

 
class DrawingWindow:
    def __init__(self):
        self.drawing = False # true if mouse is pressed
        self.mode = True
        self.im = cv2.imread("white-background.png")
        cv2.namedWindow("white background image")
        cv2.setMouseCallback('white background image', self.draw)

        self.keepWindowUntil()

    def keepWindowUntil(self):
        while(True):
            cv2.imshow('white background image', self.im)
            k = cv2.waitKey(1) #&0xFF
            if k==27:
                break
        
        cv2.destroyAllWindows()

    # mouse callback function
    def draw(self, event, former_x, former_y, flags, param):
        global current_former_x, current_former_y

        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            current_former_x, current_former_y = former_x, former_y

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing == True:
                if self.mode == True:
                    cv2.line(self.im, (current_former_x, current_former_y) ,(former_x, former_y), (0,0,255), 5)
                    current_former_x = former_x
                    current_former_y = former_y
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            if self.mode == True:
                cv2.line(self.im, (current_former_x, current_former_y), (former_x, former_y), (0,0,255), 5)
                current_former_x = former_x
                current_former_y = former_y
        return former_x, former_y  


