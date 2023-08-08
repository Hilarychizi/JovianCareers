from flask import Flask, jsonify, render_template, url_for, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app=Flask(__name__)

@app.route('/')
def index():
    jobs_list=load_jobs_from_db()
    return render_template('index.html',jobs=jobs_list)

@app.route("/jobs")
def list_jobs():

    return jsonify(load_jobs_from_db())

@app.route("/job/<id>")
def show_job(id):
    job=load_job_from_db(id)
    if not job:
        return "Not found", 404
    
    return render_template('jobpage.html',job=job)
@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    data=request.form
    job=load_job_from_db(id)
    add_application_to_db(id, data)
    return render_template('application_submitted.html',application=data, job=job)


if __name__== "__main__":
    app.run(debug=True)