file = open("a.txt", "w", encoding="utf-8")
file.write("Садок вишневий коло хати,\n"
           "Хрущі над вишнями гудуть,\n"
           "Плугатарі з плугами йдуть,\n"
           "Співають ідучи дівчата,\n"
           "А матері вечерять ждуть.\n"
           "Сім'я вечеря коло хати,\n"
           "Вечірня зіронька встає.\n"
           "Дочка вечерять подає,\n"
           "А мати хоче научати,\n"
           "Так соловейко не дає.\n"
           "Поклала мати коло хати\n"
           "Маленьких діточок своїх;\n"
           "Сама заснула коло їх.\n"
           "Затихло все, тілько дівчата\n"
           "Та соловейко не затих.\n")
file.close()

f = open("a.txt", "r", encoding='utf-8').read().splitlines()

f1 = open("b1.txt", "w", encoding='utf-8')
f2 = open("b2.txt", "w", encoding='utf-8')
f1.write('\n'.join(f[0::2]).upper())
f2.write('\n'.join(f[1::2]).lower())

f1.close()
f2.close()
