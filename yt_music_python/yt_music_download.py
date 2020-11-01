# !pip install pytube
# !python -m pip install git+https://github.com/nficano/pytube
# !pip install moviepy

# Importações
import os
import pytube as pt
import moviepy.editor as mp

# Download
url = str(input('URL: '))
stream = pt.YouTube(url = url).streams.get_audio_only()
stream.download('mp4')
title = str(stream.title)

# Conversão
clip = mp.AudioFileClip('mp4\\' + title + '.mp4')
clip.write_audiofile('mp3\\' + title + '.mp3')

# Deletar mp4
delete = str(input('Deletar mp4? (S/N): '))
if delete in 'Ss':
    os.remove('mp4\\' + title + '.mp4')
    print(".mp4 deletado!")
else:
    print(".mp4 não deletado!")
