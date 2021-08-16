import gspread
import json

from flask import Flask, request

app = Flask(__name__)

gc = gspread.service_account(filename="./service_account.json")
worksheet = gc.open_by_url("URL").sheet1


@app.route("/get2k17", methods=['GET'])
def get2k17():
    data = worksheet.col_values(1)[1:]
    data = json.dumps(data)
    return data


if __name__ == '__main__':
    app.run()