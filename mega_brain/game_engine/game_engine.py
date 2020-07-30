class Game_Engine:
    def __init__(self, lives=0, chances=0):
        self.__lives = lives
        self.__chances = chances
        self._start()

    def _start(self):
        raise NotImplementedError("Subclass must implement abstract method")
    #
    # def validate_expr(self):
    #     raise NotImplementedError("Subclass must implement abstract method")
    #
    # def end(self):
    #     raise NotImplementedError("Subclass must implement abstract method")
