import re

def check_valid_fill_in_blank_quiz(self, quiz: dict) -> bool:
    fill_in_blank_quiz = quiz.get("fill_in_blank_quiz")
    answer = quiz.get("answer")
    options = quiz.get("options")
    key_expression = quiz.get("key_expression")
    answer_index = quiz.get("answer_index")
    # 0. 필드값 누락 체크
    if (
        not fill_in_blank_quiz
        or not answer
        or not options
        or not answer_index
        or not key_expression
    ):
        return False

    # 1. 빈칸이 정확히 하나, 다섯개의 언더바로 구성되어있는지 체크
    if len(re.findall(self.appropriate_blank, fill_in_blank_quiz)) != 1:
        return False
    # 2. 정답이 옵션에 포함되어 있는지 체크
    if answer not in options:
        return False
    if isinstance(answer_index, str) and not answer_index.isnumeric():
        return False
    # 3. 정답의 인덱스가 answer_index와 일치하는지 체크
    answer_index = int(answer_index)
    if options[answer_index - 1] != answer:
        return False
    # 4. blank 자리에 정답을 넣었을 때, key expression과 일치하는지 체크
    filled_sentence = fill_in_blank_quiz.replace(
        str(self.appropriate_blank), answer
    )
    if filled_sentence.lower() != key_expression.lower():
        return False
    return True