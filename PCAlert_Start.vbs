' This Visual Basic script run the python script in silent mode
'	i.e. without the appearence of the command prompt

Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "D:\MyProjects\Python\PCLogAlert\send_alert.py" & Chr(34), 0
Set WshShell = Nothing
