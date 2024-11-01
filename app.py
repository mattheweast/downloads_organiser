from flask import Flask, redirect, render_template, request, session, flash

import downloads, screenshots

app = Flask(__name__, static_folder='static')
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/')
def index():
    project_name = session.get('project_name')  # Get project name from session
    return render_template('index.html', project_name=project_name)

@app.post("/organise")
def organise():
    downloads.download_organiser()
    return redirect(request.referrer)

@app.post("/set_project_name")
def set_project_name():
    project_name = request.form.get('project_name')
    
    if project_name:
        session['project_name'] = project_name  # Save project name in session
        flash('Project name updated successfully!', 'success')  # Flash message for success
    else:
        flash('Project name cannot be empty!', 'error')  # Flash message for error
    
    return redirect('/')  # Redirect back to the index page

@app.post("/screenshot")
def screenshot():
    project_name = session.get('project_name')  # Retrieve project name from session
    
    if project_name:
        screenshots.organise_screenshots(project_name)
        return redirect(request.referrer)  # Redirect back after organizing
    else:
        flash('Project name must be set before organizing screenshots!', 'error')  # Flash error message
        return redirect('/')  # Redirect back to the index page

if __name__ == '__main__':
    app.run(debug=True)
