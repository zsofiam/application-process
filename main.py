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


@app.route('/applicants')
def applicants_list():
    applicants_list = data_manager.get_applicants()
    return render_template('applicants.html', applicants=applicants_list)


@app.route('/applicant/<code>', methods=['GET', 'POST'])
def applicant_details(code):
    if request.method == 'POST':
        new_phone = request.form["new-phone"]
        data_manager.update_applicant_phone(new_phone, code)
    applicant_details = data_manager.get_applicant_by_code(code)
    return render_template('applicant.html', applicant = applicant_details)


@app.route('/applicants/<code>/delete', methods=['POST'])
def delete_applicant(code):
    if request.method == 'POST':
        data_manager.delete_applicant_by_code(code)
    return redirect('/applicants')


@app.route('/delete-applicant', methods=["POST"])
def delete_applicant_by_email_ending():
    if "email-ending" in request.form.keys() and request.form["email-ending"]:
        applicant_email_ending = request.form["email-ending"]
        data_manager.delete_applicant_by_email_ending(applicant_email_ending)
    return redirect('/applicants')


@app.route("/applicants-phone")
def get_applicant_data_by_name():
    if "email-ending" in request.args.keys() and request.args["email-ending"]:
        applicant_email_ending = request.args["email-ending"]
        applicants_details = data_manager.get_applicant_data_by_email_ending(applicant_email_ending)
        return render_template('applicants_phone.html', applicants=applicants_details)
    if "applicant-name" in request.args.keys() and request.args["applicant-name"]:
        applicant_name = request.args["applicant-name"]
        applicants_details = data_manager.get_applicant_by_name(applicant_name)
        return render_template('applicants_phone.html', applicants=applicants_details)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
