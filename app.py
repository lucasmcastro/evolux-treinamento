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


@app.route("/jobs/<job_id>/update", methods=['POST'])
def update_job(job_id):
    job = mongo.db.jobs.find_one({'_id': ObjectId(job_id)})
    job.update(request.form.to_dict())
    mongo.db.jobs.save(job)
    return redirect('/')


@app.route("/jobs/<job_id>/delete")
def delete_job(job_id):
    mongo.db.jobs.remove({'_id': ObjectId(job_id)})
    return redirect('/')

if __name__ == "__main__":
        app.run(debug=True)
