import json
import os
import pymongo
from types import EllipsisType
from flask import Flask, jsonify, json, url_for, request, render_template
from flask_pymongo import PyMongo
from datetime import datetime


app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/technica_2022-HomeBuyerInfo'
mongo = PyMongo(app)
db = mongo.db

# 'login' page
@app.route('/')
def askInput():
    return render_template('askinput.html')

# home guider dashboard
@app.route("/getdata", methods=['POST'])
def getdata():
    holder = list()
    currentCollection = mongo.db.scores

    for i in currentCollection.find():
        holder.append({'ID':i['ID'], 
                        'GrossMonthlyIncome' : i['GrossMonthlyIncome'],
                        'CreditCardPayment' : i['CreditCardPayment'],
                        'CarPayment' : i['CarPayment'], 
                        'StudentLoanPayments' : i['StudentLoanPayments'], 
                        'AppraisedValue' : i['AppraisedValue'], 
                        'DownPayment' : i['DownPayment'], 
                        'LoanAmount' : i['LoanAmount'], 
                        'MonthlyMortgagePayment' : i['MonthlyMortgagePayment'],
                        'CreditScore' : i['CreditScore']})

    pay = request.form['id']

    for i in holder:
        if i['ID'] == int(pay):
            ID_num = i['ID'];
            GrossMonthlyIncome = i['GrossMonthlyIncome'];
            CreditCardPayment = i['CreditCardPayment'];
            CarPayment = i['CarPayment'];
            StudentLoanPayments = i['StudentLoanPayments'];
            AppraisedValue = i['AppraisedValue'];
            DownPayment = i['DownPayment'];
            LoanAmount = i['LoanAmount'];
            MonthlyMortgagePayment = i['MonthlyMortgagePayment']
            CreditScore= i['CreditScore']

    #data dict to push to front end 
    #CreditScore
    LTV = (AppraisedValue - DownPayment)/AppraisedValue;
    DTI = (CreditCardPayment + CarPayment + StudentLoanPayments + MonthlyMortgagePayment) / GrossMonthlyIncome
    FEDTI = MonthlyMortgagePayment/GrossMonthlyIncome 
    
    data = {'CreditScore': CreditScore, 'LTV': LTV, 'DTI': DTI , 'FEDTI': FEDTI}
    userInfo = {'ID': ID_num, 'AppraisedValue':AppraisedValue, 'DownPayment':DownPayment, 'LoanAmount':LoanAmount, 'MonthlyMortgagePayment':MonthlyMortgagePayment}

    dateTimeObj = datetime.now()
    date_num = dateTimeObj.strftime("%d %b %Y")

    return render_template('index.html', data=data, userInfo=userInfo, date_num=date_num )


if __name__ == '__main__':
    app.run(debug=True, port=8080)