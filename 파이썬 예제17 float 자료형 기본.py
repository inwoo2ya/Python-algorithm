#float 자료형 기본
output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273) #15칸 만들기
output_c = "{:+15f}".format(52.273) #15칸에 부호 추가
output_d = "{:+015f}".format(52.273) #15칸에 부호 추가하고 0으로 채우기
#소수점 아래 자릿수 지정
output_e = "{:15.3f}".format(52.2734) 
output_f = "{:15.2f}".format(52.2734)
output_g = "{:15.1f}".format(52.2734)
#의미없는 소수점 제거하기
a = 52.0
b = "{:g}".format(a)
print("#float 자료형 기본")
print(output_a)
print(output_b)
print(output_c)
print(output_d)
print("#소수점 아래 자릿수 지정")
print(output_e)
print(output_f)
print(output_g)
print("#의미없는 소수점 제거")
print(a)
print(b)
