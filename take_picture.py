from datetime import datetime
import cv2


def take_picture(date_time, path):
    # Filename
    formatted_time = date_time.strftime('%d_%m_%y - %H_%M')
    filename = f'{path}/Capture {formatted_time}.jpg'
    # Initialize the camera
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)   # 0 -> index of camera
    # Take and save the picture
    _, img = cam.read()                        # take picture
    cv2.imwrite(filename, img)                 # save image
    # Release the camera
    cam.release()
    cv2.destroyAllWindows()
    # Return filename
    return filename


def main():
    crnt_time = datetime.now()
    take_picture(crnt_time, './TestCaptures')


if __name__ == '__main__':
    main()
