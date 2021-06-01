from datetime import datetime
import cv2


def take_picture(date_time, path):
    # Filename
    formatted_time = date_time.strftime('%d_%m_%y - %H_%M')
    filename = f'{path}/Capture {formatted_time}.jpg'

    # Initialize the camera
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)   # 0 -> index of camera

    # Read the video input
    ret, img = cam.read()

    # If the reading is correct, save the image after 10ms
    if ret:
        cv2.waitKey(10)
        cv2.imwrite(filename, img)

    # Release the camera
    cam.release()
    cv2.destroyAllWindows()

    # Return filename
    return filename


def main():
    crnt_time = datetime.now()
    take_picture(crnt_time, './src/test_captures')


if __name__ == '__main__':
    main()
