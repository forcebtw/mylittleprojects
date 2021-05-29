pupil = [100,63,76,54,13,90,19,86,56,91]
for index, value in enumerate(pupil):
    if value < 60:
        print(f"Ученик номер {index + 1} тест не прошел, баллов - {value}. В журнал поставлена оценка 2")
    if value>60 and value < 75:
        print(f"Ученик номер {index+1} тест прошел, баллов - {value}. В журнал поставлена оценка 3")
    if value > 75 and value < 85:
        print(f"Ученик номер {index +1 } тест прошел, баллов - {value}. В журнал поставлена оценка 4")
    if value > 85:
        print(f"Ученик номер {index + 1} тест прошел, баллов - {value}. В журнал поставлена оценка 5")
