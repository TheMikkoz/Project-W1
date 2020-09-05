import os
import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def downloadMP4(url):
    with ydl:
        result = ydl.extract_info(
            url,
            download=True
        )

if __name__ == "__main__":
    run = True
    while run:
        uInput = input()
        if uInput == "quit":
            quit()
        try:
            downloadMP4(uInput)
            clear()
            print("Downloaded successfully")
        except:
            print("!ERROR!")