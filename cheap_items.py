import time
import requests
from plyer import notification
import json
from playsound import playsound
key = "YOUR TORN API KEY"
item_number = 206
url = 'https://api.torn.com/market/%s?selections=itemmarket&key=%s'%(item_number ,key )
price_wanted = 8750000
item_name = "xanax"
def notificatio():
	notification.notify(
	title = "CHEAP" + item_name,
	message='https://www.torn.com/imarket.php#/p=shop&type=%s'%(item_number),
	timeout=5)
	playsound("../home/torn/Downloads/beep-02.mp3")

while True:
	print("should be sleeping")
	time.sleep(60)
	print("should have been about 15 sec")
	json_list = json.loads(requests.get(url).text)
	for i in json_list["itemmarket"]:
		if i["cost"] <  price_wanted:
			notificatio()
