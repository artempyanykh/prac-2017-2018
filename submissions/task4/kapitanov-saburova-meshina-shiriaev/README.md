### Задание 4:
Описание алгоритмов и анализ полученных данных приведены в презентации: _presentation.pdf_
 
 ## Описание задания 
После оглушительного успеха в освобождении Астапора, Миэрина и Юнкая от власти работорговцев Дейенерис Бурерожденная открыла себе доступ к Летнему морю, а следовательно -- путь в Вестерос.

Для ведения войны с Семью Королевствами нужно оружие, я для оружия нужна сталь. Нет никаких сомнений в кузнечном искусстве Безупречных, однако поставщики стали не столь надежны.

Два основных поставщика стали -- это Westeros Inc. и Harpy & Co. На протяжении нескольких месяцев мы закупаем сталь у обеих компаний, и каждая из них предлагает ощутимую скидку при заключении эксклюзивного договора на поставку.

Советник королевы Тирион Ланнистер знает о твоем умении принимать взвешенные рациональные решения и просит помощи в объективном решении вопроса о том, с какой из компаний следует заключить эксклюзивный договор на поставку стали.

У Тириона есть записи о производстве мечей каждым из кузнецов-безупречных, а также данные о количестве сломанных мечей в каждый из месяцев ведения боевых действий.

Для победы в войны с Королевствами требуется оружие, для изготовления которого нужна сталь, купить которые можно в двух компаниях Westeros Inc. и Harpy & Co, каждая из которых предлагает достаточно большую скидку если контракт на поставку сырья будет заключен эксклюзивно с ней.

### Решение задачи
анализ подразумевает множество различных способов отображения информации в наглядном виде. Мы остановились на следующих инструментах:
* Построение графиков;
* Построение гистограмм;

 ### Набор данных
 
 |unsullen.id  |	production.date |	report.date |	produced | defects | supplier|
 |    ---	    |       ---       |     ---     |   --- 	 | ---     | ---     |
 |    1.0	    |       1         |     1	      |   103.0	 |  0.0	   | harpy.co|
 |    1.0	    |       1         |     2	      |   0.0	   |  2.0	   | harpy.co|
 |    1.0	    |       1         |     3	      |   0.0	   |  4.0	   | harpy.co|
 
 * unsullen.id - id кузнеца-безупречного
 * production.date - месяц производства
 * report.date - месяц жалоб на продукцию кузнеца
 * produced - количество произведенных в данный месяц мечей
 * defects - число поломанных мечей
 * supplier - компания поставщик
 
По данному набору данных составляются различные графики, которые помогают наглядно увидеть разницу между компаниями.
 
 ### Запуск
заходим в директорию с проектом, в терминале набираем "jupyter notebook"

 ## Необходимое ПО
 1) Jupyter Notebook
 2) Latex
 
 ### Библиотеки:	
 1) **Pandas**
 * Для работы с временными рядами
 2) **Numpy** 
 * Для работы с массивами
 3) **Beamer**
 * Для работы с презентациями в среде Latex
 4) **Seaborn** 
 * Для работы с графиками
 5) **matplotlib.pyplot**
 * Для работы с графиками
 
 ## Участники 
 
 1) Капитанов Филипп - 312 гр.
 2) Мешина Злата - 312 гр.
 3) Сабурова Анна - 312 гр.
 4) Ширяев Павел - 312 гр.
 * Все этапы работы были выполнены совместно.