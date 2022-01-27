import sys
import wave
import shutil
import os

from .convert import conv_mp3_to_wav
from .recognize import recognize
from .infile import save_in_file
from .downsample import reset_sample
from .merge import merge



def sample_check(path: str):
	sample_list = [8000, 16000, 32000, 48000]
	wf = wave.open(path, "rb")
	sample = wf.getframerate()
	wf.close()
	tmp = sample
	new_sample = 0

	#Если частота не подходит для передачи в следующий модуль, то она изменяется на ближаюшую
	if sample not in sample_list:
		for i in sample_list:
			if abs(sample-i) < tmp:
				new_sample = i
				tmp = abs(sample-i)
				
		reset_sample(path,new_sample)
	

def recognition(path: str):
	audio_mp3 = path
	name = audio_mp3.split('/')[-1]
	#name = name.replace('.mp3','')
	audio_wav = conv_mp3_to_wav(str(audio_mp3))
	result = recognize(str(audio_wav))
	return result










	
