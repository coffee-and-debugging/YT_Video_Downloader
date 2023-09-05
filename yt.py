from pytube import YouTube
print('Program source: https://github.com/coffee-and-debugging\n')
link = input("Enter your link: ")

yt1 = YouTube(link)

print(yt1.title + "\n")

video = yt1.streams.filter(progressive=True)

vid = list(enumerate(video))

for i in vid:
    print(i)

strm = int(input("\nPlease choose your choice: "))

video[strm].download()

print("Download successful!")
