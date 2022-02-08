from kaldi_recognition.recognition import file_recognition, stream_recognition
import sys
from utils.semantic import check_answer_type


'''audio = sys.argv[1]
#file_recognition(audio) список словарей, где в каждом словаре одно отдельное предложение[{"text": "да хорошо"}]
#
#
answer = file_recognition(audio)[0]['text']
answer_type = check_answer_type(answer)
print(answer_type)'''

from vosk import Model, KaldiRecognizer
import os
import pyaudio

model = Model(r"/home/ysiberia/Документы/GitHub/speech_robot/kaldi_recognition/vosk-model") # полный путь к модели

p = pyaudio.PyAudio()
stream1 = p.open(
        format=pyaudio.paInt32,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=16000
    )

#распознаем текст. запуск потока осуществляется внутри самой функции.
answer = stream_recognition(stream1)
# склеиваем текст в одну строку
answer = [x["text"] for x in answer]
answer = ' '.join(answer)
# определяем категорию ответа
answer_type = check_answer_type(answer)
print(answer_type)