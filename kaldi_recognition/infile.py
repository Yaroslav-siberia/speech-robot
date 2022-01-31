import json

def save_in_file(json_obj, path:str):
	f = open(path, 'w')
	#вытаскиваю результат из строки в JSON формате
	jsonData = json.loads(json_obj)

	for data in jsonData:
		#Проверка на пустоту
		if 'result' in data:
			part = data["result"]
			for i in part:
				print(i)
				f.write(str(i["start"]) + "/" + str(i["word"]) +"/"+str(i["end"])+" " )
		
	f.close()
