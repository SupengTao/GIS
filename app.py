from flask import Flask, render_template, request, jsonify
from neo_db.query_graph import query, get_KGQA_answer

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')


@app.route('/KGQA', methods=['GET', 'POST'])
def KGQA():
    return render_template('KGQA.html')


@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    name = request.args.get('name')
    option = request.args.get('option')
    print(str(name))
    print(int(option))
    json_data = query(str(name), int(option))
    print(json_data)
    return jsonify(json_data)

@app.route('/KGQA_answer', methods=['GET', 'POST'])
def KGQA_answer():
    question = request.args.get('name')
    print('question:{}\n\n\n'.format(question))
    json_data = get_KGQA_answer(str(question))
    return jsonify(json_data)

@app.route('/get_all_relation', methods=['GET', 'POST'])
def get_all_relation():
    return render_template('all_relation.html')


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port=5004)
