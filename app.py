from flask import Flask, redirect, render_template, request

import downloads

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')

@app.post("/organise")
def organise():
    downloads.download_organiser()
    return redirect(request.referrer)

if __name__ == '__main__':
    app.run(debug=True)