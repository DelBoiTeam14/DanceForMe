@ECHO OFF

echo Terminating
set UnityProcessName=DanceForMeUnity.exe
for /f "tokens=2 delims==;" %%a in ('wmic process where "name='%UnityProcessName%'" get processid /value ^| findstr /r "^ProcessId"') do set UnityPID=%%a
if not [%UnityPID%]==[] (
    echo Terminating Unity process %UnityPID%
    taskkill /f /pid %UnityPID%
) else (
    echo Unity process not found
)

