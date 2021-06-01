# PC LOG ALERT

Receive a message on Telegram whenever someone login on your computer account.  
The message will contain the time of the access and a picture taken from the computer's webcam.

## HOW TO MAKE IT WORK

1. You need to create a new Telegram bot and save your BOT_TOKEN and BOT_CHAT_ID keys in a file called keys.py, situated in this directory.
2. You nedd to specify the variables PC_NAME and IMG_PATH in a file called config.py, situated in this directory. PC_NAME is a string to identify your pc; IMG_PATH is the absolute path to the folder you want to save the pictures in (eg: 'C:/Pictures/Recorded Accesses').
3. Change the path in PCAlert_Start.vbs to match the absolute path of the file send_alert.py on your computer.
4. Create a new event in the Windows Event Scheduler, which starts on user login and executes PCAlert_Start.vbs.
