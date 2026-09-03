import subprocess
import sys

"""
255 = puzzle
2 = ile_au_tresor
3 = Donjon
4 = Manoir
5 = shop
6 = regles
8 = boss

"""
while True:
    code = subprocess.run([sys.executable, "en_mer.py"]).returncode
    
    if code == 255:
        subprocess.run([sys.executable, "puzzle_knk_odyssee_final2.py"])
    if code == 2:
        subprocess.run([sys.executable, "ile_au_trésor2.py"])
    if code == 3:
        subprocess.run([sys.executable, "Donjon2.py"])
    if code == 4:
        subprocess.run([sys.executable, "Manoir2.py"])
    if code == 5:
        subprocess.run([sys.executable, "shop2.py"])
    if code == 6:
        subprocess.run([sys.executable, "regles2.py"])
    if code == 8:
        subprocess.run([sys.executable, "boss_poseidon_.py"])
    if code == 0:
        break
    else:
        pass