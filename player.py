import pygame
import keyboard
import os
import pandas as pd
pygame.mixer.init()
s=0
n=0
result='neutral'
os.system('cls')
song_list=pd.read_csv('song list/'+result+'.csv')
emotion=(song_list.columns)[0]
artist=(song_list.columns)[1]
album=(song_list.columns)[2]
count=song_list[emotion].count()
while n==0:
    pygame.mixer.music.load('songs/'+song_list[emotion][s]+'.mp3')
    print('\t\t\t\t\t\t\t\t\t MONOSONIC')
    print('\t\t\t\t\t\t\tA MUSIC PLAYER TO PLAY SONGS FOR YOUR MOOD')
    print('\t\t\t\t\t\tLOOKS LIKE UR {} SO HERE ARE SOME SONGS FOR UR MOOD'.format(result.upper()))
    print('\n\n\t\t\t\t\t\t\tSong:'+song_list[emotion][s])
    print('\n\t\t\t\t\t\t\tArtist:'+song_list[artist][s])
    print('\n\t\t\t\t\t\t\tAlbum:'+song_list[album][s])
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\tPRESS THE KEY P TO PAUSE')
    print('\n\t\t\t\t\t\t\tPRESS THE KEY D TO PLAY NEXT TRACK')
    print('\n\t\t\t\t\t\t\tPRESS THE KEY A TO PLAY PREVIOUS TRACK')
    print('\n\t\t\t\t\t\t\tPRESS THE KEY X TO EXIT THE SOFTWARE')
    pygame.mixer.music.play()
    while True:
        if keyboard.is_pressed('p'):
            pygame.mixer.music.pause()
            os.system('cls')
            print('\t\t\t\t\t\t\t\t\t MONOSONIC')
            print('\t\t\t\t\t\t\tA MUSIC PLAYER TO PLAY SONGS FOR YOUR MOOD')
            print('\n\n\t\t\t\t\t\t\tSong:'+song_list[emotion][s])
            print('\n\t\t\t\t\t\t\tArtist:'+song_list[artist][s])
            print('\n\t\t\t\t\t\t\tAlbum:'+song_list[album][s])
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\tPRESS THE KEY R TO RESUME')
            print('\n\t\t\t\t\t\t\tPRESS THE KEY D TO PLAY NEXT TRACK')
            print('\n\t\t\t\t\t\t\tPRESS THE KEY A TO PLAY PREVIOUS TRACK')
            print('\n\t\t\t\t\t\t\tPRESS THE KEY X TO EXIT THE SOFTWARE')
        if keyboard.is_pressed('r'):
            pygame.mixer.music.unpause()
            os.system('cls')
            print('\t\t\t\t\t\t\t\t\t MONOSONIC')
            print('\t\t\t\t\t\t\tA MUSIC PLAYER TO PLAY SONGS FOR YOUR MOOD')
            print('\n\n\t\t\t\t\t\t\tSong:'+song_list[emotion][s])
            print('\n\t\t\t\t\t\t\tArtist:'+song_list[artist][s])
            print('\n\t\t\t\t\t\t\tAlbum:'+song_list[album][s])
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\tPRESS THE KEY P TO PAUSE')
            print('\n\t\t\t\t\t\t\tPRESS THE KEY D TO PLAY NEXT TRACK')
            print('\n\t\t\t\t\t\t\tPRESS THE KEY A TO PLAY PREVIOUS TRACK')
            print('\n\t\t\t\t\t\t\tPRESS THE KEY X TO EXIT THE SOFTWARE')
        if keyboard.is_pressed('d'):
            pygame.mixer.music.stop()
            os.system('cls')
            if s<count-1:
                s=s+1
            else:
                s=0
            break;
        if keyboard.is_pressed('a'):
            pygame.mixer.music.stop()
            os.system('cls')
            if s>0:
                s=s-1
            else:
                s=count-1
            break;
        if keyboard.is_pressed('x'):
            os.system('cls')
            pygame.mixer.music.stop()
            n=1
            break