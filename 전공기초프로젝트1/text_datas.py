"""
# 전공기초프로젝트1 시간표 생성 프로그램
# 3239분반 4조
# 텍스트 데이터베이스
"""

TEXT_HELP = "명령어는 접두어 '/'와 명령단어를 공백 없이 붙여 사용한다.\n\
이 프로그램에서 사용할 수 있는 명령어는 다음과 같다.\n\
/도움말 명령어를 이용하면 이와 같이 도움말에 대한 정보를 열람할 수 있다.\n\
\n\
_________________________\n\
\n\
*시간표 명령어\n\
\n\
1. /이동 : 다음 목록의 페이지로 이동할 수 있다. 인자로 페이지 이름을 입력한다.\n\
페이지 목록 : 1) 메뉴페이지 2) 생성페이지 3) 결과페이지\n\
\n\
2. /입력완료 : 할 일을 모두 입력한 후 시간표를 생성하기 위해 사용한다. 인자는 없다.\n\
\n\
3. /저장 : 시간표와 할 일 데이터를 파일로 저장한다. 인자는 없다.\n\
\n\
4. /불러오기 : 시간표 혹은 할 일 데이터 파일을 열어 내용을 확인한다. 인자는 없다.\n\
\n\
_________________________\n\
\n\
*할 일 명령어\n\
\n\
1. /추가 : 할 일 데이터를 추가한다.\n\
필수로 입력하는 인자로 내용, 필수태그가 포함되어야 한다. \n\
내용은 접두, 접미어가 없고, 명령어 바로 뒤에 공백을 두고 입력되어야 한다. 필수 태그는 접두어로 샵(#)을 사용한다.\n\
선택 인자로 시작시각과 지속시간, 요일을 고정하거나, 서브 태그를 포함할 수 있다.\n\
시작시각, 지속시간, 요일은 모두 중괄호로 감싼다. 서브 태그는 접두어로 대시(-)를 사용한다. 서브 태그는 인자 중 가장 마지막에 입력되어야 한다.\n\
*예시 : /추가 친구만나기 #일과\n\
*예시 : /추가 물리문제 {금요일 수요일 13시} #과제 -p213부터 p238\n\
\n\
2. /검색 : 할 일을 검색한다. 인자로는 검색할 내용, 서브 태그 내용, 필수 태그 내용을 입력한다.\n\
인자로 검색어와 검색 조건을 입력한다. 접두어로는 대시(-)를 사용하며 몇 글자 이상 일치할 경우 출력할지 정수를 입력한다.\n\
검색할 내용은 명령어 바로 뒤에 공백을 두고 입력되어야 한다.\n\
*예시 : /검색 확통과제\n\
*예시 : /검색 미적분 과제 71 -3\n\
-> \"미적분과제71\" 텍스트 집합에서 3글자 이상 포함하는 결과를 출력한다.\n\
\n\
3. /수정 : 할 일을 수정한다. 인자로는 접두어 -와 수정할 구성요소 지칭어와 함께 올바른 접두, 접미어를 붙인 수정할 내용을 입력한다.\n\
*예시 : /수정 수학과제 -요일 {월요일}\n\
-> 요일의 경우 접두, 접미어로 중괄호를 사용하므로 중괄호를 사용한다.\n\
*예시 : /수정 영어과제 -태그 #일과\n\
-> 태그(필수 태그)의 경우 접두어로 샵(#)을 사용하므로 샵(#)을 사용한다.\n\
\n\
4. /삭제 : 할 일을 삭제한다. 인자로는 삭제할 할 일의 내용을 정확하게 입력한다.\n\
*예시 : /삭제 \"미적분수강\"\n\
-> 할 일의 내용이 정확히 일치해야 한다.\n\
\n\
_________________________\n\
\n\
*기타 명령어\n\
\n\
1. /종료 : 프로그램을 안전하게 종료합니다. 인자는 없다.\n"

BAR = "──────────"
SPC = "          "

TEXT_TODO_HEADER = "\
┌──────────┬──────────┬──────────┬──────────┬─────────────────────┬──────────┬────────────────────────┐\n\
│  할 일   │ 시작시각 │ 지속시간 │ 종료시각 │       요  일        │   태그   │        서브태그        │"

TEXT_TODO_CENTER = "\
├──────────┼──────────┼──────────┼──────────┼─────────────────────┼──────────┼────────────────────────┤\n\
│$T│$S│$R│$E│$W│$G│$D│"

