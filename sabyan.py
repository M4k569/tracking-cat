#-*- coding: utf 8 -*-
#
#  Cuk Jan Lupa Doain W Ya :") Semoga 
#  Punya istri kek sabyan :v nissa nya ya bukan grup nya :"v
#  Cape cuk Ngefans Ter0000s :v Knpa Malah Curhat oaqkoaka
#
#  -Muh4k3mos


import json,requests,os
import time
import argparse
import sys , random, time

b = "\033[96m"
w = "\033[97m"
m = "\033[91m"
h = "\033[92m"
c = "\033[1;36m";
n = "\n"

def k2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)


print("""
%sIP-Location%s
-----------
        \   ^__^
         \  (oo)\_______         %sBy %sKalsel Exploit%s
            (__)\       )\/\     %sAuthor : %smuh4k3mos & Mr_MSDV%s
                ||----w |
                ||     ||
"""%(b,w,m,b,w,m,c,w))

parsing = argparse.ArgumentParser(description="%sapi choice : %sserv1,serv2,serv3,serv4%s"%(m,h,w))
parsing.add_argument('-a','--api',metavar='',dest='url',help="sto enter a api/server")
parsing.add_argument('-i','--ip',metavar='',dest='ip',help='Enter an IP address to check {} '.format(n))
args=parsing.parse_args()

def server(ip,api):
        if api == 'serv1':
           url="https://extreme-ip-lookup.com/json/"+ip
           print("[!] with https://extreme-ip-lookup.com \n")
           time.sleep(3)
           sabyan = json.loads(requests.get(url).text)
           class serv:
                 try:
                         status = sabyan['status']
                         if status == '':
                            status = 'tidak ditemukan'
                         else:pass
                         city = sabyan['city']
                         if city == '':
                            city = 'tidak ditemukan'
                         else:pass
                         kerja = sabyan['businessWebsite']
                         if kerja == '':
                            kerja = 'tidak ditemukan'
                         else:pass
                         tipe = sabyan['ipType']
                         if tipe == '':
                            tipe = 'tidak ditemukan'
                         else:pass
                         kodenegara = sabyan['countryCode']
                         if kodenegara == '':
                            kodenegara = 'tidak ditemukan'
                         else:pass
                         negara = sabyan['country']
                         if negara == '':
                            negara = 'tidak ditemukan'
                         else:pass
                         wilayah = sabyan['region']
                         if wilayah == '':
                            wilayah = 'tidak ditemukan'
                         else:pass
                         isp = sabyan['isp']
                         if isp == '':
                            isp = 'tidak ditemukan'
                         else:pass
                         kordinat = sabyan['lat']+' '+sabyan['lon']
                         if kordinat == ' ':
                            kordinat = 'tidak ditemukan'
                         else:pass
                         bisnis = sabyan['businessName']
                         if bisnis == '':
                            bisnis = "tidak ditemukam"
                         else:pass
                         namaip = sabyan['ipName']
                         if namaip == '':
                            namaip = 'tidak ditemukan'
                         else:pass
                         perusahaan = sabyan['org']
                         if perusahaan == '':
                            perusahaan = 'tidak ditemukan'
                         else:pass
                         benua = sabyan['continent']
                         if benua == '':
                            benua = 'tidak ditemukan'
                         else:pass
                 except KeyError:
                        print "\n[*] ip address not found \n"
                        sys.exit()
           print("status : {} ".format(serv.status)+"tipe ip : %s "%(serv.tipe))
           print("kota : {}".format(serv.city))
           print("benua :{} ".format(serv.benua))
           print("negara : {}".format(serv.negara))
           print("kode negara : {} ".format(serv.kodenegara))
           print("wilayah : {}      ".format(serv.wilayah))
           print("pji : {}    ".format(serv.isp))
           print("bisnis : {}      ".format(serv.bisnis))
           print("perusahaan : {}      ".format(serv.perusahaan))
           print("Situs Web Bisnis : {}".format(serv.kerja))
           print("Kordinat : {} ".format(serv.kordinat))
       
       
        elif api == 'serv2':
                url="https://ipinfo.io/"+ip+"/json"
                print("\n[*] with https://ipinfo.io/ \n")
                time.sleep(3)
                sabyan = json.loads(requests.get(url).text)
                if 'error' in sabyan:
                   for cekc in sabyan['error']:
                       if 'message' in cekc:
                          print("[!] ip address not found \n")
                          sys.exit()
                       else:pass
                else:
                     class serv:
                                  try:
                                      com = sabyan['org']
                                  except KeyError:
                                         com = 'tidak ditemukan'
                                  try:
                                         poustal = sabyan['poustal']
                                  except KeyError:
                                         poustal = 'tidak ditemukam'
                                  try:
                                        host = sabyan['hostname']
                                  except KeyError:
                                         host = 'tidak temukan'
                                  kota = sabyan['city']
                                  if kota == '':
                                     kota = 'tidak ditemukan'
                                  else:pass
                                  try:
                                       koden = sabyan['country']
                                  except KeyError:
                                         koden = 'tidak ditemukan'
                                  wila = sabyan['region']
                                  if wila == '':
                                         wila = 'tidak ditemukan'
                                  else:pass
                                  try:
                                         zonw = sabyan['geoplugin_timezone']
                                  except KeyError:
                                         zonw = 'tidak ditemukan'
                                  try:
                                      benu= sabyan['geoplugin_continentName']
                                  except KeyError:
                                         benu='tidak ditemukan'
                                  try:
                                      ll = sabyan['loc']
                                  except KeyError:
                                         ll = "tidak ditemukan"
                     print "kota : %s "%(serv.kota) 
                     print "kode negara {} ".format(serv.koden)
                     print "wilayah : {} ".format(serv.wila)
                     print("hostname : {} ".format(serv.host))
                     print("poustal : {} ".format(serv.poustal))
                     print('company : %s '%(serv.com))
                     print "zona waktu {} ".format(serv.zonw)
                     print("benua : {} ".format(serv.benu))
                     print("kordinat : {} ".format(serv.ll))

