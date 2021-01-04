# 프로그래밍 기초 in Python 4-2 (2) 숫자 맞추기 게임

import random

answer = random.randint(1, 20)

for num in [4, 3, 2, 1]:
    input_num = int(input(f"기회가 {num}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    if input_num == answer:
        chance = 5 - num
        print(f"축하합니다. {chance}번 만에 숫자를 맞히셨습니다.")
        break
    elif input_num < answer:
        if num > 1:
            print("Up")
        else:
            print(f"Up\n아쉽습니다. 정답은 {answer}입니다.")
    elif input_num > answer:
        if num > 1:
            print("Down")
        else:
            print(f"Down\n아쉽습니다. 정답은 {answer}입니다.")