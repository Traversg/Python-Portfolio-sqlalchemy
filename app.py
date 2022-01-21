import re
from flask import (render_template, redirect,
                   url_for, request)
from models import db, Project, app
import datetime


def str_to_datetime(str):
    date = datetime.datetime.strptime(str, '%Y-%m')
    return date


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def create():
    if request.form:
        new_project = Project(project_title=request.form['title'],
                              completion_date=str_to_datetime(
                                  request.form['date']),
                              description=request.form['desc'],
                              skills=request.form['skills'],
                              url=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/projects/<id>')
def detail(id):
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get_or_404(id)
    if request.form:
        project.project_title = request.form['title']
        project.completion_date = str_to_datetime(request.form['date'])
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.url = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editform.html', project=project)


@app.route('/projects/<id>/delete')
def delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
