# Git 복제 실습 기록

역사 퀴즈 프로젝트의 저장소 초기화부터 기능 브랜치 병합, 복제본에서 만든 README 커밋을 원본으로 가져오기까지 기록했습니다. 명령은 Windows PowerShell에서 실행했습니다. 터미널 출력은 결과 확인에 필요한 줄만 발췌했고, 공개 문서의 로컬 경로는 `$env:USERPROFILE`로 표기했습니다.

| 폴더 | 경로 |
|---|---|
| 원본 작업 폴더 | `$env:USERPROFILE\.codyssey\2주차` |
| 복제를 실행한 상위 폴더 | `$env:USERPROFILE\Documents\ChatGPT` |
| 복제본 작업 폴더 | `$env:USERPROFILE\Documents\ChatGPT\CodysseyQuiz-clone-practice` |

## 1. 원본 저장소 초기화와 첫 커밋

원본 작업 폴더에서 `main`을 만들고 `.gitignore`와 `README.md`를 첫 커밋에 넣었습니다.

```powershell
git init -b main
git status --short --branch
git add -- .gitignore README.md
git status --short --branch
git commit -m "chore: initialize quiz project"
git log -1 --oneline
```

```text
## No commits yet on main
A  .gitignore
A  README.md
?? Quiz.py
[main (root-commit) 75904e2] chore: initialize quiz project
75904e2 (HEAD -> main) chore: initialize quiz project
```

`A`는 다음 커밋에 들어갈 새 파일, `??`는 Git이 아직 추적하지 않는 파일입니다. `Quiz.py`는 뒤에서 메뉴 기능을 별도 커밋으로 기록했습니다.

## 2. GitHub 연결과 첫 푸시

원본 폴더에서 `git remote -v`로 연결을 확인한 뒤 `origin`을 추가했습니다. 실제 URL을 넣을 자리에 예시 문구인 `복사한 https 주소`를 그대로 입력해 첫 푸시가 실패했습니다.

```text
fatal: '복사한 https 주소' does not appear to be a git repository
fatal: Could not read from remote repository.
```

같은 폴더에서 주소를 실제 GitHub URL로 바꿨습니다.

```powershell
git remote set-url origin (Read-Host 'GitHub HTTPS 주소')
git remote -v
git push -u origin main
```

```text
origin  https://github.com/diafao7394-stack/CodysseyQuiz (fetch)
origin  https://github.com/diafao7394-stack/CodysseyQuiz (push)
 ! [rejected]        main -> main (fetch first)
```

GitHub에 README를 만든 첫 커밋 `55e33bb`가 이미 있었습니다. GitHub와 로컬에서 독립적으로 시작한 두 이력을 합치기 위해 원격 이력을 가져오고 병합한 뒤 다시 푸시했습니다.

```powershell
git status --short --branch
git fetch origin
git merge --allow-unrelated-histories -m "Merge GitHub initial commit" origin/main
git push -u origin main
```

```text
Auto-merging README.md
Merge made by the 'ort' strategy.
55e33bb..f85f163  main -> main
branch 'main' set up to track 'origin/main'.
```

`f85f163`은 로컬 첫 커밋 `75904e2`와 GitHub 첫 커밋 `55e33bb`를 합친 커밋입니다. `-u`로 로컬 `main`에 기본 추적 대상인 `origin/main`을 설정했습니다.

## 3. 메뉴 커밋과 기능 브랜치 병합

원본 폴더에서 `git add -- Quiz.py`로 파일을 스테이징했습니다. 이어서 `git commit`을 실행했으나 메시지를 비워 두어 커밋이 취소됐습니다. `git add -- Quiz.py -m "add quiz menu"`도 시도했는데, `--` 뒤의 `-m`은 파일 경로로 해석됐습니다.

```text
Aborting commit due to empty commit message.
fatal: pathspec '-m' did not match any files
```

이미 스테이징한 `Quiz.py`를 `git commit -m "add quiz menu"`로 커밋했습니다.

```text
[main bb66e31] add quiz menu
bb66e31 (HEAD -> main) add quiz menu
```

퀴즈 풀기는 원본의 `main`에서 `git checkout -b feature/play-quiz`로 만든 작업 브랜치에서 진행했습니다. 브랜치의 구현 커밋 `374dde0`과 기록 커밋 `0cd753c`를 만든 뒤, `git checkout main`으로 돌아와 `feature/play-quiz`를 병합했습니다. 저장소 이력에서 병합 커밋 `ff77c31`의 두 부모가 `d40a593`과 `0cd753c`임을 확인했습니다.

