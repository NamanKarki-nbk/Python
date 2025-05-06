with open(".\\Session-03\\tsukasa.txt") as f:
    # print(f.read())
    f.write("Woops! I have deleted the content!")
    print(f.readline())
    
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
import os
os.rmdir("myfolder")