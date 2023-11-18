class Interaction:
    def __init__(self, question, expected_answer, answer, answer_time, simalirity):
        self.question = question
        self.expected_answer = expected_answer
        self.answer = answer
        self.answer_time = answer_time
        self.simalirity = simalirity

    def __str__(self):
        return f"Question: {self.question}\nExpected Message: {self.expected_answer}\nAnswer: {self.answer}\nAnswer time:{self.answer_time}, \nSimali{self.simalirity}"