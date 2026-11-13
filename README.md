# 전체적인 파이썬 파일 구조

Class Quiz :  
	init - question, choices, answer
	def show_question - print
	def is_correct  
Class QuizGame :
	init - quizzes (Quiz)
	def load_state (Load Json file)
	def save_state (Save Json file)
	def show_menu  
	def run
	def play_quiz
	def add_quiz
    def quiz_list

	## 실행 방법

Python 3가 필요합니다. 별도로 설치할 패키지는 없습니다.

1. `Quiz.py`가 있는 프로젝트 폴더에서 터미널을 엽니다.
2. 아래 명령으로 게임을 실행합니다.

   ```powershell
   python Quiz.py
   ```

3. 메뉴 번호를 입력해 기능을 선택합니다. `5`를 입력하면 게임이 종료됩니다.

IDLE에서는 `Quiz.py`를 열고 `F5`를 눌러 실행할 수 있습니다.

추가한 퀴즈와 최고 점수는 `Quiz.py`와 같은 폴더의 `state.json`에 저장됩니다. 저장 파일이 없는 첫 실행에는 기본 문제 5개가 나옵니다.