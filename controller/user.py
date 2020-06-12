from controller import answer,pachong
from flask import Blueprint,render_template,request
wv_from_text = None

user = Blueprint('user', __name__)



@user.route('/qa',methods=["POST","GET"])
def get_question():
    # wv_from_text = answer.wv()
    if request.method == 'GET':
        return render_template('qa.html')
    if request.method == 'POST':
        question = request.form.get('question')
        global wv_from_text
        if wv_from_text is None:
            wv_from_text = answer.wv()
            try:
                m_answer = answer.answer(question, wv_from_text)
            except:
                m_answer = pachong.pachong_answer(question)
            return render_template('qa.html', m_answer=m_answer)
        else:
            try:
                m_answer = answer.answer(question, wv_from_text)
            except:
                m_answer = pachong.pachong_answer(question)
            return render_template('qa.html', m_answer=m_answer)
