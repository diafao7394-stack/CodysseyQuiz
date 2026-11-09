import json
from pathlib import Path


class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show_question(self):
        print(self.question)
        for num, choice in enumerate(self.choices, start=1):
            print(num, choice)

    def is_correct(self, selected):
        return selected == self.answer


class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = list(quizzes)
        self.best_score = None
        self.state_path = Path(__file__).resolve().with_name("state.json")

    def load_state(self):
        try:
            with self.state_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            print("저장 파일의 형식이 올바르지 않아 기본 퀴즈를 사용합니다.")
            return

        loaded_quizzes = []
        for item in data["quizzes"]:
            quiz = Quiz(item["question"], item["choices"], item["answer"])
            loaded_quizzes.append(quiz)

        loaded_best_score = data["best_score"]
        self.quizzes = loaded_quizzes
        self.best_score = loaded_best_score

    def save_state(self):
        saved_quizzes = []
        for quiz in self.quizzes:
            saved_quizzes.append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer,
            })

        data = {
            "quizzes": saved_quizzes,
            "best_score": self.best_score,
        }

        temp_path = self.state_path.with_suffix(".json.tmp")
        try:
            with temp_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            temp_path.replace(self.state_path)
        except OSError as error:
            print(f"저장 파일을 쓰지 못했습니다. {error}")

    def show_menu(self):
        print("""퀴즈를 진행하겠습니다.
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 최고 점수
5. 종료""")
    
    def run(self):
        self.show_menu()

        while True:
            try:
                choice = int(input("번호를 선택해주세요 >> ").strip())
            except ValueError:
                print("숫자를 다시 입력해주세요.")
                continue

            if choice < 1 or choice > 5:
                print("1~5 사이의 숫자를 입력해주세요.")
                continue

            if choice == 1:
                score = self.play_quiz()
                if score is not None :
                    print(f"최종 점수: {score}/{len(self.quizzes)}")
                elif score is None :
                    print("퀴즈가 정상적으로 출력되지 않았습니다.")
            elif choice == 2:
                print("퀴즈를 추가하겠습니다.")
            elif choice == 3:
                print("퀴즈 목록을 출력하겠습니다.")
            elif choice == 4:
                print("최고 점수를 알려드리겠습니다.")
            elif choice == 5:
                print("퀴즈 프로그램을 종료합니다.")
                break

    def play_quiz(self) :
        score = 0
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        for i in self.quizzes :
            while True :
                i.show_question()
                try:
                    select = int(input("정답을 입력하세요 ==> ").strip())
                    if select < 1 or select > 4 :
                        print("잘못된 값을 입력하셨습니다. 다시 입력해주세요.")
                        continue
                    score += i.is_correct(select)
                    if i.is_correct(select) :
                        print("정답입니다!")
                        break
                    elif not i.is_correct(select) :
                        print("오답입니다!")
                        break
                except ValueError :
                    print("숫자를!!!! 입력하세요!!!!")
                    continue
                    
        return score
            


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
game.load_state()
game.run()
