# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку. Пример:

from operator import itemgetter

text = 'Будущий майянист родился в семье преподавателя химии Пенсильванского военного колледжа[en]; по воле отца в 1904 году получил степень бакалавра гражданской инженерии. После смерти родителя поступил в Гарвардский университет, где изучал антропологию и египтологию. С детства интересуясь цивилизациями Центральной Америки, в университете он обратился к изучению американистики, получив по этой специальности магистерскую степень (1908) и членство Американского института архитекторов, но докторскую диссертацию так и не защитил (в 1921 году Пенсильванский военный колледж присвоил ему докторскую степень honoris causa). Первые полевые исследования Морли провёл в Нью-Мексико и был связан с этим штатом всю последующую жизнь. В 1910—1912 годах вёл раскопки в Киригуа, там же впервые проводил реставрацию памятников Древней Америки (в 1935 году выпустил путеводитель по руинам). В 1921 году удостоен почётного гражданства муниципалитета Санта-Роса-де-Копан. В 1914 году впервые вёл работы в Чичен-Ице на средства Института Карнеги, до 1929 года руководил археологическим отделом Института, определяя его программу, в 1924—1940 годах возглавлял стационарную экспедицию на городище Чичен-Ицы. В 1916 году открыл руины Вашактуна — одного из древнейших городов майя. Параллельно С. Морли начал программу всестороннего изучения надписей майя, лично занимаясь поиском и съёмкой эпиграфических памятников. В 1915 году опубликовал «Введение в изучение иероглифов майя», и в 1920-м «Надписи Копана» — первую сводную публикацию эпиграфических памятников с одного городища; в 1937—1938 году выпустил пятитомные «Надписи Петена», за которые был удостоен гватемальского Ордена Кетцаля и премии Колумбийского университета. Морли интересовался хронологией, отождествил иероглифы, обозначающие 360-дневный цикл (тун), его начало и завершение, и циклы в пять и десять тунов. В 1930-е годы широко занимался популяризацией культуры древних майя. Его обобщающая книга «Древние майя» (1946) заложила стандарт подобного рода публикаций и переиздавалась шесть раз, не считая перевода на испанский язык[4]. В 1947 году Сильванус Морли был назначен директором Музея Нью-Мексико в Санта-Фе. Скончался от сердечного заболевания.'.lower().split()
res = {}
count = 0

for number, word in enumerate(text, start=1):
    res[word] = text.count(word)

sorted_text = sorted(res.items(), key=itemgetter(1), reverse=True)[:10]

for text in sorted_text:
    print(f' Слово "{sorted_text[count][0]}" повторяется {sorted_text[count][1]} раз')
    count += 1
