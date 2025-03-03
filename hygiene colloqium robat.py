import json
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='./static')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/add_qa', methods=['POST'])
def add_qa():
    q = request.form.get('question')
    a = request.form.get('answer')
    if q and a:
        d[q] = a
        save_to_json()
        return jsonify(message=f"Вопрос '{q}' и ответ '{a}' успешно добавлены!")
    else:
        return jsonify(message="Пожалуйста, введите вопрос и ответ.")

@app.route('/show_data', methods=['GET'])
def show_data():
    return jsonify(d)

def save_to_json():
    with open('src/data.json', 'w', encoding='utf-8') as file:
        json.dump(d, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app.run(debug=True)
    
