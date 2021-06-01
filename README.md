# PC LOG ALERT

Receive a message on Telegram whenever someone login on your computer account.  
The message will contain the time of the access and a picture taken from the computer's webcam.

## DEPENDENCIES

Install the following libraries in your virtual environment:

- requests
- opencv-python
- pyinstaller

## HOW TO MAKE IT WORK

1. Create a new Telegram bot and save your BOT_TOKEN and BOT_CHAT_ID keys in a file called keys.py, situated in the src directory.
2. Specify the variables PC_NAME and IMG_PATH in a file called config.py, situated in the src directory. PC_NAME is a string to identify your pc; IMG_PATH is the absolute path to the folder you want to save the pictures in (eg: 'C:/Pictures/Recorded Accesses').
3. Run the script create_exe.py in the console. The executable send_alert.exe should be created in the dist folder.
4. Create a new event in the Windows Event Scheduler, which starts on user login and executes send_alert.exe.
