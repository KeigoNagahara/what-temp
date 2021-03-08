from bottle import route, run, template, request
from temp_ans import temp_ans


@route('/start')
def start():
    return template('image_template', output_text='')


@route('/start', method='POST')
def start_up():
    input_text = request.forms['input_text']
    output_text = temp_ans(input_text)
    print('hoge')
    return template('image_template', output_text=output_text)


run(host='localhost', port=8080, debug=True)
