import cv2  
import os 

class faceAuthentication():
 
    path = "/root/projects/projectFelix/faceAuthentication/faceDetection"
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');


    def __init__(self):
        pass 
    @classmethod
    def changeDir(self, directory):

        #creating directory to save the image of users who login 
        fullPath = os.path.join(self.path, directory)
        #check if the fullPath directory exist
        if os.path.isdir(fullPath):
            os.chdir(fullPath)
        #create a directory it doesnt exits
        else:
            os.mkdir(fullPath)
            os.chirdir(fullPath)
            
    @classmethod
    def authenticateFace(self, directory, userName):

        count = 0
        video = cv2.VideoCapture(0);
        while True:
        check, frame = video.read();
            faces = self.face_cascade.detectMultiScale(frame,scaleFactor=1.1, minNeighbors=5);
            for x,y,w,h in faces:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 1);
                roiColor = frame[y:y + h, x:x + w]
            cv2.imshow('Face Detector', frame);

            key = cv2.waitKey(1000);
            self.changeDir(directory)
            imageName = "{}.jpg".format(userName)
            cv2.imwrite(imageName, roiColor)
            os.chdir(self.path)
            break


        video.release();
        cv2.destroyAllWindows()

def main():

    userName = input("[INFO] Enter UserName : ")
    directory = "imageTest"
    authenticate = faceAuthentication()
    authenticate.authenticateFace(directory, userName)

if __name__ == '__main__':
    main()
