from kaldi_recognition.recognition import recognition
import sys
from utils.semantic import check_answer_type


audio = sys.argv[1]
answer_type = check_answer_type(recognition(audio))
print(answer_type)




	
