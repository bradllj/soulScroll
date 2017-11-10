import cv2
import cv2.cv as cv
import numpy
import zbar
import subprocess

class test():
    def __init__(self):
        cv.NamedWindow("w1", cv.CV_WINDOW_NORMAL)

#        self.capture = cv.CaptureFromCAM(camera_index) #for some reason, this doesn't work
        self.capture = cv.CreateCameraCapture(-1)
#        cv.SetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
#        cv.SetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 1024)
        #self.capture = cv2.VideoCapture(-1)
        #self.capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
        #self.capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 1024)
        self.vid_contour_selection()



    def vid_contour_selection(self):


      while True:

          self.frame = cv.QueryFrame(self.capture)


          aframe = numpy.asarray(self.frame[:,:])
          g = cv.fromarray(aframe)


          g = numpy.asarray(g)

          imgray = cv2.cvtColor(g,cv2.COLOR_BGR2GRAY)

          raw = str(imgray.data)
          scanner = zbar.ImageScanner()


          scanner.parse_config('enable')          
          imageZbar = zbar.Image( self.frame.width, self.frame.height,'Y800', raw)
          scanner.scan(imageZbar)

          for symbol in imageZbar:

              print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
              subprocess.call('echo "'+ symbol.data +'"| festival --tts', shell=True)          


          cv2.imshow("w1", aframe)

          c = cv.WaitKey(5)

      if c == 110: #pressing the 'n' key will cause the program to exit
        exit()
#        
p = test()
