# Import the os module
import os

print('What lab would you like to run? (0-10)')
x = input()
x = int(x)
# Print the current working directory
#print("Current working directory: {0}".format(os.getcwd()))

# Change the current working directory
if x == 0:
  os.chdir('./000_Base_Folder')
elif x == 1:
  os.chdir('./001_Input_&_Variables')
elif x == 2:
  os.chdir('./002_Conditionals')
elif x == 3:
  os.chdir('./003_else_elif')
elif x == 4:
  os.chdir('./004_Random')
elif x == 5:
  os.chdir('./005_Lists&Loops')
elif x == 6:
  os.chdir('./006_Dictionaries')
else:
  print('run again')

# Print the current working directory
#print("Current working directory: {0}".format(os.getcwd()))

os.system('python main.py')
