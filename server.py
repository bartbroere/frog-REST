import itertools
import json

from frog import Frog, FrogOptions
from flask import Flask, request

frog = Frog(FrogOptions())
app = Flask(__name__)


@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        return json.dumps(frog.process(request.form.get('document')))
    else:
        return 'Perform a POST request with a sentence parameter to get the FROG-tokenized and annotated sentence back'


@app.route('/organisations', methods=['GET', 'POST'])
def organisations():
    organisations = []
    if request.method == 'POST':
        processed_document = frog.process(request.form.get('document'))
        for is_organisation, organisation in itertools.groupby(processed_document,
                                                               key=lambda x: x['ner'].endswith('ORG')):
            if is_organisation:
                organisations.append(" ".join(x['text'] for x in organisation))
        return json.dumps(organisations)


@app.route('/persons', methods=['GET', 'POST'])
def persons():
    persons = []
    if request.method == 'POST':
        processed_document = frog.process(request.form.get('document'))
        for is_person, person in itertools.groupby(processed_document,
                                                   key=lambda x: x['ner'].endswith('-PER')):
            if is_person:
                persons.append(" ".join(x['text'] for x in person))
        return json.dumps(persons)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
