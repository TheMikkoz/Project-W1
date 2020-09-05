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
    except:
        pass

tk.Label(root, text="Url: ").grid(row=0)
userInput = tk.Entry(root, width=100)
userInput.grid(row=0, column=1)

tk.Button(root, text="Download", command=geturl).grid(row = 2)

root.mainloop()