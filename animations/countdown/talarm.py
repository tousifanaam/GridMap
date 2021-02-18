import threading
from datetime import datetime
from time import sleep
from os import system, sys, name
from playsound import playsound
from countdown import countdown
from gridmap import GridMap as gm

try:
    if len(sys.argv) != 2:
        raise TypeError(
            "missing 1 required positional argument.\nFor 24 hour format:\n\t[(hour):(minute)]\nFor 12 hour format:\n\t[(hour):(minute):(AM/PM)]") from None
    else:
        sysvar = sys.argv[1].split(":")
        format_12 = False
        if len(sysvar) == 3 and (sysvar[2].lower() == "am" or sysvar[2].lower() == "pm"):
            format_12 = True
except TypeError as e:
    print(f"{e.__class__.__name__}: {e}")
    exit()

# load
def conv24(time):
	"""
	Converts 12HR clock to 24HR clock
	time should be either 
	('hh:mm:am' or 'hh:mm:pm') or ('hh:mm:AM' or 'hh:mm:PM')
	"""
	l = list(time)
	l[2] = l[2].upper()
	if int(l[0]) > 12 or int(l[0]) < 1:
		raise ValueError(f"{l[0]}. is not a valid hour value - 0 < hour <= 12")
	if int(l[1]) > 60 or int(l[1]) < 0:
		raise ValueError(f"{l[1]}. is not a valid minute value - 0 < minute <= 12")
	if 'PM' in l[2]:
		v = int(l[0])
		if v < 12 and v > 0:
			v += 12
			l[0] = str(v)
		l[2] = l[2].strip('PM')
	elif 'AM' in l[2]:
		v = int(l[0])
		if v == 12:
			l[0] = '00'
		l[2] = l[2].strip('AM')
	res = ''
	for i in l:
		res += i + ":"
	return res.rstrip(':')

if format_12:
    sysvar = str(conv24(sysvar)).split(":")
h = int(sysvar[0])
if h > 23 or h < 0:
    raise ValueError(
        f"{sysvar[0]}. is not a valid hour value - 0 <= hour < 24")
m = int(sysvar[1])
if m > 59 or h < 0:
    raise ValueError(
        f"{sysvar[1]}. is not a valid minute value - 0 <= minute < 60")

end_at = (h, m)
current_time = tuple([int(i) for i in tuple(
    str(datetime.now()).split(" ")[1].split(".")[0].split(":"))])
if end_at == current_time[:2] and current_time[2] != 0:
    print("talarm: Time reached already!")
    exit()
# GridMap objects
zero = gm.zero()
one = gm.one()
two = gm.two()
three = gm.three()
four = gm.four()
five = gm.five()
six = gm.six()
seven = gm.seven()
eight = gm.eight()
nine = gm.nine()

# object mapping
grid_dict = {
    "0": zero,
    "1": one,
    "2": two,
    "3": three,
    "4": four,
    "5": five,
    "6": six,
    "7": seven,
    "8": eight,
    "9": nine,
}

def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

col_plot = [(1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5),
            (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10)]
col = gm(14, 4, col_plot, lines=True)
now = tuple(str(datetime.now()).split(" ")[1].split(".")[0].split(":"))
hour = 0
while True:
    def display():
        globals()['var'] = tuple(str(datetime.now()).split(
            " ")[1].split(".")[0].split(":"))
        h = var[0]
        m = var[1]
        s = var[2]
        hms_grid_obj = gm.merge(gm.merge(gm.merge(gm.merge(grid_dict[h[0]], grid_dict[h[1]]), col), gm.merge(
            gm.merge(grid_dict[m[0]], grid_dict[m[1]]), col)), gm.merge(grid_dict[s[0]], grid_dict[s[1]]))
        print(hms_grid_obj.grid_without_lines())
    t = threading.Thread(target=display)
    t.start()
    #print(f"\n[*] Points: {len(hms_grid_obj.scat_plot)}")
    sleep(1)
    clear()
    # check
    end_at = (h, m)
    if int(var[0]) <= end_at[0]:
        v = int(var[0]) - int(now[0])
        if v > hour:
            hour += 1
            playsound('dash.wav')
    else:
        v = int(var[0]) - int(now[0])
        if v < hour:
            hour += 1
            playsound('dash.wav')
    if int(var[0]) == end_at[0] and int(var[1]) == end_at[1] - 1 and int(var[2]) >= 49:
        break

countdown()
playsound('sos.wav')
sleep(1.5)
clear()
