class Valid:
    def __init__(self, data:pd.DataFrame) -> pd.DataFrame:
        # CSV 파일 json로 변환
        csv_to_json = data.to_json(orient="records", force_ascii=False, indent=2)

        # json 파일로 불러오기
        self.data_json = json.loads(csv_to_json)

    def check_valid_quiz(self, quiz:dict) -> bool:
        # 변수 가져오기 quiz1
        quiz_1 = quiz.get("Quiz 1")
        korean_1 = quiz.get("Korean 1")
        option_1_1 = quiz.get("Option 1-1")
        option_1_2 = quiz.get("Option 1-2")
        option_1_3 = quiz.get("Option 1-3")
        answer_1 = quiz.get("Answer 1")
        index_1 = quiz.get("Index 1")
        
        # 변수 가져오기 quiz2
        quiz_2 = quiz.get("Quiz 2")
        korean_2 = quiz.get("Korean 2")
        option_2_1 = quiz.get("Option 2-1")
        option_2_2 = quiz.get("Option 2-2")
        option_2_3 = quiz.get("Option 2-3")
        answer_2 = quiz.get("Answer 2")
        index_2 = quiz.get("Index 2")

        # 0. 필드값 누락 체크
        if (
            not quiz_1
            or not korean_1
            or not option_1_1
            or not option_1_2
            or not option_1_3
            or not answer_1
            or not index_1
            or not quiz_2
            or not korean_2
            or not option_2_1
            or not option_2_2
            or not option_2_3
            or not answer_2
            or not index_2
        ):
            return False
        else:
            return True
