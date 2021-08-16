import gspread
import json

from flask import Flask, request

app = Flask(__name__)

gc = gspread.service_account()
worksheet = gc.open_by_url("URL").sheet1


@app.route("/get2k17", methods=['GET'])
def get2k17():
    
    rows = worksheet.get_all_values()[1:]
    
    data = []
    for row in rows:
        volunteer_info = {
            "name": row[0],
            "phone": row[2],
            "branch": row[3]
        }
        data.append(volunteer_info)
    
    data = json.dumps(data)
    
    return data


if __name__ == '__main__':
    app.run()