TEXT_TODO_BOTTOM = "\
└──────────┴──────────┴──────────┴──────────┴─────────────────────┴──────────┴────────────────────────┘"

TEXT_TABLE = "\
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐\n\
│          │   MON    │   TUE    │   WED    │   THU    │   FRI    │   SAT    │   SUN    │\n\
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤\n\
│  09:00   │$M09│$T09│$W09│$H09│$F09│$S09│$U09│\n\
├──────────┼&M09┼&T09┼&W09┼&H09┼&F09┼&S09┼&U09┤\n\
│  10:00   │$M10│$T10│$W10│$H10│$F10│$S10│$U10│\n\
├──────────┼&M10┼&T10┼&W10┼&H10┼&F10┼&S10┼&U10┤\n\
│  11:00   │$M11│$T11│$W11│$H11│$F11│$S11│$U11│\n\
├──────────┼&M11┼&T11┼&W11┼&H11┼&F11┼&S11┼&U11┤\n\
│  12:00   │$M12│$T12│$W12│$H12│$F12│$S12│$U12│\n\
├──────────┼&M12┼&T12┼&W12┼&H12┼&F12┼&S12┼&U12┤\n\
│  13:00   │$M13│$T13│$W13│$H13│$F13│$S13│$U13│\n\
├──────────┼&M13┼&T13┼&W13┼&H13┼&F13┼&S13┼&U13┤\n\
│  14:00   │$M14│$T14│$W14│$H14│$F14│$S14│$U14│\n\
├──────────┼&M14┼&T14┼&W14┼&H14┼&F14┼&S14┼&U14┤\n\
│  15:00   │$M15│$T15│$W15│$H15│$F15│$S15│$U15│\n\
├──────────┼&M15┼&T15┼&W15┼&H15┼&F15┼&S15┼&U15┤\n\
│  16:00   │$M16│$T16│$W16│$H16│$F16│$S16│$U16│\n\
├──────────┼&M16┼&T16┼&W16┼&H16┼&F16┼&S16┼&U16┤\n\
│  17:00   │$M17│$T17│$W17│$H17│$F17│$S17│$U17│\n\
├──────────┼&M17┼&T17┼&W17┼&H17┼&F17┼&S17┼&U17┤\n\
│  18:00   │$M18│$T18│$W18│$H18│$F18│$S18│$U18│\n\
├──────────┼&M18┼&T18┼&W18┼&H18┼&F18┼&S18┼&U18┤\n\
│  19:00   │$M19│$T19│$W19│$H19│$F19│$S19│$U19│\n\
├──────────┼&M19┼&T19┼&W19┼&H19┼&F19┼&S19┼&U19┤\n\
│  20:00   │$M20│$T20│$W20│$H20│$F20│$S20│$U20│\n\
├──────────┼&M20┼&T20┼&W20┼&H20┼&F20┼&S20┼&U20┤\n\
│  21:00   │$M21│$T21│$W21│$H21│$F21│$S21│$U21│\n\
├──────────┼&M21┼&T21┼&W21┼&H21┼&F21┼&S21┼&U21┤\n\
│  22:00   │$M22│$T22│$W22│$H22│$F22│$S22│$U22│\n\
├──────────┼&M22┼&T22┼&W22┼&H22┼&F22┼&S22┼&U22┤\n\
│  23:00   │$M23│$T23│$W23│$H23│$F23│$S23│$U23│\n\
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘"

TEXT_MENU = "\
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐\n\
│                                                                                                     │\n\
│                                         시간표 생성 프로그램                                        │\n\
│                                                                                                     │\n\
│                             - 건국대학교 전공기초프로젝트1 3239분반 4조 -                           │\n\
├─────────────────────────────────────────────────────────────────────────────────────────────────────┤\n\
│                                                                                                     │\n\
│                                     ┌───────────────────────────┐                                   │\n\
│                                     │                           │                                   │\n\
│                                     │      1. 생 성 하 기       │                                   │\n\
│                                     │      2. 불 러 오 기       │                                   │\n\
│                                     │      3. 저 장 하 기       │                                   │\n\
│                                     │      4. 종 료 하 기       │                                   │\n\
│                                     │                           │                                   │\n\
│                                     └───────────────────────────┘                                   │\n\
│                                                                                                     │\n\
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘"

