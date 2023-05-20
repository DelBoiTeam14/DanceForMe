import sys
import subprocess


def reset():
    pid = 0
    p = subprocess.Popen("tasklist /v /fi \"imagename eq cmd.exe\" /fo csv", stdout=subprocess.PIPE)
    out, err = p.communicate()
    for line in out.decode().splitlines():
        if "PersonDetect.bat" in line:
            pid = int(line.split(",")[1].replace("\"", ""))
        elif "Tutorial.bat" in line:
            pid = int(line.split(",")[1].replace("\"", ""))

    terminateMessage = "Exits Unity"
    # Terminate the batch file process
    subprocess.call("taskkill /f /pid {} /t".format(pid), shell=True)
    # TerminateUnityExe.bat will terminate the current DanceForMe.exe instance
    subprocess.run(["TerminateUnityExe.bat", terminateMessage])
    # Start a new bat script
    message = "Going back to the idling page"
    subprocess.run(["start.bat", message])
    sys.exit()
