from datetime import datetime
from datetime import date
import time, os, sys, pytz

def getCurrentTime():
	today = date.today()
	tanggal = today.strftime("%d/%m/%Y")
	tz_ID = pytz.timezone('Asia/Makassar')
	datetime_MK = datetime.now(tz_ID)
	waktu = datetime_MK.strftime("%H:%M:%S")
	result = tanggal + " " + waktu
	return result

def backup():
	os.system("git add .")
	os.system('git commit -a -m "%s"' % (getCurrentTime()))
	os.system("git push -u origin master")

while (True):
	backup()
	time.sleep(12)
