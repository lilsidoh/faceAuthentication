import time
import os
from captureFace import faceAuthentication


def prosessor():
    print('[INFO] PhasePass select an option to conute:\n\t[1] Register\n\t[2] Authenticate\n\t[3] Exit')
    option = input('[INFO] Select: ')
    if int(option) == 1:
        time.sleep(2)
        userName = input("[INFO] Enter UserName : ")
        print("[INFO] UserName will be used for authentication:")
        directory = "imageTest"
        time.sleep(2)
        faceAuthentication.authenticateFace(directory, userName)
        time.sleep(2)
        print('[INFO] Image captured you can now login with your image as your password:')
    elif int(option) == 2:
        time.sleep(2)
        import blinkDetection
        print('[INFO] Matching face for authentication:') 
        os.chdir('..')
        import faceMatch

    elif int(option) == 3:
        exit()

prosessor()
