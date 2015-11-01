import time
import webbrowser

i = 0

print "This program started on " + time.ctime()
while i < 3:
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    i = i + 1

print "This program ended on " + time.ctime()
