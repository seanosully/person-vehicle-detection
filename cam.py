import cv2

def get_image(imageName):
    # Change argument based on the camera you are yousing. Default is your webcam
    cam = cv2.VideoCapture(0)

    result, image = cam.read()

    if result:
        cv2.imwrite(imageName, image)

    else:
        print("error accessing image")

    return imageName
