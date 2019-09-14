from flask import Flask, render_template, url_for, jsonify
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('static/data/students.csv')

app = Flask(__name__)


@app.route('/')
def index():
    # Student 1: Change this plot to a bar chart
    df.bar()
    plt.xlabel('Student')
    plt.xticks(ticks=df.index, labels=df.student)
    plt.ylabel('Grade')
    plt.tight_layout()
    plt.savefig('static/img/plot.svg')

    # Student 2: Remove the index in the resulting html
    tables = df.to_html(index=False,classes='table table-striped')

    return render_template("index.html", tables=[tables])


@app.route('/API/students', methods=['GET'])
def students():
    # Student 1: Sort df on 'grade' inplace (inplace=True)
    # Student 2: Jsonify the response
<<<<<<< HEAD
    students_dict = df.to_dict(orient='records').sort_values(inplace=True)
    return str(students_dict)
=======
    students_dict = df.to_dict(orient='records')
    return jsonify(students_dict)
>>>>>>> 335e5733ba717abdebb38f73655b04e7027dd030


if __name__ == "__main__":
    app.run(debug=True)
