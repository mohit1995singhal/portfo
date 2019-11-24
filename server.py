from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home_page():
  return render_template('index.html')


@app.route('/<string:page_name>')
def remaining_page(page_name):
  return render_template(page_name)


@app.route('/contact_server', methods=['POST', 'GET'])
def contact_server():
  if request.method == 'POST':
    try:
      data = request.form.to_dict()
      print(data)
      write_to_contact_csv(data)
      return redirect('/thanks.html')
    except:
      return 'did not save to database'
  else:
    return 'something went wrong Try again!'


def write_to_contact_csv(data):
  with open('./dataBase/database.csv', mode='a')as database2:
    email = data['Email_Id']
    subject = data['Subject']
    message = data['Message']
    csv_writer = csv.writer(database2, delimiter=",", quotechar="", quoting=csv.QUOTE_NONE)
    csv_writer.writerow([email, subject, message])


@app.route('/signup_server', methods=['POST', 'GET'])
def signup_server():
  if request.method == 'POST':
    try:
      data = request.form.to_dict()
      return redirect('/login.html')
      userdatabase_csv(data)
    except:
      return 'did not save to database'
  else:
    return 'something went wrong Try again!'


def userdatabase_csv(data):
  with open('./dataBase/userdatabase.csv', newline="", mode='a')as database3:
    name = data['name']
    email = data['email']
    password = data['password']
    csv_writer = csv.writer(database3, delimiter=",", quotechar="", quoting=csv.QUOTE_NONE)
    csv_writer.writerow([name, email, password])


if __name__ == "__main__":
  app.run(debug=True)
