from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

tasks = []
completed_tasks = []


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html", tasks=tasks, completed_tasks=completed_tasks)


@app.route("/add", methods=["POST"])
def add_task():
    new_task = request.form.get("task")
    if new_task:
        tasks.append(new_task)
    return redirect(url_for("home"))


@app.route("/mark_as_done", methods=["POST"])
def mark_as_done():
    task = request.form.get("task")
    if task in tasks:
        tasks.remove(task)
        completed_tasks.append(task)
    return redirect(url_for("home"))


@app.route("/remove_task", methods=["POST"])
def remove_task():
    task = request.form.get("task")
    if task in tasks:
        tasks.remove(task)
    return redirect(url_for("home"))


@app.route("/remove_completed", methods=["POST"])
def remove_completed():
    task = request.form.get("task")
    if task in completed_tasks:
        completed_tasks.remove(task)
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