#bagian jika ip < 5 ga berfungsi entah knpa aoakooao 
#Jika Kalian Nemuin Solved Nya Kabarin w instagram : ardho_ainullah

        elif api == 'serv3':
                url="https://ipapi.co/"+ip+"/json"
                if ip < 5:
                   print("\n[!] Enter a correct IP address \n")
                   sys.exit()
                else:
                      sabyan = json.loads(requests.get(url).text)
                      print("[*] with https://ipapi.co/ ")
                      time.sleep(3)
                      class serv:
                            try:
                                 print("Kota : %s "%(sabyan['city']))
                                 print("Kode Negara : %s "%(sabyan['country']))
                                 print("Negara : %s "%(sabyan['country_name']))
                                 print("bahasa : {} ".format(sabyan['languages']))
                                 print("utc offset : {} ".format(sabyan['utc_offset']))
                                 print("perusahaan : {} ".format(sabyan['org']))
                                 print("kode no telpon : {} ".format(sabyan['country_calling_code']))
                                 print("benua : {} ".format(sabyan['continent_code']))
                                 print("mata uang : {} ".format(sabyan['currency']))
                                 print("postal : {} ".format(sabyan["postal"]))
                                 print("Wilayah : %s "%(sabyan['region']))
                                 print("Zona Waktu : %s "%(sabyan['timezone']))
                                 print("ASN : %s "%(sabyan['asn']))
                                 print("Latitude : %s "%(sabyan['latitude']))
                                 print("Longitude : %s "%(sabyan['longitude']))
                            except KeyError:
                                   print "\n[*] ip address not found \n"
                                   sys.exit()

#bagian jika ip < 5 ga berfungsi entah knpa aoakooao
#Jika Kalian Nemuin Solved Nya Kabarin w instagram : ardho_ainullah

        elif api == 'serv4':
                url="https://geoip-db.com/json/"+ip
                if ip < 5:
                   print "\n[[!] Enter a correct IP address\n"
                   sys.exit()
                else:
                     sabyan = json.loads(requests.get(url).text)
                     print "[*] with https://geoip-db.com/ \n"
                     time.sleep(3)
                     class serv:
                           try:
                               print("%s Tipe IPv4"%(sabyan["IPv4"]))
                               print("State : {} ".format(sabyan['state']))
                               print("Kota : %s "%(sabyan['city']))
                               print("Kode Negara : %s "%(sabyan['country_code']))
                               print("Negara : %s "%(sabyan['country_name']))
                               print("Wilayah : %s "%(sabyan['state']))
                               print("Latitude : %s "%(sabyan['latitude']))
                               print("Longitude : %s \n"%(sabyan['longitude']))
	        	       sys.exit()
                           except KeyError:
                                  print "\n[*] ip address not found \n"
                                  sys.exit()
        else:
             k2("\n%s[!] %sto use %s: %spython2 sabyan.py %s--help %sor %s-h\n"%(m,h,w,c,h,m,h))
    
server(args.ip,args.url)
