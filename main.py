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
  print('not done yet')
else:
  print('run again')

# Print the current working directory
#print("Current working directory: {0}".format(os.getcwd()))

os.system('python main.py')