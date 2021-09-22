# 조합하기
output_a ="{:+5d}".format(52) #기호를 뒤로 밀기: 양수
output_b ="{:+5d}".format(-52) #기호를 뒤로 밀기: 음수
output_c ="{:=+5d}".format(52) #기호를 앞으로 밀기: 양수
output_d = "{:=+5d}".format(-52) #기호를 앞으로 밀기: 음수
output_e = "{:+05d}".format(52) #0으로 채우기: 양수
output_f = "{:+05d}".format(-52) #0으로 채우기: 음수

print("# 조합하기")
print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)
print(output_f)
