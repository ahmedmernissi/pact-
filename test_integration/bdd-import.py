# Copy Library.py to each sub dir
import os
import shutil

dirs = os.listdir(".")
dirs.remove("BDD")
dirs.remove(".git")
for repo in dirs:
	if os.path.isdir(repo):
		# Copying BDD module into each module
		print("[*] Copying Library into ", repo)
		shutil.copyfile("./BDD/Library.py", repo + "/Library.py")
		# Copying Son module for systemes embarques and CI
		shutil.copyfile("./Son/AmbianceSonore.py", "SE/AmbianceSonore.py")
		shutil.copyfile("./Son/AmbianceSonore.py", "test_integration/AmbianceSonore.py")
