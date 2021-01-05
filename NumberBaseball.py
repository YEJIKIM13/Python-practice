from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        u_num = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))

        if u_num < 0 or u_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif u_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(u_num)

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    # 스트라이크 계산 먼저
    for i in range(0, 3):
        if guess[i] == solution[i]:
            strike_count += 1

    for num in guess:
        if num in solution:
            ball_count += 1

    ball_count = ball_count - strike_count

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()  # 정답 뽑기
tries = 0


# take_guess를 계속 하는거지. 답과 일치할 때까지.
# 대신 take_guess 한 번 할 때마다 tries가 늘어나고
# take_guess 끝날 때마다 get_score로 스트라이크, 볼 계산

user_guess = []  # user_guess 초기화
while user_guess != ANSWER:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)  # 변수에 담는 과정
    print(f"{s}S {b}B")
    tries += 1  # 마지막에 추가했으니까 0부터 시작해도 괜찮은 것

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
