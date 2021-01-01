#애완동물을 소개해 주세요.
animal="강아지"#문자열 자료형이기때문에 큰따옴표
name="연탄이"
age=4 #정수형 자료이기때문에 따옴표 필요X
hobby="산책"
is_adult = age>=3#boolean형태

print("우리집"+animal+"의 이름은"+name+"이예요")
print(name+"는 "+str(age)+"살이며,"+hobby+"을 아주 좋아해요")#정수형을 +을 포함한 print 문에 쓰이기 위해선 str함수를 이용해 정수형을 문자형으로 바꿔준다.
print(name,"는 ",age,"살이며,",hobby,"을 아주 좋아해요")#+대신,을 사용할경우 str을 안써도되지만 띄어쓰기가 하나씩 포함된다.
print(name+"는 어른일까요?"+str(is_adult))#boolean형도 정수형과 마찬가지로 print문에 쓰이기 위해 str을 이용하여 문자형으로 바꿔준다.