from vosk import Model, KaldiRecognizer
import os
import wave
import json

voskmodel_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "vosk-model")
#Обученная модель для русского языка
model = Model(voskmodel_path)
"""
Модуль, осуществляющий перевод аудиофрагмента в текст, посредством использования vosk-api, построенной на системе распознавания kaldi
Принимает: строку - путь к файлу ФОРМАТА WAV
Возвращает: результат перевода в JSON формате
"""
def recognize_file(str_wav:str):
	if not os.path.exists(voskmodel_path):
	    print ("Please download the model (vosk-model-ru-0.10.zip) from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
	    exit (1)
	wf = wave.open(str_wav, "rb")
	if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
	#getnchannels() -> Возвращает количество аудиоканалов ( 1для моно, 2для стерео)
	#getsampwidth() -> Возвращает ширину образца в байтах
	#getcomptype() -> Возвращает тип сжатия ( 'NONE'это единственный поддерживаемый тип)
	#то есть все эти проверки на то, что нам на самом деле подсунули нужный формат
	    print ("Audio file must be WAV format mono PCM.")
	    print(wf.getnchannels())
	    print(wf.getsampwidth())
	    print(wf.getcomptype())
	    exit (1)
	result = list()
	rec = KaldiRecognizer(model, wf.getframerate())	
	while True:
		data = wf.readframes(1000)
		if len(data) == 0:
			break
		if rec.AcceptWaveform(data):
			#вытаскиваю результат из строки в JSON формате

			jsonData = json.loads(rec.Result())
			result.append(jsonData)
	jsonData = json.loads(rec.FinalResult())
	#Проверка на пустоту
	if 'result' in jsonData:
		result.append(jsonData)
	wf.close()
	return result

def stop_recognizing(result):
	'''если прошло 3 паузы размером как паузы между предложениями то остановка
	result : list(dict)
	'''
	try:
		if result[-3]["text"] == "" and result[-2]["text"] == "" and result[-1]["text"] == "":
			return True
		else:
			return False
	except:
		return False

def recognize_stream(stream, rate = 16000):
	result = list()
	rec = KaldiRecognizer(model, rate)
	stream.start_stream()
	while True:
		# exception_on_overflow = False не сыпать исключения при переполнении буфера. исключения не сыпятся и без него
		# но как ни странно с ним будет меньше ошибок если несопадаютс частоты
		data = stream.read(16000, exception_on_overflow = False)
		if len(data) == 0:
			#stream.close()
			# данная остановка сработает если прекратится поток. то есть сработает переключатель который до этой функции
			break
		if rec.AcceptWaveform(data):
			jsonData = json.loads(rec.FinalResult())
			result.append(jsonData)

		#jsonData = json.loads(rec.FinalResult())
		#result.append(jsonData)

		# эта остановка срабатывает когда поток не прервался но человек на той стороне замолчал
		if len(result) > 1 and stop_recognizing(result):
			break
	return result