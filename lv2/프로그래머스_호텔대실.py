
'''
문제: 
    호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님들을 받으려고 합니다. 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용할 수 있습니다.
    예약 시각이 문자열 형태로 담긴 2차원 배열 book_time이 매개변수로 주어질 때, 코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.

    1 ≤ book_time의 길이 ≤ 1,000
    book_time[i]는 ["HH:MM", "HH:MM"]의 형태로 이루어진 배열입니다
    [대실 시작 시각, 대실 종료 시각] 형태입니다.
    시각은 HH:MM 형태로 24시간 표기법을 따르며, "00:00" 부터 "23:59" 까지로 주어집니다.
    예약 시각이 자정을 넘어가는 경우는 없습니다.
    시작 시각은 항상 종료 시각보다 빠릅니다.

해석:
    1) 겹치는 시간대의 최대 개수를 구할 것
    2) 객실을 사용하는 시간과 청소시간은 사용이 불가능한 시간으로 동일하게 취급함
    
키포인트:
    1) 코테에서 시간은 거의 무적권 분으로 바꿀것
    2) 청소가 끝남과 동시에 입실이 가능함(ex: 10:10 청소끝 -> 10:10 입실 가능)
'''
def hotel_time(book_time):
    book_table = [0] * 1500 # 하루는 총 1440이라서 하루 전체를 분단위로 테이블로 만듬 1500인 이유는 넉넉하게 1500


    for i in range(len(book_time)):
        start_h, start_m = map(int, book_time[i][0].split(':'))
        start_time = start_h*60 + start_m
        
        if first_book > start_time:
            first_book = start_time

        end_h, end_m = map(int, book_time[i][1].split(':'))
        end_time = end_h*60 + end_m + 10

        if end_time > last_out:
            last_out = end_time

        for j in range(start_time, end_time):
            book_table[j] +=1


    answer = max(book_table)

    return answer
    