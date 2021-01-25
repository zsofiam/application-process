from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    mentor_city = request.args.get('mentor-city')

    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif mentor_city:
        mentor_details = data_manager.get_mentors_by_city(mentor_city)
    else:
        mentor_details = data_manager.get_mentors()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template('mentors.html', mentors=mentor_details)


@app.route("/applicants-phone")
def get_applicant_data_by_name():
    if request.args["applicant-name"]:
        applicant_name = request.args["applicant-name"]
        print(applicant_name)
        applicants_details = data_manager.get_applicant_by_name(applicant_name)
        print(applicants_details)
        return render_template('applicants_phone.html', applicants=applicants_details)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
