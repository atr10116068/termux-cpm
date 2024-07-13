import os
import json
import random
import math
import time
import sys, requests
import random as rdm
from colr import color

def disp(clrnama):
    clrfirsttime = True
    clrVnama = clrnama.split("[")
    clrdisps = clrVnama[0]
    for clrx in clrVnama:
        if clrfirsttime == False:
            clrcode1 = f"{clrx[0:2]}"
            clrcode2 = f"{clrx[2:4]}"
            clrcode3 = f"{clrx[4:6]}"
            clrcode1 = (int(clrcode1, 16))
            clrcode2 = (int(clrcode2, 16))
            clrcode3 = (int(clrcode3, 16))
            clrhuruf = clrx[7:8]
            clrdisps += color(clrhuruf,
                              fore=(clrcode1,
                                    clrcode2,
                                    clrcode3),
                              back=(0, 0, 0))
        if clrfirsttime:
            clrfirsttime = False

    clrdisps += clrVnama[len(clrVnama)-1][8:len(clrVnama[len(clrVnama)-1])]
    return(clrdisps)

def generate():
    gabungwarna = ""
    contohnama = input("Nama anda adalah :")
    # proses memecah huruf di nama
    data = {
        "huruf": "",
        "kodewarna": [255, 0, 0],
        "mode": 1,
        "kodewarnaCPM": ""
    }
    while True:
        tanya = input("Mulai dari warna apa? [merah/hijau/biru] : ")
        if tanya == "merah":
            data["kodewarna"] = [255, 0, 0]
            break
        elif tanya == "hijau":
            data["kodewarna"] = [0, 255, 0]
            break
        elif tanya == "biru":
            data["kodewarna"] = [0, 0, 255]
            break
        else:
            print("Harus sesuai pilihan warna ..!")

    for huruf in contohnama:
        while True:
            # print(f"\nmode sekarang : {data['mode']}")
            tambah = 45
            if data["mode"] == 1:
                if data["kodewarna"][1]+tambah <= 255:
                    data["kodewarna"][1] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [255, 255, 0]
            elif data["mode"] == 2:
                if data["kodewarna"][0]-tambah >= 0:
                    data["kodewarna"][0] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 255, 0]
            elif data["mode"] == 3:
                if data["kodewarna"][2]+tambah >= 255:
                    data["kodewarna"][2] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 255, 255]
            elif data["mode"] == 4:
                if data["kodewarna"][1]-tambah >= 0:
                    data["kodewarna"][1] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 0, 255]
            elif data["mode"] == 5:
                if data["kodewarna"][0]+tambah >= 255:
                    data["kodewarna"][0] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [255, 0, 255]
            elif data["mode"] == 6:
                if data["kodewarna"][2]-tambah >= 255:
                    data["kodewarna"][2] -= tambah
                    break
                else:
                    data["mode"] = 1
                    data["kodewarna"] = [255, 0, 0]
        # print(f"{huruf} {data['kodewarna']}")
        gabungwarna += color(huruf,
                             fore=(data["kodewarna"][0],
                                   data["kodewarna"][1],
                                   data["kodewarna"][2]),
                             back=(0, 0, 0))
        kodas = []
        for t in range(3):
            clrcode = hex(data["kodewarna"][t])[2::]
            if len(clrcode) == 1:
                clrcode += "0"
            kodas.append(clrcode)
        data["kodewarnaCPM"] += f"[{kodas[0]}{kodas[1]}{kodas[2]}]{huruf}"
    print(f"hasil\t:  {disp(data['kodewarnaCPM'])}")
    print(f"kode\t:  {data['kodewarnaCPM']}")
    return data["kodewarnaCPM"]


v="4.8"
try:
    import wget,httpx
    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
except:
    os.system("pip install httpx")
    os.system("pip install wget")
    os.system("pip install pystyle")
    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem

pySystem.Clear()
pySystem.Size(120, 40)


text = """
< [ YouTube TopixSB ] > X < [ ₱ⱤØ₲Ɽ₳₥ ฿Ɇ₮₳ ] >"""[1:]

banner = r"""
___ç$$$ç________________
__$$$$$$$_####______####_       YouTube TopixSB
___*$$$$$$ç####___########        
_____*$$$$$$$$$$$##########     ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█
_____$$$$$$$$$$$$$##########    ░▒█░░ ░▀▀▀▄▄ ▒█▀▀▄
______$$$$$$$$$$$$$##########   ░▒█░░ ▒█▄▄▄█ ▒█▄▄█ 
______$$$$$$$$$$_$$$##########
______$$$$$$$$$$##$$$##########
_______$$$$$$$$$_##$$##########
______$$$$$$$$$$___$$#########
_____$_$$$$$$$$$$__$$_########
___$$__$$$$$$$$$$_$$$__######
______$$$$$$$$$$__$$$___#####
______$$$$$$$$$___$$____####
______$$$$$$$$$_________###
______$$$$$$$$__________##
_______$$$$$$___________##
_______$$$$$$______________
_______$$$$$$$$____________
_______$$$$$$$$____________
_______$$$$_$$$$___________
_______$$$$_$$$$___________
_______$$$___$$$$__________
__ççç$$$$$$_çç$$$$__________       
                          
           Car Parking Multiplayer Instant Script
                    LESS THEN 1 MINUTE

                        PRESS ENTER          
"""[1:]


pyAnime.Fade(pyCenter.Center(banner), pyColors.purple_to_red, pyColorate.Vertical, enter=True)

pySystem.Clear()

print("\n"*2    )
print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))
print("\n"*2)


persi=httpx.get("https://raw.githubusercontent.com/atr19love/rilis/master/versi.txt").text
newsc=httpx.get("https://raw.githubusercontent.com/atr19love/rilis/master/topixsb.py").text
if v!=persi:
    with open("topixsb.py", "w") as file1:
        file1.write(newsc)
    print(f"Updateing TopixSB Termux Tools {persi} Version")
dat={"Vip":0}


delet=["cpm/pos.py","cpm/__init__.py"]
for psdd in delet:
    if os.path.exists(f"{psdd}") == True:
        os.system(f"rm {psdd}")



def c(colr, tex):
    try:
        w = {
            "RED": [255, 0, 0],
            "GREEN": [0, 255, 0],
            "CYAN": [0, 255, 255],
            "YELLOW": [255, 255, 0],
            "GOLD": [255, 223, 0]
        }
        return color(tex,
                     fore=(w[colr.upper()][0],
                           w[colr.upper()][1],
                           w[colr.upper()][2]),
                     back=(0, 0, 0))
    except:
        return tex


print()
tex="""


Wajib BACA
1. Harus Logout dari apk CPM dulu 
kecuali hanya ingin pakai fitur 
inject rank dan instant rank
karna 2 fitur itu tidak perlu logout

2. Isi Credit Script termux di t.me/topixsb
3. Cara Pakainya ada di YT TopixSB
"""


    
bannerwz = f"""
{c("cyan","=======================================================================")}
    Topix SB CPM TOOLS {persi} {c("cyan","||")} {c("green","https://carparking.topixsb.dev/")}
{c("cyan","=======================================================================")}"""

print(pyColorate.Horizontal(pyColors.green_to_yellow, pyCenter.XCenter(tex)))
print(bannerwz)
if __name__ == "__main__":
    uname = input("  username : ")
    upass = input("  password : ")
    while True:
        pySystem.Clear()
        print(bannerwz)
        
        input("")
