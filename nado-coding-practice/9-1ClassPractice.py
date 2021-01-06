# 클래스 만듦, init 함수 통해 기본적으로 필요한 값들 정의
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 똑같은 하나의 클래스 통해 서로 다른 마린과 탱크에 대해 만들 수 있었던 것! marine1과 tank는 Unit 클래스의 인스턴스
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)

# 레이스: 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않는 기능)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))  # 클래스 외부에서 멤버변수 쓴 것./ .으로 멤버변수에 접근 가능

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True
# 클로킹이라는 변수는 __init__함수 안에 없다. 외부에서 clocking이라는 변수를 추가로 할당한 것
# 파이썬에서는 추가로 객체 외부에서 변수 만들어서 쓸 수 있다.
# 확장한 변수는 확장한 객체에서만 적용됨

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
