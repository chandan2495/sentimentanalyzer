from flask import Flask, jsonify, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/api/sentiment', methods=['POST'])
def sentiment():
    alltext=request.form['message']
    totalPolarities = 0.0
    numberoflines=0
    texts = alltext.split('.')
    for text in texts:
        polarity = TextBlob(text)
        polarities += polarity
        numberoflines+=1
    response = {'polarity': polarities/numberoflines, 'subjectivity' : text.subjectivity}
    return jsonify(response)

if __name__ == "__main__":
    app.run()
