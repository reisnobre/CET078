class Expression:
    def __init__(self, difficulty, category, expression, answer):
        self.__difficulty = difficulty
        self.__category = category
        self.__expression = expression
        self.__answer = answer

    # Getters
    def difficulty(self):
        return self.__difficulty
    def category(self):
        return self.__category
    def expression(self):
        return self.__expression
    def answer(self):
        return self.__answer

    def check(self, guess):
        return True if guess == self.__answer else False
