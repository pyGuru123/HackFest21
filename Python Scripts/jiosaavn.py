# pip install requests colorama wget
# API by https://github.com/sumitkolhe
# Script by https://github.com/gpri989

import requests
import subprocess
import sys
import wget
from colorama import Fore
import os

def main():
    print(Fore.GREEN + "\nJioSaavn Music Download Script by Priyanshu(@gpri989)")
    print("\nCredits to https://github.com/sumitkolhe for JioSaavn API")
    options = int(input("\n Enter 0 To Exit\n\n 1. With Song Name\n 2. With Song URL\n 3. With Album ID \n 4. With Album URL\n => "))
    if options == 0:
        exit()
    elif options == 1:
        download("song name", "search?song", 1)
    elif options == 2:
        download("song URL", "song?link", 2)
    elif options == 3:
        download("album ID", "album?id", 3)
    elif options == 4:
        download("album URL", "album?link", 4)
    else:
        print("\nEnter Valid Option\n")
def download(type1: str, type2: str, i: int):
        song_name = input("\nEnter the" +  " " + type1 + " " + ":\n => ")
        print(f"\nSearching for {song_name}\n")
        base_url = f"https://saavn.me/{type2}={song_name}"
        song_results = requests.get(url=base_url).json()
        index = 1
        songs = []
        final = []
        if i == 1:
            for result in song_results:
                print(index, ") ", result['song_name'], "(", result['album_name'], ")", "==>", result['song_artist'])
                index += 1
                songs.append(result['download_links'])
                final.append(result['song_name'] + " " + "By" + " " + result['song_artist'])
            if songs:
                try:
                    choice = int(input("\nEnter the index of the song which you want to download:\n => "))
                    song_link = songs[choice-1]
                    qchoice = int(input("\nQuality of Song\n 1. Low \n 2. Medium \n 3. High \n => "))
                    if qchoice  == 1:
                        n = 0
                    elif qchoice  == 2:
                        n = 1
                    elif qchoice  == 3:
                        n = 2
                    else:
                        print("\nEnter Valid Option!!\n")
                        print("Exiting..\n")
                        exit()
                    limnk = song_link[n]
                    print("\nDownloading :" + " " + final[choice-1] + "\n")
                    download = wget.download(limnk)
                    print("\n")    
                    final_song = final[choice-1]
                    final_song_name = f"{final_song}.m4a"
                    print("\n" + final_song_name + " " + "Downloaded Successfully \n")
                    os.rename(download, final_song_name)
                except IndexError:
                    print("\n Wrong Value! Exited..\n")
                    exit()
        elif i == 2:
            print("\n Found :" + " " + song_results['song_name'] + " " + "==>" + " " + song_results['song_artist'] + "\n")
            song_link = song_results['download_links']
            try:
                qchoice = int(input("\nQuality of Song\n 1. Low \n 2. Medium \n 3. High \n => "))
                if qchoice  == 1:
                    n = 0
                elif qchoice  == 2:
                    n = 1
                elif qchoice  == 3:
                    n = 2
                limnk = song_link[n]
                print("\nDownloading....\n")
                download = wget.download(limnk)
                final_song = (song_results['song_name'] + " " + "By" + " " + song_results['song_artist'])
                final_song_name = f"{final_song}.m4a"
                print("\n" + final_song_name + " " + "Downloaded Successfully \n")
                os.rename(download, final_song_name)
            except UnboundLocalError:
                    print("\n Wrong Value! Exited..\n")
                    exit()
        elif i == 3 or 4:
            for result in song_results['songs']:
                print(index, ") ", result['song_name'], "==>", result['song_artist'])
                index += 1
                songs.append(result['download_links'])
                final.append(result['song_name'] + " " + "By" + " " + result['song_artist'])
            if songs:
                try:
                    choice = int(input("\nEnter the index of the song which you want to download:\n => "))
                    song_link = songs[choice-1]
                    qchoice = int(input("\nQuality of Song\n 1. Low \n 2. Medium \n 3. High \n => "))
                    if qchoice  == 1:
                        n = 0
                    elif qchoice  == 2:
                        n = 1
                    elif qchoice  == 3:
                        n = 2
                    limnk = song_link[n]
                    print("\nDownloading :" + " " + final[choice-1] + "\n")
                    download = wget.download(limnk)
                    print("\n")    
                    final_song = final[choice-1]
                    final_song_name = f"{final_song}.m4a"
                    print("\n" + final_song_name + " " + "Downloaded Successfully \n")
                    os.rename(download, final_song_name)
                except IndexError:
                    print("\n Wrong Value! Exited..\n")
                    exit()
if __name__ == "__main__":
    main()
