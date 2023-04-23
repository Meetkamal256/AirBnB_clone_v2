#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """hello"""
    return ('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    """"HBNB"""
    return ('HBNB')


@app.route('/c/<text>')
def c_text(text):
    """display 'C ', followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """display 'Python ', followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def num(n):
    """display 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def html_n(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """display a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY"""
    if n % 2 == 0:
        txt = 'even'
    else:
        txt = 'odd'

    return render_template('6-number_odd_or_even.html', num=n, odd_even=txt)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
