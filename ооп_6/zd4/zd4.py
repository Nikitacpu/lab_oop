from radKart import RadKart
# Создаем грядку из пяти картошек
bed = RadKart(5)
# Три раза взращиваем грядку
for n in range(3):
    bed.mature_all()
    if bed.all_mature():
        print("Вся картошка созрела. Можно собирать!")
    else:
        print("Картошка ещё не созрела!")