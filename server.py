from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)


@app.route('/')
def home_page():
  return render_template('index.html')


@app.route('/<string:page_name>')
def remaining_page(page_name):
  return render_template(page_name)



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
      try:
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect('/thanks.html')
      except:
        return 'did not save to database'
    else:
      return 'something went wrong Try again!'



def write_to_text_file(data):
  with open('database.txt',mode='a')as database:
    email=data['Email_Id']
    subject=data['Subject']
    message=data['Message']
    file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
  with open('database.csv',mode='a')as database2:
    email=data['Email_Id']
    subject=data['Subject']
    message=data['Message']
    csv_writer = csv.writer(database2,delimiter=",",quotechar="",quoting=csv.QUOTE_NONE)
    csv_writer.writerow([email,subject,message])

if __name__=="__main__":
  app.run(debug=True)