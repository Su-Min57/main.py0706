

print("{1}는 {0}를 보고 만든 건데 초상권에 대한 비용을 지불하지 않았습니다.".format("체리", "블루베리"))


origin = "체리"

copy = "블루베리"

print(f"{copy}는 {origin}를 보고 만든 건데 초상권에 대한 비용을 지불하지 않았습니다.")



name = input("Your name:")
print(name)

#문자열을 정수로 전환
age = int(input("Your age:"))
print(age + 1)

#여러 개 입력
hobbys = input("취미를 ,로 구분해서 입력 : ").split(",")
for hobby in hobbys:
    print(hobby)
print("프로그램 종료")