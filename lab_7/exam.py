class Exam:
    amount = 0
    def __init__(self, student):
        self._aswers = [None] * 20
        self._template = [None] * 20
        self._student = student
        self.start()

    def start(self):
        for i in range(20):
            self.template(i, input('Resposta da questão {}: '.format(i+1)))

    def template(self, index, answer):
        self._template[index] = answer

    def correct(self):
        raise NotImplementedError("Subclass must implement abstract method")


    def answer(self, index, answer):
        raise NotImplementedError("Subclass must implement abstract method")

class MultipleChoice(Exam):
    def __init__(self, student):
        Exam.__init__(self, student=student)
        Exam.amount += 1
        print(self._template)
    def correct(self):
        print('correct')

    def answer(self, index, answer):
        self._aswers[index] = answer

class SumChoice(Exam):
    def __init__(self):
        Exam.__init__(self, student=student)
        Exam.amount += 1
    def correct(self):
        print('correct')

    def answer(self, index, answer):
        self._aswers[index] = answer
