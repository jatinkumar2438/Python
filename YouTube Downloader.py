from pytube import YouTube
i = "y"

print("")

while i == "yes" or i == "y":
    yt_link = input("Paste Link Here : ")
    yt = YouTube(yt_link)
    yr = yt.streams.get_highest_resolution()

    print("")

    print("Title : ",yt.title)
    print("Number of views : ",yt.views)
    print("Length of video : ",yt.length," seconds")
    print("Ratings : ",yt.rating,"/ 10")
    print("")
    print("Downloading...")
    yr.download()
    print("Downloaded")
    print("")

    i = input("Wanna Download More YouTube Videos (Yes/No) : ").casefold()
    print("")
    
print("Thank for using our application.")
print("Follow me on Instagram   @jatinkumar2438")