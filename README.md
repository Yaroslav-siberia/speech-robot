# speech robot
 робот для автоматического распознавания ответов и определения ветки разговора.  
 На текущий момент данная версия работает с файлами, а не с потоковым аудио.  
 
В качестве движка  STT используется Kaldi с vosk-api.  
Модель vosk можно скачать с https://alphacephei.com/vosk/models.  
Архим с моделью распаковать в директорию kaldi_recognition/vosk-model.
 
 Определение ветки разговора или вернее "типа" ответа происходит с использованием библиотеки spacy.  
 Определение типа ответа происходит на основе семантического расстояния к типам/вариантам ответов.  
 Варианты ответов приведены в файле answers.json и сгруппированы по категориям.  
 Для большей точности определения семантической близости между ответами рукомендую использовать большую модель spacy ru_core_news_lg-3.2.0.
 
 Соответственно от полноты файла, содержащего варианты ответов, зависит точность работы данного этапа.

### [ Использование ]  
 Для запуска введите команду 'python3 main.py mp3/1.mp3'

## TO DO
 Добавить механизмы для обработки потокового звука
 Собрать самостоятельный модуль.



