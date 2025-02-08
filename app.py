from flask import Flask, render_template, request, redirect
import os


app = Flask(__name__)

poll_data = {
    'question': 'Which framework do you use?',
    'fields': ('Flask', 'Django')
}

filename = 'data.txt'

@app.route('/')
def root():
    return render_template('poll.html', data=poll_data)


@app.route('/poll')
def poll():
    vote = request.args.get('field')
    out = open(filename, 'a')
    out.write(vote + '\n')
    out.close()
    return vote

if __name__ == "__main__":
    app.run(debug=True)
    


