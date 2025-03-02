from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__, template_folder='', static_folder='./static')

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        q = request.form.get('question')
        a = request.form.get('answer')
        if q and a:
            d[q] = a
            save_to_json()
            return jsonify(message=f"Вопрос '{q}' и ответ '{a}' успешно добавлены!")
        else:
            return jsonify(message="Пожалуйста, введите вопрос и ответ.")
    return render_template('index.html', data=d)

def save_to_json():
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(d, file, ensure_ascii=False, indent=4)

@app.route('/show', methods=['GET'])
def show_data():
    return jsonify(d)

if __name__ == '__main__':
    app.run(debug=True)

    
