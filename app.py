# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)

# Main
def picked_up():
    messages = [
        "こんにちは、あなたの名前を入力してください",
        "やあ！お名前は何ですか？",
        "あなたの名前を教えてね"
    ]
    return np.random.choice(messages)

# Routing
@app.route('/')
def index():
    title = "ようこそ！"
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)

@app.route('/post', methods=['POST', 'GET'])
def post():
    title = "こんにちは！"
    rev_word = "TEST"

    #TEST
    from google.cloud import storage as gcs
    import pandas as pd

    bucket_name = 'ml_bucket_01'
    #fname = 'wiki_tohoku.model'
    fname = 'sample.txt'
    project_name = 'My First Project'

    #プロジェクト名を指定してclientを作成
    client = gcs.Client(project_name)

    #バケット名を指定してbucketを取得
    bucket = client.get_bucket(bucket_name)

    #Blobを作成
    blob = gcs.Blob(fname, bucket)
    content = blob.download_as_string()

    rev_word = content
    #TEST
    
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html',
                               name=name, title=title,rev_word=rev_word)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
