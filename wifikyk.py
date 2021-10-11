import requests
from bs4 import BeautifulSoup


r = requests.get("https://wifi.gsb.gov.tr/")

content = BeautifulSoup(r.content , "html.parser")

lbl = content.find("label" , attrs = {"id":"j_idt51:j_idt106:0:j_idt128"})

kalan = float(str(lbl.text))
print("KALAN :" , float("%.2f" % (kalan/1024)) , "GB ")
