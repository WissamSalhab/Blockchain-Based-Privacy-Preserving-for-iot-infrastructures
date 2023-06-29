def DownloadYoutubeVid(link,SAVE_PATH = "D:\Hajer\Scrapper\ytVideos"    ):
    from pytube import YouTube 
    try: 
        # object creation using YouTube
        # which was imported in the beginning 
        yt = YouTube(link) 
    except: 
        print("Connection Error") #to handle exception 
    try:
        did=False
        a=yt.streams.filter(res="1080p")
        if list(a)==[]:
            a=yt.streams.filter(res="720p")
            if list(a)!=[]:
                a.first().download(output_path = SAVE_PATH, filename = yt.title)
                did=True
        else:
            a.first().download(output_path = SAVE_PATH, filename = yt.title)
            did=True    
        if not(did)&(list(yt.streams)!=[]):
            yt.streams.first().download(SAVE_PATH, filename = yt.title)
    except:
        print("Some Error!")
    #os.rename(yt.streams.first().default_filename, 'new_filename.ext')

def getlinks(csvpath="D:\Hajer\Scrapper\ml-youtube.csv"):
    import csv
    links=[]
    with open(csvpath, mode='r',encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
                continue
            #print(f'\t{row[0]} ---- {row[1]} ---- {row[2]}.')
            link="https://www.youtube.com/watch?v="+row[0]
            links.append(link)
            line_count += 1
        print(f'Processed {line_count} lines.')
    return links

DownloadYoutubeVid("https://www.youtube.com/watch?v=Q5s_HCPdD6E")
#links=getlinks(csvpath="D:\Hajer\Scrapper\ml-youtube.csv")
# for link in links:
#     DownloadYoutubeVid(link)
