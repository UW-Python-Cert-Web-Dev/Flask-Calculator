from datetime import datetime
import os

from flask import Flask, render_template, request, redirect, url_for, session

from model import SavedTotal

app = Flask(__name__)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        number = int(request.form['number'])

        if 'total' not in session:
            session['total'] = 0

        session['total'] += number
        pass

    return render_template('add.jinja2', tasks=Task.select())


@app.route('/retrieve')
def retrieve():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        user = User.select().where(User.name == session['username']).get()

        Task.update(performed=datetime.now(), performed_by=user)\
            .where(Task.id == request.form['task_id'])\
            .execute()

    return render_template('retrieve.jinja2', tasks=Task.select().where(Task.performed.is_null()))


@app.route('/save', methods=['GET', 'POST'])
def save():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        task = Task(name=request.form['name'])
        task.save()

        return redirect(url_for('all_tasks'))
    else:
        return render_template('create.jinja2')



app.secret_key = b'\x9d\xb1u\x08%\xe0\xd0p\x9bEL\xf8JC\xa3\xf4J(hAh\xa4\xcdw\x12S*,u\xec\xb8\xb8'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
