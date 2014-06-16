from flask import render_template

from datascience import app
from .tasks.task1 import print_array
from .tasks.task2 import create_tableS


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/task1')
def do_task1():
    output = print_array()
    return render_template("task1.html",
                           first_line=output[0],
                           second_line=output[1])

@app.route('/task2')
def do_task2():
    general_table, summary_table = create_tableS()
    return render_template("task2.html",
                           general_table=general_table.to_html(),
                           summary_table=summary_table.to_html())
