#Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.

import vlc

player = vlc.MediaPlayer("C:\Users\meiry\PycharmProjects\cursoEmVideo\Luiz_Gonzaga.mp3")
player.play()
