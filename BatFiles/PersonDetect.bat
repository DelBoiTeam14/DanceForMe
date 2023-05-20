@ECHO OFF
Rem set /p message=<message.txt
Rem echo "\nMessage is %message%"
Rem  The following python script will check if the user is still here. FIXME Need to run a while loop to keep this running at all time
Rem start /b "" "python.exe" "DanceForMeUnity\Assets\Scripts\PythonScripts\checkInactivity.py"
timeout /t 5 > NUL
start /b "" "python.exe" "..\DanceForMeUnity\Assets\Scripts\PythonScripts\PersonDetect.py"




