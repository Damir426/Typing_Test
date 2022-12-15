from tkinter import *
import ctypes
import random
import tkinter

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title('Тест скорости')

root.geometry('800x800')

root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")


def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            labelRight.configure(text=labelRight.cget('text')[1:])

            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())

            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass


def resetWritingLabels():
    possibleTexts = [
        'Шакира – знаменитая певица и самая успешная латиноамериканская исполнительница на современной сцене, автор многих популярных музыкальных композиций. Благодаря таланту и трудолюбию она легко взобралась на вершину олимпа славы и сейчас остается любимицей публики. Ее имя фигурирует в Книге рекордов Гиннесса, а также в многочисленных рейтингах и хит-парадах. ',
        'Шакира Изабель Мебарак Риполл родилась 2 февраля 1977 года в колумбийском городе Барранкилья. В семье Нидии Риполл и Уильяма Мебарака Шадида воспитывалось еще 8 детей от предыдущих браков Шадида. Отец будущей звезды был богатым человеком, владел ювелирным магазином и увлекался написанием прозы.',
        'Шакира рано выучила алфавит, читала и писала на родном языке. Девочка начала писать стихи в 4-летнем возрасте, а к 7 годам обзавелась собственной печатной машинкой. В детстве она увлеклась танцем живота, поэтому родители незамедлительно отправили юную звезду обучаться хореографии. Музыка заинтересовала будущую артистку чуть позднее. Тем не менее уже в 8 лет ее репертуар пополнился первой композицией.'
    ]

    text = random.choice(possibleTexts).lower()

    splitPoint = 0

    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg='red')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    global labelRight
    labelRight = Label(root, text=text[splitPoint:])
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg='red')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    global timeleftLabel
    timeleftLabel = Label(root, text=f'0 Секунды:', fg='blue')
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    root.after(60000, stopTest)
    root.after(1000, addSecond)


def stopTest():
    global writeAble
    writeAble = False

    amountWords = len(labelLeft.cget('text').split(' '))

    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    global ResultLabel
    ResultLabel = Label(root, text=f'Слов минуту: {amountWords}', fg='blue')
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    global ResultButton
    ResultButton = Button(root, text=f'Начать занова', command=restart)
    ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)


def restart():
    ResultLabel.destroy()
    ResultButton.destroy()

    resetWritingLabels()


def addSecond():
    global passedSeconds
    passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Секунды')

    if writeAble:
        root.after(1000, addSecond)


resetWritingLabels()

root.mainloop()

