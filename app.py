from flask import Flask
from controller.user import user
from flask import render_template,request
from controller import answer

app = Flask(__name__)
app.register_blueprint(user)

@app.route('/')
def hello_world():
    return render_template('qa.html')


# @app.route('/qa',methods=["POST","GET"])
# def get_question():
#     if request.method == 'GET':
#         return render_template('qa.html')
#     if request.method == 'POST':
#         question = request.form.get('question')
#         m_answer = answer.answer(question, wv_from_text)
#         return render_template('qa.html', m_answer=m_answer[1])




if __name__ == '__main__':
    # wv_from_text = answer.wv()
    app.run(host='0.0.0.0', port=5000, debug=True)
