from flask import Flask, render_template, request, redirect
import requests
import json
import data_manager
import function_app
import datetime

app = Flask(__name__)

@app.route ("/")
def index():
    return render_template('index.html')

@app.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        sysTime = str(datetime.datetime.now())
        title = request.form['title']
        message = request.form['message']
        data = {'datetime':sysTime,'title':title,'message':message}
        print("Before Post")
        response = requests.post('https://arydeenfunc.azurewebsites.net/api/CreateRecord', data=json.dumps(data))
        print("After Post:" + str(response.status_code))
        if (response.status_code == 200): 
            return redirect('/records', code=200)
        else:
            return render_template("createFail.html")
    elif request.method == 'GET':
        return render_template("create.html")

@app.route ("/records")
def records():
    print("Before read records")
    response = requests.get('https://arydeenfunc.azurewebsites.net/api/ReadRecords')
    if response.status_code == 200:
        try:
            data = json.loads(response.text.replace("'", "\""))
            return render_template('records_template.html', records=data)
        except json.JSONDecodeError as e:
            return f"Error decoding Json: {e}"
    else:
        return "Failed to fetch records"
    
if __name__ == '__main__':
    app.run(debug=True)