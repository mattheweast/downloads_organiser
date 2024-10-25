from flask import Flask, redirect, render_template, request

import downloads, screenshots

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')

@app.post("/organise")
def organise():
    downloads.download_organiser()
    return redirect(request.referrer)

@app.post("/screenshot")
def screenshot():
    project_name = request.form.get('project_name')
    if project_name:
        screenshots.organise_screenshots(project_name)
        return redirect(request.referrer)
    else:
        return "Project Name is required.", 400

if __name__ == '__main__':
    app.run(debug=True)