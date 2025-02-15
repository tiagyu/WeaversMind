import re

response = "goal='자기소개와 출신지에 대해 말하고, 이에 반응하기.' preview_quizzes=[Quiz(fill_in_blank_quiz='A: ___ Felix. I’m from Australia. B: Glad to meet you.', korean_translation='내 이름은 Felix이야. 나는 호주 출신이야. 반가워.', options=['I live in', 'My name is', 'This is'], answer='My name is', answer_index=2), Quiz(fill_in_blank_quiz='A: Hi, I’m Emily. ______ Canada. B: Nice to meet you.', korean_translation='안녕, 나는 Emily야. 나는 캐나다 출신이야. 반가워.', options=['I come from', 'I live in', 'I was born in'], answer='I come from', answer_index=1)]"

class QuizValidator:
    def __init__(self):
        self.appropriate_blank = r'_{3}'
    
    def check_valid_fill_in_blank_quiz(self, quizzes:str) -> bool:
        """
        퀴즈 데이터의 유효성을 검증하는 메서드
        """
        preview_quizzes = quizzes.dict()['preview_quizzes']
        
        # 데이터 값 가져오기
        for i in range(len(quizzes.dict())):
            fill_in_blank_quiz = preview_quizzes[i]['preview_quizzes']
            korean_translation = preview_quizzes[i]['korean_translation']
            options = preview_quizzes[i]['options']
            answer = preview_quizzes[i]['answer']
            answer_index = preview_quizzes[i]['answer_index']
            print(fill_in_blank_quiz)
            print(korean_translation)
            print(options)
            print(answer)
            print(answer_index)

        return True
    

print(QuizValidator.check_valid_fill_in_blank_quiz(response))
