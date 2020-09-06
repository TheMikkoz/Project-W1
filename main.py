import os
import youtube_dl
import tkinter as tk

root = tk.Tk()
root.title("Youtube downloader")

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def geturl():
    downloadMP4(userInput.get())

def downloadMP4(url):
    try:
        with ydl:
            result = ydl.extract_info(
                url,
                download=True
            )

        done()
    except:
        error()

def error():
    popup = tk.Tk()
    popup.wm_title("ERROR")
    label = tk.Label(popup, text=("Url: " + userInput.get() + " was not valid")).grid(row=1)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy).grid(row=2)
    popup.mainloop()

def done():
    popup = tk.Tk()
    popup.wm_title("Done")
    label = tk.Label(popup, text="Downloaded successfully").grid(row=1)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy).grid(row=2)
    popup.mainloop()

tk.Label(root, text="Url: ").grid(row=0)
userInput = tk.Entry(root, width=100)
userInput.grid(row=0, column=1)

tk.Button(root, text="Download", command=geturl).grid(row = 2)

root.mainloop()