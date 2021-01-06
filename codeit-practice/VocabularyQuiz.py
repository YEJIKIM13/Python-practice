with open("vocabulary.txt", "r") as vocab:
    # lines = vocab.readlines()  # 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려줌
    # for line in lines:
    for line in vocab:
        line_word = line.strip().split(": ")
        line_word_eng = line_word[0]
        line_word_kor = line_word[1]

        # 유저 입력값 받기
        user_eng_input = input(f"{line_word_kor}: ")

        # 정답확인
        if user_eng_input == line_word_eng:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {line_word_eng}입니다.")