from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route('/fake_naver')
def fake_naver():
    return render_template('fake_naver.html')

@app.route('/fake_google')
def fake_google():
    return render_template('fake_google.html')

@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/recieve')
def recieve():
    #request.args  => {'username': 'dlqkflr', 'message':'안녕'}
    username = request.args.get('username') #=> 'dlqkflr
    message = request.args.get('message') #=> '안녕'

    # ...

    return render_template('recieve.html', username= username, message= message)




@app.route('/check_lotto')
def check_lotto():
    return render_template('check_lotto.html')

@app.route('/result_lotto')

def result_lotto():
    n = request.args.get('round_lotto') #=> 회차정보
    #lotto_number = request.args.get('lotto_number') #=> '1 2 3 4 5 6'
    numbers = [ int(number) for number in request.args.get('lotto_number').split()]

    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'

    response = requests.get(url)
    lotto = response.json() #=> dict

    #winner = []

    #for i in range(1,7):
    #    winner.append(lotto[f'drwtNo{i}'])

    winner = [lotto[f'drwtNo{i}'] for i in range(1,7)]
    bonus = lotto['bnusNo']
    
    matched = list(set(numbers) & set(winner)) #=> 중복되는 숫자들
    #count = len(matched)
    if len(matched) == 6:
        result = '1등입니다!!!'
    elif len(matched) == 5:
        if bonus in numbers:
            result = '2등입니다!!'
        else:
            result = '3등입니다!'
    elif len(matched) == 4:
        result = '4등입니다.'
    elif len(matched) == 3:
        result = '5등입니다..'
    else :
        result = '꽝입니다...'

    
    # score = 0
    # for i in lotto_number.split(' '):
    #     if int(i) in winner:
    #         score += 1
    #     elif int(i) == int(bonus) :
    #          score += 10
    # if score == 3 :
    #     score_result = '5등입니다.'
    # elif score == 4 :
    #     score_result = '4등입니다.'
    # elif score == 5 :
    #     score_result = '3등입니다.'
    # elif score == 15 :
    #     score_result = '축하드립니다. 2등입니다.'
    # elif score == 6 :
    #     score_result = '축하드립니다. 1등입니다.'
    # else :
    #     score_result = '안타깝네요 미당첨입니다.'
    

    return render_template('result_lotto.html', winner= winner, bonus = bonus, n= n, numbers = numbers, result = result)


if __name__ == '__main__':
    app.run(debug=True)