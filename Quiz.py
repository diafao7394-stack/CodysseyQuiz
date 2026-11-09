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

class QuizGame :
    def __init__(self, quizzes) :
        self.quizzes = quizzes

    def show_menu(self) :
        print("""퀴즈를 진행하겠습니다.
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 최고 점수
5. 종료""")

    def run(self) :
        self.show_menu()
        while True :
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
            
        


default_quizzes = [
    Quiz(
        "Question! 정유재란은 언제 발발했는가!?",
        ["592년", "1592년", "1597년", "1945년"],
        3,
    ),
    Quiz(
        "Question! 한글은 누가 창제하였는가!?",
        ["광개토대왕", "법흥왕", "광종", "세종"],
        4,
    ),
    Quiz(
        "Question! 우리나라에서 최초로 과거제를 시행한 왕은 누구인가!?",
        ["세종", "광종", "문조", "태조 왕건"],
        2,
    ),
    Quiz(
        "Question! 살수대첩에서 승리한 장수는 누구인가!?",
        ["을지문덕", "항우", "양만춘", "이순신"],
        1,
    ),
    Quiz(
        "Question! 위화도회군을 한 인물은 누구인가!?",
        ["태조 왕건", "태조 이성계", "태종 이방원", "공민왕"],
        2,
    ),
]


game = QuizGame(default_quizzes)
game.run()
