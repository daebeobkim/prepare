"""
-모듈은 sys, datetime 를 임포트해서 사용
datetime.now.date()

-출첵시스템에서 기록을 txt 파일로 저장하는 프로그램

-총 4번 반복 (A회원 출근, A퇴근, B출근, B퇴근)

-프린트와 문자열 포멧팅을 사용해서 출근과 퇴근 메세지를 출력해줄것.

-출근 시각은 24시간 기준 HHmm 양식으로 입력
ex) 1530

-input 함수로 입력받은 변수는 리스트에 콤마로 구분하여 저장
ex) 대법,220701,1530

-저장 경로는 1. 실행파일을 먼저 저장해두고, 2. 그 실행파일 기준 상대경로로 저장할것.
ex)주소="../파일이름.txt"

-저장이 완료되면 sys.exit()를 이용해서 창 종료


"""

from datetime import datetime as DT
now=DT.now()
DATE=str(now.date())
print(type(DATE))


"""

with open('원하는 파일 이름.txt','w',encoding='UTF-8') as f:
    for 원소변수 in 리스트 이름:
        f.write(원소변수+'\n')


num_list=list(range(1, 51)) 

print(num_list)
print()

for LeeJM in num_list:
    print(LeeJM)
"""
