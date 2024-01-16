import os
import arrow
import subprocess
from pathlib import Path

current_date = arrow.now().format('YYYY-MMM-DD-HH-mm')
file_path = Path("C:\\Users\\mp71517\\OneDrive-Deere&Co\\OneDrive - Deere & Co\\Documents\\ClassWork\\2024")

file_name = current_date + str('.yml')
full_file_path = os.path.join(file_path, file_name)

if not os.path.exists(full_file_path):
    f = open(full_file_path, "w+")
    print ("New File {} was created successfully".format(file_name))

subprocess.call(['C:\\Program Files\\Notepad++\\notepad++.exe', full_file_path])
