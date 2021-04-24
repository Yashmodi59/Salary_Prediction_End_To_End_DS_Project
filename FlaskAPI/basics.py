from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    return render_template('after.html',data = 0)
    # rating = request.form['rate']
    # noc = request.form['competitors']
    # hourly = 0
    # employer_provided=0
    # same_state = request.form['same_state']
    # age = request.form['age']
    # skill1 = request.form['skill1']
    # skill2 = request.form['skill2']
    # skill3 = request.form['skill3']
    # skill4 = request.form['skill4']
    # desc_len = 3788.521505
    # size1 = request.form['size1']
    # size2 = request.form['size2']
    # size3 = request.form['size3']
    # size4 = request.form['size4']
    # size5 = request.form['size5']
    # size6 = request.form['size6']
    # size7 = request.form['size7']
    # size8 = request.form['size8']
    # size9 = request.form['size9']
    # too = request.form['Too']
    # IND = request.form['IND']
    # sector = request.form['sector']
    # revenue = request.form['revenue']
    # job_state = request.form['job_state']
    # job_simple = request.form['job_simple']
    # seniority = request.form['seniority']
    # print(seniority)
    # ll= [rating,noc,hourly,employer_provided,same_state,age,skill1,skill2,skill3,skill4,desc_len,size1,size2,size3,size4,size5,size6,size7,size8,too,IND,sector,revenue,job_state,job_simple,seniority]
    # return render_template('after.html')

if __name__ == "__main__":
    app.run(debug=True)