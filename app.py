from flask import Flask, render_template, request, redirect
from flask.ext.pymongo import PyMongo

app = Flask("jobs")
mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/jobs/new")
def new_job():
    return render_template("new_job.html")


@app.route("/jobs/create", methods=['POST'])
def create_job():
    mongo.db.jobs.insert(request.form.to_dict())
    return redirect('/jobs/new')

if __name__ == "__main__":
        app.run(debug=True)
