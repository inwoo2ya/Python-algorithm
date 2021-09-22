score =float (input("평균학점을 입력해주십시오 >> "))
score = (score)

if score == 4.5 :
    print("축하합니다! 당신의 학점은 4.5 로  \" 신 \" 단계입니다.")
elif score >4.5:
    print(" 고딩이냐? ㅋ")
elif 4.2<= score<4.5:
    print("축하합니다! 당신의 학점은 {} 로 \" 교수님의 사랑 \" 단계입니다.".format(score))
elif 3.5<= score < 4.2:
    print("축하합니다! 당신의 학점은 {} 로 \" 현 체제의 수호자 \" 단계입니다.".format(score))
elif 2.8<= score < 3.5:
    print("당신의 학점은 {} 로 \" 일반인\" 단계입니다.".format(score))
elif 2.3<= score < 2.8:
    print("당신의 학점은 {} 로 \" 일탈을 꿈꾸는 소시민 \" 단계입니다.".format(score))
elif 1.75<=score <2.3:
    print("당신의 학점은 {} 로 \" 오락문화의 선구자 \" 단계입니다. \n아직 늦지않았습니다. 공부좀 하세요!".format(score))
elif 1.0<= score <1.75:
    print("당신의 학점은 {} 로 \" 불가촉천민 \" 단계입니다.".format(score))
elif 0.5<= score <1.0:
    print("당신의 학점은 {} 로 \" 자벌레 \" 단계입니다. \n제발 공부좀 하세요!".format(score))
elif 0< score<0.5 :
    print("당신의 학점은 {} 로 \" 플랑크톤 \"단계입니다. \n우리집 개가 그것보다 잘나오겠다...".format(score))
else :
    print(" 대단해요! 당신의 학점은 0 으로 \" 시대를 앞서가는 혁명의 씨앗 \" 단계입니다. \n아주 멋져요!! 진심으로 한거면 공부는 안맞습니다.\n 자퇴를 하세요".format(score)) 
