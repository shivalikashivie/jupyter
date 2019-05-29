import sys
import time
import webbrowser

data = sys.argv[1:]

print(data)

for i in data:
	print(i)
	time.sleep(2)
	webbrowser.open_new_tab("https://www.google.com/search?q="+i)

