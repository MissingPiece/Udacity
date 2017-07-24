import os

def rename_files():
  file_list = os.listdir(r"C:\Users\Kevin\Udacity\Intro_to_programming\Python\prank")
  os.chdir(r"C:\Users\Kevin\Udacity\Intro_to_programming\Python\prank")
  for file_name in file_list:
      os.rename(file_name,file_name.translate(None, "0123456789"))


rename_files()
