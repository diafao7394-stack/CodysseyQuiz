class Quiz() :
    def __init__(self, question, choices, answer) :
        self.question = question
        self.choices = choices
        self.answer = answer
        
    def show_question(self) :
        print(self.question)
        for num, choice in enumerate(self.choices, start=1) :
          print(num, choice)
        
    def is_correct(self, selected) :
        return selected == self.answer


while True :
    print("""퀴즈를 진행하겠습니다.
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 최고 점수
5. 종료""")
    try :
        a = int(input("번호를 선택해주세요 >> ").strip())
        
        if (a > 5) or (a < 1 ) :
            print("1~5 사이의 숫자를 입력해주세요")
            continue
        elif a == 1 :
            print("퀴즈를 출제하겠습니다")
        elif a == 2 :
            print("퀴즈를 추가하겠습니다")
        elif a == 3 :
            print("퀴즈 목록을 출력하겠습니다.")
        elif a == 4 :
            print("최고 점수를 알려드리겠습니다.")
        elif a == 5 :
            print("퀴즈 프로그램을 종료합니다.")
            break
    except ValueError :
        print("숫자를 다시 입력해주세요.")
        continue

