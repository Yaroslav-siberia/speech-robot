import sys
import os
import pydub
#Модуль для удобной работой со звуком формата WAV
import wave

"""
Модуль отвечает за конвертацию аудиофайла mp3 формата в wav, с сохранением wav файла.
Так как наш распознаватель настроен на работу с моно mp3, добавила конвертацию из стерео в моно.
"""
"""
Принимает: строку - путь к исходному mp3 файл
Возвращает: строку - путь к конвертированному wav файлу
"""

def conv_mp3_to_wav(mp3:str)->str:
	str_mp3 = mp3
	str_wav = str_mp3.replace('mp3','wav')
	sound = pydub.AudioSegment.from_mp3(str_mp3)
    #sound.export(str_wav, format="wav")
	wav = sound.export(str_wav, format="wav")

	#открывает файл в формате wav
	wf = wave.open(str_wav, "rb")

	#перевод из стерео в моно
	if wf.getnchannels() != 1:
	   wf.close()
	   sound_new = pydub.AudioSegment.from_wav(str_wav)
	   sound_new = sound_new.set_channels(1)
	   os.remove(str_wav)
	   sound_new.export(str_wav, format="wav")
	   wf = wave.open(str_wav, "rb")

	wf.close()
	return str_wav
