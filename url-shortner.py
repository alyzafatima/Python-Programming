from tkinter import *
import pyshorteners

root = Tk()
root.geometry('250x250')
root.configure(bg="gray")
root.title("Url-Sortner")



def shorten():
    shortner = pyshorteners.Shortener()
    S_url=shortner.tinyurl.short("https://www.youtube.com/watch?v=NvzIGaEOKCk&list=PLs3IFJPw3G9IiHm9PEP1UaMtuvACmxVMj&index=2")
    print (short_url_entry.insert(0,S_url))

long_url= Label(root, text="Enter long url" , bg="gray")
long_url_entry= Entry(root)
long_url.pack(pady=10)
long_url_entry.pack()


short_url=Label(root, text="Your Short Url" , bg="gray")
short_url_entry=Entry(root)
short_url.pack(pady=5)
short_url_entry.pack()
submit_button=Button(root, text="Submit", command=shorten)
submit_button.pack(pady=15)
root.mainloop()