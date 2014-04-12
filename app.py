from flask import Flask, render_template, request, redirect
from flask.ext.pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask("jobs")
mongo = PyMongo(app)

@app.route("/")
def index():
    jobs = mongo.db.jobs.find()
    return render_template("index.html", jobs=jobs)


@app.route("/jobs/new")
def new_job():
    return render_template("new_job.html")


@app.route("/jobs/create", methods=['POST'])
def create_job():
    mongo.db.jobs.insert(request.form.to_dict())
    return redirect('/')


@app.route("/jobs/<job_id>/edit")
def edit_job(job_id):
    job = mongo.db.jobs.find_one({'_id': ObjectId(job_id)})
    return render_template("edit_job.html", job=job)


if __name__ == "__main__":
        app.run(debug=True)
