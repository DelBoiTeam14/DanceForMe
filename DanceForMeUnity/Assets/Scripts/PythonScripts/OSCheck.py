import subprocess
import platform
import stat
import os


def checkOS(fileName, message):
    """checkOS() takes in 2 arguments. The filename and the message. The message is needed if the user is running the
    system with a Windows machine. This function will check whether the user is running the system using an Apple
    device or a Windows device. If it is an Apple device (Darwin), then the appropriate bash script will be run.
    If it is a Windows device, then the appropriate batch script will be run."""
    if platform.system() == "Darwin":
        st = os.stat(fileName + ".sh")
        os.chmod(fileName + ".sh", st.st_mode | stat.S_IEXEC)
        subprocess.call("./" + fileName + ".sh")
    else:
        subprocess.run([fileName + ".bat", message])
