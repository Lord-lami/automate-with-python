import yt_dlp, pyperclip

video_url = pyperclip.paste()

with yt_dlp.YoutubeDL() as ydl:
    ydl.download([video_url])
