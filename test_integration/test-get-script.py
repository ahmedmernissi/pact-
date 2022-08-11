# IMPORT BDD MODULE
import os
# Condition if we ar in dev branch
if 'BDD' in os.listdir('..'):
    # Import module
    import Library
    # Set imported to True
    BDD = True
else:
    BDD = False

work = Library.getWork(5)
script = work.getScript()
script.matrixES = script.matrixES.replace("{","").replace("}","").split(",")
print(script.matrixES)
print(script.matrixES[2])