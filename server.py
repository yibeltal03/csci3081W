from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

totalCal = 0
transactions = []  

@app.route('/cal/getTotalCal',methods = ['GET'])
def getTotalCal():
   return jsonify({"Total Calories":totalCal})

@app.route('/cal/getMealLog',methods = ['GET'])
def getMealLog():
   return jsonify(transactions)

@app.route('/cal/getProtien',methods = ['GET'])
def getProtien():
   return jsonify({"Total Protien":totalCal*0.05})

@app.route('/cal/addMeal',methods = ['POST'])
def addMeal():
   global totalCal
   transaction = request.get_json()
   transaction["type"] = "addMeal"
   transaction["time"] = datetime.now()
   totalCal = totalCal + transaction["amount"]
   transactions.append(transaction)
   return jsonify({"Total Calories":totalCal})

@app.route('/cal/burnedCal',methods = ['POST'])
def burnedCal():
   global totalCal
   transaction = request.get_json()
   transaction["type"] = "burnedCal"
   transaction["time"] = datetime.now()
   totalCal = totalCal -10*transaction["amount"]
   transactions.append(transaction)
   return jsonify({"Total Calories":totalCal})




if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8081, debug = True)