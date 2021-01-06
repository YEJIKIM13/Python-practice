# 팰린드롬 여부를 확인하는 함수 is_palindrome을 작성
# is_palindrome은 파라미터 word가 팰린드롬이면 True를 리턴, 팰린드롬이 아니면 False를 리턴
# 인덱스를 이용해서 비교할 아이디어

# 함수정의
def is_palindrome(word):
    for left in range(len(word)):
        right = len(word) - (left+1)
        if word[left] != word[right]:
            return False
    return True  # 들여쓰기 조심할 것

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))