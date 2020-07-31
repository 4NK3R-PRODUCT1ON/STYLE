#!/usr/etc/python
#!/usr/etc/bash
import sys,os,platform
from time import *
x = platform.system()
import requests
from tqdm import tqdm
import random
import time
G = "\033[32;1m" 
Gt = "\033[0;32m" 
Bt = "\033[34;1m" 
b = "\033[36;1m" 
R = "\033[31;1m" 
c = "\033[0m" 
W = "\033[37;1m" 
u = "\033[35;1m" 
M = "\033[3;1m" 
k = "\033[33;1m" 
kt = "\033[0;33m" 
a = "\033[30;1m" 
#
#
os.system("clear")
print ""+k+"\t\t\t[ WELCOME CREATE SCREEN ]"
nama = raw_input(""+Bt+"[ Input YoUr Name ]>> "+W+" ")
os.system("clear")
print ""+k+"\t\t\t[ WELCOME CREATE SCREEN ]"
print ""
print ""+W+"Selamat Datang Kembali "+G+"[", nama,"]"+W+" Semoga Hari Mu Menyenangkan Dan Tuan Sehat Selalu"
os.system("sleep 2")
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)
mengetik(' Selamat Menggunakan Create Screen Instan Untuk Mempercantik Tampian Termux Dan Linux anda hanya dengan Program yang sederhana, Namun Kualitas Terbaik')
os.system("clear")
mengetik('Menginstall Package Yang di Butuhkan.. [ Loading ]')
os.system('sleep 3')
os.system("apt-get install bash")
os.system("apt-get install fish")
os.system("gem install lolcat")
os.system("sleep 2")
mengetik("Semua Package Telah Selesai Di Install.")
os.system("sleep 3")
os.system("clear")
print ""+k+"\t\t\t[ WELCOME CREATE SCREEN ]"+W+""
mengetik('Screen Tuan Sedang Di Buat..  [ Harap Tunggu ]')
os.system("sleep 3")
os.system("clear")
print ""+k+"\t\t\t[ WELCOME CREATE SCREEN ]"+W+""
print "Screen Tuan Sedang Di Buat..  [ Selesai ]"
os.system("sleep 3")
mengetik('Screen Tuan Sedang Di Pasang..  [Harap Tunggu]')
os.system("sleep 3")
os.system("clear")
print ""+k+"\t\t\t[ WELCOME CREATE SCREEN ]"+W+""
print "Screen Tuan Sedang Di Buat..  [ Selesai ]"
print "Screen Tuan Sedang Di Pasang..  [Selesai]\n\n"
mengetik(' CopyRight INDOnimoue Hack Theme Create Screen Instan 2019 ')
os.system("mv screen.sh /data/data/com.termux/files/usr/libexec/termux/")
os.system("rm -rf  /data/data/com.termux/files/usr/etc/bash.bashrc/")
os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc/")
os.system("chmod +x /data/data/com.termux/files/usr/libexec/termux/screen.sh")
os.system("sleep 4")
