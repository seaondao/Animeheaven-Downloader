import requests,csv
from GeteachEpisode import videos
from GeteachEpisode import Animename
chunk_size= 256 #mb each requests

# def readingCSV(filename):
#     array = []
#     with open((filename+".csv"),"r") as file:
#         data =csv.reader(file)
#         for item in data:
#             for x in item:
#                 if x:
#                     array.append(x)
#     return(array)


# futureURLS = readingCSV("test2")
# URLs= []

videos = videos


# Main part of Downloading

print(len(videos))
# num = 3

AnimeName = Animename

for i in range(len(videos)):#
    r = requests.get(videos[i]["src"],stream=True)#Keep sending me
    name = AnimeName + " " +videos[i]["episodeNum"]+".mp4"
    with open(name,"wb") as f:
        downloaded = 0
        count =0
        for chunk in r.iter_content(chunk_size=chunk_size):
            
            f.write(chunk)
            downloaded+=chunk_size
            count+=1
            #
            if count%6000 == 0:
                print(f"Downloaded :{round(downloaded/200000000*100)}%")
        print(name+": Done")

