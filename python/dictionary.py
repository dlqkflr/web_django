lunch = {
    '중국집': '양자강',
    '한식집': '시래기'
}

#lunch = dict(중국집 = '양자강')

lunch['분식집'] = '김밥카페'

lunch['중국집']

dinner = {
    '한식집': { #str, int, float, bool
        '고갯마루': '02-3456-7006',
        '순남시래기' : '02-1234-1234'
    }
}

dinner['한식집']['고갯마루']
dinner.get('한식집').get('고갯마루')

for key in lunch:
    print(key)