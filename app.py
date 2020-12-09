from flask import Flask
import os
app = Flask(__name__)
try:
    COLOR = os.environ['COLOR']
except:
    COLOR = 'Black'
@app.route('/', methods=['GET', 'POST'])
def index_page():
    return 'hello world {a}'.format(a=COLOR) 

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)