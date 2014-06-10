from flask import render_template
from datascience import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/sandra')
def sandra():
    output = print_array()
    return render_template("sandra.html", first_line=output[0], second_line=output[1])


def print_array():
    """
    outputs array=[['a','b','c'],['d','e','f']] in one line
    """
    array=[['a', 'b', 'c'],['d', 'e', 'f']]
    output = []
    for i in array:
        output.append(' '.join(i))
    return output
