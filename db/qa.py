from db.sql import Session


def search_question_answer(id):
    session = Session()
    sql = 'select question,answer from QuestionAnswer where id = {}'.format(id)
    cursor = session.execute(sql)
    result = cursor.fetchall()
    session.close()
    return result


def get_docs(word):
    session = Session()
    sql = 'select docs from IIndex where word = "{}"'.format(word)
    cursor = session.execute(sql)
    result = cursor.fetchall()
    session.close()
    return result



