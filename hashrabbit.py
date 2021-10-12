from bs4 import BeautifulSoup
import requests
import datetime


print("                         ███████████████████████████████████████████████████████")
print("                         █─█─██▀▄─██─▄▄▄▄█─█─█▄─▄▄▀██▀▄─██▄─▄─▀█▄─▄─▀█▄─▄█─▄─▄─█")
print("                         █─▄─██─▀─██▄▄▄▄─█─▄─██─▄─▄██─▀─███─▄─▀██─▄─▀██─████─███")
print("                         ▀▄▀▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀")
print("                         ███████████████████████████████████████████████████████")
print("--------------------------------------------------------------------------------------------------------------------------")
print("                                 This Program Is A Hash Identify Search Engine ")
print("                                             By RealRadioActive           ")
print("                                     https://realradioactive.github.io/ ")
print("                                     https://github.com/Realradioactive ")
print("--------------------------------------------------------------------------------------------------------------------------")
print("Donate - BTC -: 1QByZjKJzTqiqKdWLRRsKDu1RFNAF7YD1S ")
print("Donate - ETH -: 0xb22323451e63cF6b7D4C2C3Fe4939Fe8D5b4483D ")
print("(Max. 25 separated by newline, format hash[:salt])")
print("Type exit to exit")
#bu program https://hashes.com/ u kullanarak hash tanımlaması yapar.
def temizle():

    open('hashler.txt', 'w').close()

def tekrar():

    arama = input("Search:")
    url ="https://hashes.com/en/tools/hash_identifier"
    data = {
    "hashes":arama,
    "submitted":"true"
    }
    if (arama =="exit"):
        exit()



    istek = requests.post(url,data)
    html = istek.text
    soup = BeautifulSoup(html,'html.parser')

    temizle()
    for i in soup.find_all("div",{"class":"py-1"}):

        dosya = open("hashler.txt", "a")
        dosya.write(str(i))
        dosya.close()
        dosya = open("hashler.txt", "r")
        icerik = dosya.read()
        dosya.close()



        for line in open('hashler.txt'):

            if "Possible" in line:
                print('Search Found Hash Algorithms:')
                sonuc = line[18:-6]
                print("----------------------------------------------------------")
                print("[+]",sonuc)
                print("----------------------------------------------------------")
                save = str(input("Do you want to save the search? - yes or no -:"))

            else:
                print("Search Not Found ")
                print("Or Try Another Search Later")
                exit()

            if save == "yes" or save == "y" or save == "Y":
                dosya = open("hasharchive.txt", "a")
                veria = ("------->>>")
                verib = ("<<<-------")
                veri = ("Search:", arama, sonuc,)
                dosya.write(str(veria)+str(veri)+str(verib))
                dosya.close()

while True:
    tekrar()