| 커밋 | 기록한 변경 |
|---|---|
| `54c988b` | `Quiz` 클래스와 정답 판정 |
| `892096d` | 기본 역사 문제 5개와 실습 기록 |
| `4f2c626`, `da1c7e3` | `QuizGame`으로 메뉴 실행 흐름 이동 |
| `4c1d515`, `d40a593` | JSON 저장·불러오기와 빈 목록 저장 수정 |
| `374dde0`, `0cd753c`, `ff77c31` | 퀴즈 풀기·채점 구현, 실행 기록, `main` 병합 |
| `331fb84`, `d29fe34` | 퀴즈 추가·저장, 목록 조회와 빈 목록 처리 |
| `80d6231`, `d924443` | 기본 미션 코드 및 기록 마무리 |

## 4. 별도 폴더에 저장소 복제

`Documents\ChatGPT` 폴더에서 복제 명령을 실행한 뒤, 생성된 복제본 폴더로 이동했습니다.

```powershell
Set-Location -LiteralPath "$env:USERPROFILE\Documents\ChatGPT"
git clone https://github.com/diafao7394-stack/CodysseyQuiz.git CodysseyQuiz-clone-practice
Set-Location -LiteralPath "$env:USERPROFILE\Documents\ChatGPT\CodysseyQuiz-clone-practice"
git log -1 --oneline
```

```text
Cloning into 'CodysseyQuiz-clone-practice'...
Receiving objects: 100% (79/79), 16.62 KiB | 160.00 KiB/s, done.
Resolving deltas: 100% (36/36), done.
d924443 (HEAD -> main, origin/main, origin/HEAD) 완성본
```

## 5. 복제본 README 수정, 커밋, 푸시

복제본 작업 폴더의 README에 `python Quiz.py` 명령, IDLE의 `F5` 실행 방법, `state.json`의 저장 위치를 추가했습니다. `git diff -- README.md`의 페이지 보기에서 `q`로 나온 뒤 `--no-pager`를 붙여 변경 내용을 한 번에 확인했습니다.

```powershell
git --no-pager diff -- README.md
git add -- README.md
git commit -m "Document how to run the quiz"
git push origin main
```

```text
[main 0e5799a] Document how to run the quiz
 1 file changed, 18 insertions(+), 2 deletions(-)
d924443..0e5799a  main -> main
```

## 6. 원본 폴더에서 가져오기

원본 작업 폴더로 돌아와 `git pull --ff-only origin main`을 실행했습니다. GitHub의 새 커밋은 가져왔지만, 원본 README에 커밋하지 않은 변경이 있어 작업 파일에 반영하는 과정이 중단됐습니다. `git log -1 --oneline`에서 로컬 `main`이 `d924443`에 머물러 있는 것을 확인했습니다.

```text
Updating d924443..0e5799a
error: Your local changes to the following files would be overwritten by merge:
        README.md
Aborting
d924443 (HEAD -> main) 완성본
```

같은 원본 폴더에서 README 변경을 확인하고 그 파일만 `stash`에 보관했습니다. 그런 다음 `pull`을 다시 실행했습니다.

```powershell
git --no-pager diff -- HEAD -- README.md
git stash push -m "Save original README edits before pull" -- README.md
git pull --ff-only origin main
git log -1 --oneline
```

```text
Saved working directory and index state On main: Save original README edits before pull
Updating d924443..0e5799a
Fast-forward
 README.md | 20 ++++++++++++++++++--
 1 file changed, 18 insertions(+), 2 deletions(-)
0e5799a (HEAD -> main, origin/main) Document how to run the quiz
```

복제본에서 푸시한 커밋과 원본에서 `pull`한 뒤의 커밋은 모두 `0e5799a`였습니다. 이 커밋에서 README 변경 한 건이 원본에 반영됐고, 원본 README의 이전 로컬 수정은 `stash`에 보관했습니다.

| 실습 시점 | 복제본 `main` | 원본 `main` |
|---|---|---|
| 복제 직후 | `d924443` | `d924443` |
| 복제본 푸시 후, 원본의 첫 pull 중단 | `0e5799a` | `d924443` |
| 원본의 pull 재시도 성공 | `0e5799a` | `0e5799a` |
