# 구구단 전체 출력
# for dan in range(2,10):
#    print(dan, "단")
#    for hang in range(1,10):
#        print(dan, " X " ,hang, " = " ,dan * hang)
# 아래 코드를 while문을 사용한 중첩 코드로 변경해주세요
# 힌트 -> while문 하나당 변수 하나를 써야합니다
dan = 2
while dan < 10:
    hang = 1
    print(dan,"단입니다")
    while hang < 10:
        print(dan, " * " ,hang, " = " ,dan * hang)
        hang += 1
    dan += 1
    print()