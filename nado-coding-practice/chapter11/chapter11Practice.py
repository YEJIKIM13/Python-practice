# 모듈 import
import theater_module
theater_module.price(3)  # 3명이서 영화를 보러갔을 때 가격
theater_module.price_morning(4)  # 4명이서 조조할인 영화를 보러갔을 때 가격
theater_module.price_soldier(5)  # 5명이서 군인할인 영화를 보러갔을 때 가격

# # 모듈의 별명사용
# import theater_module as tm
# tm.price(3)
# tm.price_morning(4)
# tm.price_soldier(5)
#
# # 모듈 내에서 전부 불러오기
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)
#
# # 모듈 내에서 필요부분 불러오기
# from theater_module import price, price_morning
# price(3)
# price_morning(4)