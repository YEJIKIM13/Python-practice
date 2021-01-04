# 프로그래밍 기초 in Python 4-2 (2) 숫자 맞추기 게임

import random

# 상수 정의
ANSWER = random.randint(1, 20)
NUM_TRIES = 4

# 변수 정의
guess = -1  # 임시적으로 지정
tries = 0

while guess != ANSWER and tries < NUM_TRIES:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(NUM_TRIES - tries)))
    tries += 1

    if ANSWER > guess:
        print("Up")
    elif ANSWER < guess:
        print("Down")


# 사용자가 정답을 맞혀서 빠져나온 경우
# 사용자가 정답은 못 맞혔지만, 기회를 다 사용해서 빠져나온 경우
if guess == ANSWER:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))