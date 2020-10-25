import face_recognition
import cv2
import os
from imutils import paths
import pickle
import time

def imagesNames():

    #imagePath = os.listdir("/root/projects/FaceRecognition/FaceDetection/imageTeest")
    imagePaths = list(paths.list_images("./knownImages"))
    knownEncodings = []
    knownNames = []

    for (i, imagePath) in enumerate(imagePaths):
        name = imagePath.split(".")[-2].split("/")[-1]
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb , model="hog", number_of_times_to_upsample=1)
        encodings = face_recognition.face_encodings(rgb, boxes, num_jitters=3)
        #print encodings
        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames .append(name.split("_")[0].lower())

    data = {"encodings" : knownEncodings, "names" : knownNames}
    dataFile = open("encodings.pickle", "wb")
    dataFile.write(pickle.dumps(data))
    dataFile.close()

    def predictFace(imagepath):
        image = cv2.imread(imagepath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes  = face_recognition.face_locations(rgb, model='hog', number_of_times_to_upsample=3)
        encodings = face_recognition.face_encodings(rgb, boxes) #num_jitters=100
        names = []
        for encoding in encodings:
            matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance=0.45)
            #print( matches)
            name = "uknown"
            
            if True in matches:
                matchedIndex = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                for i in matchedIndex:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                    name = max(counts, key=counts.get)
            else:
                print("No matches")
                    
            return name

    testFolder = './imageTest'
    #actual = []
    predicted = []
    startTime = time.time()
    for filename in os.listdir(testFolder):
        img = cv2.imread(os.path.join(testFolder, filename))
        #actual.append(str(os.path.join(testFolder, filename).split("_")[0].split("/")[2].split(".")[0].lower()))
        #check if the image is uploaded successfully
        if img is not None:
            fullPath = os.path.join(testFolder, filename)
            matchedPerson = predictFace(fullPath)
            predicted.append(matchedPerson)
            
        else:
            print("No image found")

    for predict in predicted:
        print ('[INFO] Authenticating {}'.format(predict))

imagesNames()

'''if __name__ == '__main__':
    imagesNames()
'''
