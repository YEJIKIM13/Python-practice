with open("vocabulary.txt", "w", encoding="utf-8") as vocab:
    while True:
        eng_input = input("영어 단어를 입력하세요: ")
        if eng_input == "q":
            break

        kor_input = input("한국어 뜻을 입력하세요: ")
        if kor_input == "q":
            break

        vocab.write(f"{eng_input}: {kor_input}\n")
