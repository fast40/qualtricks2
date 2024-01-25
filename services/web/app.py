from flask import Flask, Response, request, render_template, redirect, abort
from helpers import url_bool
import datasets
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongo:27017/qualtricks'

client = PyMongo(app).cx


@app.route('/')
def index():
    return render_template('index.html', datasets=list(datasets.get(client)))


@app.route('/get_file')
def get_file():
    dataset_id = request.args.get('dataset_id')
    response_id = request.args.get('response_id')
    loop_number = request.args.get('loop_number', type=int)
    should_redirect = request.args.get('redirect', type=url_bool)

    if None in (dataset_id, loop_number, response_id, should_redirect):
        abort(400, 'The URL is missing required parameters and/or gives them invalid types.')

    path = datasets.get_path(dataset_id, str(loop_number), client)

    if should_redirect:
        return redirect(f'/file/{path.removeprefix("/")}')
    else:
        response = Response(path)
        response.headers['Access-Control-Allow-Origin'] = '*'

        return response


@app.route('/upload', methods=['POST'])
def upload():
    zip_file = request.files.get('zip_file')
    dataset_name = request.form.get('dataset_name')

    if None in (zip_file, dataset_name):
        abort(400, 'The request is missing required data fields.')
    
    datasets.create(dataset_name, zip_file, client)

    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
