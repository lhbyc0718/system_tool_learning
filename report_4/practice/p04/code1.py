import subprocess
subprocess.Popen("ls", shell=True)
subprocess.Popen(["ls"], shell=False)
