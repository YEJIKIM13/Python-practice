# 팰린드롬 여부를 확인하는 함수 is_palindrome을 작성
# is_palindrome은 파라미터 word가 팰린드롬이면 True를 리턴, 팰린드롬이 아니면 False를 리턴

# 함수정의
def is_palindrome(word):
    reverse_word_list = list(word)  # list로 형변환
    reverse_word_list.reverse()  # reverse 정렬

    reverse_word = "".join(reverse_word_list)
    return (reverse_word == word)


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))