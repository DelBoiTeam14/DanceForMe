import OSCheck
# This Python script will only be run once. Since the game will loop back to the IdleMode Scene after the
# leaderboard scene. You don't want to loop back to start.bat file since it will open up another instance
# of the unity project. In order to avoid that. This should be run instead of PersonDetect.py for the first
# iteration. Afterwards, PersonDetect.bat will run instead of start.bat
# This is a terrible practice, but I don't see another way around it.

# The following commented code will write a message to a file so the bat file can read the output
# with open("message.txt", "w") as f:
#     f.write(message)
# subprocess.run(["PersonDetect.bat"], stdin=open("message.txt", "r"))

OSCheck.checkOS("PersonDetect", "Starting PersonDetect.py")
