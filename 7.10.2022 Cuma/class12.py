class Question():
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def check_answer(self, answer):
        return self.answer == answer

class Quiz():
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0
        self.load_question()
        
    
    def get_question(self):
        return self.questions[self.question_index]

    def display_question(self):
        question = self.get_question()
        print(f"Soru {self.question_index + 1}: {question.text}")
        for q in question.choices:
            print("-",q)

        answer = input("Cevabınız: ")
        self.guess(answer)
        self.load_question()

    def guess(self, answer):
        question = self.get_question()
        if question.check_answer(answer):
            self.score += 25
        else:
            self.score -= 25
        self.question_index += 1

    def load_question(self):
        if len(self.questions) == self.question_index:
            self.show_score()
        else:
            self.display_progress()
            self.display_question()

    def show_score(self):
        print("score:",self.score)

    def display_progress(self):
        total_questions = len(self.questions)
        question_number = self.question_index + 1

        if question_number > total_questions:
            print("Quiz bitti!")
        else:
            print(f"question {question_number} of {total_questions}")



q1 = Question("Türkiye'nin başkenti neresidir?",["İstanbul","Ankara","İzmir","Kayseri"],"Ankara")
q2 = Question("Dünyanın şekli nedir?",["Geoit","Küp","Düz","Küre"],"Geoit")
q3 = Question("Atatürk'ün doğum yılı nedir?",["1879","1880","1881","1882"],"1881")
q4 = Question("Şubat kaç yılda bir 30 gün?",["1","2","3","4"],"4")

questions = [q1, q2, q3, q4]

quiz1 = Quiz(questions)












