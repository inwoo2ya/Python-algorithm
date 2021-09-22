#정수
input_a = input("입력 > ")
int_a = int(input_a)
output_a = "{:d}".format(int_a)


#특정 칸에 출력
output_b = "{:5d}".format(int_a)
output_c = "{:10d}".format(int_a)

#빈칸을 0으로 채우기
output_d = "{:05d}".format(int_a)
output_e = "{:05d}".format(-int_a)

#기호와 함께 출력하기
output_f = "{:+d}".format(int_a)
output_g = "{:+d}".format(-int_a)
output_h = "{: d}".format(int_a)
output_i = "{: d}".format(-int_a)

print("#기본")
print(output_a)
print()
print("#특정 칸에 출력하기")
print(output_b)
print(output_c)
print()
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)
print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)

