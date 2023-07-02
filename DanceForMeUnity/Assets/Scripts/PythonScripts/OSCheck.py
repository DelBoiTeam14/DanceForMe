import subprocess
import platform
import stat
import os


def checkOS(fileName, message):
    if platform.system() == "Darwin":
        st = os.stat(fileName + ".sh")
        os.chmod(fileName + ".sh", st.st_mode | stat.S_IEXEC)
        subprocess.call("./" + fileName + ".sh")
    else:
        subprocess.run([fileName + ".bat", message])
