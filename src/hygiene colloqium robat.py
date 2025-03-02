import json

print("hello students we want to play a game with you!")
print("as you are going to be ready for a Russian exam, i plan to make you speak in russian.\nfirst i ask you the questions. then you must be able to answer in the required format.")

# Функция для чтения данных из JSON-файла и загрузки их в словарь
def load_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}  # Возвращаем пустой словарь, если файл не найден

# Загружаем данные из JSON-файла в словарь
d = load_from_json('data.json')



def addqa(q,a):
    d[q]=a
    return d

def save_to_json():
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(d, file, ensure_ascii=False, indent=4)

while True:
 
 i=input("next or break or show : ").lower()
 
 if i=="break":
     break
   
 elif i=="show":
     print(d)
 elif i=="next":   
    q=input("please write the question: ")
    a=input("please write the answer: ")
    addqa(q,a)
    save_to_json()
 else:
     print("undefined input!!")
    

    
