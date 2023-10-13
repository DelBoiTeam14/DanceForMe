#!/bin/bash
pip3 install opencv-python==4.6.0.66
pip3 install mediapipe
pip3 install numpy
pip3 install python-osc
./../DanceForMeExe/MacDanceForMe.app/Contents/MacOS/DanceForMeUnity &
python3 ../DanceForMeUnity/Assets/Scripts/PythonScripts/Starting.py 
