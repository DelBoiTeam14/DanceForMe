@ECHO OFF
pip install opencv-python==4.6.0.66
pip install mediapipe
pip install numpy
pip install python-osc
ECHO Starting Dance For Me Unity Project
start /b "" "..\DanceForMeExe\DanceForMeUnity.exe"
ECHO Starting PersonDetect.py
start /b "" "python.exe" "..\DanceForMeUnity\Assets\Scripts\PythonScripts\Starting.py"




