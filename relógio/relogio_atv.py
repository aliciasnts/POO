

class NumberDisplay:
    def __init__(self, rollOverLimit):
        self.__limit = rollOverLimit
        self.__value = 0

    def increment(self):
        self.__value = (self.__value + 1) % self.__limit

    def getValue(self):
        return self.__value

    def setValue(self, replacementValue):
        if 0 <= replacementValue < self.__limit:
            self.__value = replacementValue
        else:
            raise ValueError("Valor fora dos limites permitidos.")

    def getDisplayValue(self):
        return f"{self.__value:02d}"


class ClockDisplay:
    def __init__(self):
        self.__hours = NumberDisplay(24)
        self.__minutes = NumberDisplay(60)
        self.__seconds = NumberDisplay(60)
        self.__updateDisplay()

    def timeTick(self):
        self.__seconds.increment()
        if self.__seconds.getValue() == 0:
            self.__minutes.increment()
            if self.__minutes.getValue() == 0:
                self.__hours.increment()
        self.__updateDisplay()

    def __updateDisplay(self):
        self.__displayString = f"{self.__hours.getDisplayValue()}:{self.__minutes.getDisplayValue()}:{self.__seconds.getDisplayValue()}"

    def getTime(self):
        return self.__displayString

    def setTime(self, hour, minute, second):
        self.__hours.setValue(hour)
        self.__minutes.setValue(minute)
        self.__seconds.setValue(second)
        self.__updateDisplay()


def testNumberDisplay():
    print("\nTestando NumberDisplay:")
    numDisplay = NumberDisplay(60)

    print("Valor inicial:", numDisplay.getValue())
    numDisplay.setValue(30)
    print("Valor após setValue(30):", numDisplay.getValue())
    numDisplay.increment()
    print("Valor após increment:", numDisplay.getValue())
    print("Valor de exibição:", numDisplay.getDisplayValue())

    try:
        numDisplay.setValue(70)  # Isso deve gerar um erro
    except ValueError as e:
        print(e)


def testClockDisplay():
    print("\nTestando ClockDisplay:")
    clock = ClockDisplay()

    print("Hora inicial:", clock.getTime())

    for _ in range(65):
        clock.timeTick()
    print("Hora após 65 segundos:", clock.getTime())

    clock.setTime(1, 0, 0)
    print("Hora configurada para 01:00:00:", clock.getTime())

    for _ in range(3600):
        clock.timeTick()
    print("Hora após 3600 segundos:", clock.getTime())


def main():
    print("Iniciando testes...")
    testNumberDisplay()
    testClockDisplay()
    print("\nTestes concluídos!")


if __name__ == "__main__":
    main()
    
