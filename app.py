from flask import Flask,render_template

AI=Flask(__name__)

@AI.route ('/one')

def one():
    return render_template('one.html')
@AI.route('/two')

def two():
    return render_template('two.html')


if __name__=='__main__':
    AI.run(debug=True)

