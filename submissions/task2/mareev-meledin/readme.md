# Задание 2
## Краткое описание задания
### Обязательные пункты
1. Считать данные из training.csv. Ответы на тестовой выборке testing.csv не следует использовать ни в каких экспериментах, кроме финального. Проверить является ли ряд стационарным в широком смысле. Это можно сделать двумя способами:
Провести визуальную оценку, отрисовав ряд и скользящую статистику(среднее, стандартное отклонение). Постройте график на котором будет отображен сам ряд и различные скользящие статистики.
Провести тест Дики - Фуллера.
Сделать выводы из полученных результатов. Оценить достоверность статистики. (25 баллов)
1. Разложить временной ряд на тренд, сезональность, остаток в соответствии с аддитивной, мультипликативной моделями. Визуализировать их, оценить стационарность получившихся рядов, сделать выводы. (15 баллов)
1. Проверить является ли временной ряд интегрированным порядка k. Если является, применить к нему модель ARIMA, подобрав необходимые параметры с помощью функции автокорреляции и функции частичной автокорреляции. Выбор параметров обосновать. Отобрать несколько моделей. Предсказать значения для тестовой выборки. Визуализировать их, посчитать r2 score для каждой из моделей. Произвести отбор наилучшей модели с помощью информационного критерия Акаике. Провести анализ получившихся результатов. (50 баллов)
За все правильно выполненные пункты можно получить 90 баллов.

### Необязательные пункты
1. +10 баллов - соблюдение PEP8.

1. +10 баллов - использование для визуализации библиотек bokeh или seaborn. Надо сделать, чтобы было красиво:).

1. 30 баллов - конкурсные. Вы можете использовать различные статистические модели и методы машинного обучения(ARIMA, ES, ARFIMA, LSTM, различные виды регрессий, etc). 30 баллов получает группа, получившая наилучший результат среди учавствующих.

## Теоретическая справка

***Временной ряд*** -  это последовательность значений, описывающих протекающий во времени процесс, измеренный в последовательные моменты времени, обычно через равные промежутки. 

### Пункт 1

***Стационарный временной ряд*** - это временной ряд для которого справедливо следующие:

1. Математическое ожидание временного ряда постоянно.
1. Дисперсия временного ряда постоянна.
1. Автоковариация ряда с лагом I является постоянной.

**Замечание:** Если давать более неформальное определение, то ряд явялется стационарным, если не имеет тренда.

***Тренд*** - основная тенденция развития ряда (может быть линейный, экспоненциальным и тд...).

***Скользящая средняя*** - функция, значение которой в каждой точке определения равны среднему значению исходной функции за предыдущий период заданного размера.

***Стандартное отклонение*** - показатель рассеивания значений временного ряда относительно их среднего значения.

### Пункт 2
***Сезональность*** - составляющая временного ряда, которая характеризует переодические измнения в нём.

***Остаток*** - составляющая временного ряда, которая характеризует ошибку между фактическим и теоретическим  значением временного ряда.

***Аддитивная модель*** - модель согласно которой ```Y = T + S + E```, где 

* ***Y*** - значение временного ряда.
* ***T*** - тренд.
* ***S*** - сезональность.
* ***E*** - остаток.

Как находить составляющие:

* Тренд находиться с помощью приближения временного ряда методом наименьших квадратов.
* Сезональность - это разность между временным рядом и его центрированным скользящим средним (скользящее среднее от скользящего среднего). 
* Для нахождения остатка вычитаем из значения ряда тренд и сезональность.

***Мультипликативная модель*** - модель согласно которой ```Y = T * S * E```, где 

* ***Y*** - значение временного ряда.
* ***T*** - тренд.
* ***S*** - сезональность.
* ***E*** - остаток.

Как находить составляющие:

* Тренд находиться с помощью приближения временного ряда методом наименьших квадратов.
* Сезональность - это частное между временным рядом и его центрированным скользящим средним (скользящее среднее от скользящего среднего). 
* Для нахождения остатка делим значение ряда на тренд и сезональность.

### Пункт 3
***Интегрированный временной ряд*** - нестационарный временной ряд, разности некоторого порядка от которого являются стационарным временным рядом.

***Интегрированный временной ряд порядка ```k```*** - это нестационарны временной ряд, разности порядка ```k``` от которого являются стационарным временным рядом, а все разности меньшего порядка являются нестационарными рядами.

***ARIMA(p,d,q)*** - интегрированная модель авторегресси - скользящего среднего - модель для анализа и прогнозирования временных рядов. Является разширение модели ARMA(p,q) для нестационарных временных рядов. Здесь ```d``` - порядок интегрирования временного ряда. 

***ARMA(p,q)*** - модель для анализа и прогнозирования стационарных временных рядов. Является обобщение модели AR(p) и MA(q).

***AR(p)*** - модель для анализа и прогнозирования стационарных временных рядов. В ней значения временного ряда в текущий момент линейно зависят от ```p``` предыдущих значений ряда.

***MA(q)*** - модель для анализа и прогнозирования стационарных временных рядов. в ней значения временного ряда в текущий момент линейно зависят от ```q``` предыдущих остатков временного ряда.

***Коэффициент детерминации*** - это доля дисперсии зависимой переменной, объясняемая рассматриваемой моделью зависимости. Чем значение критерия детерминации ближе к единице, тем лучше модель предсказывет значения временного ряда.

***Информационнный критерий Акаике*** - численная характеристика для оценки моделей между собой и выбора лучшей (У какой модели он меньше, та и лучше по сравнению с другой). Особенность данного критерия является то, что он не отображает насколько хорошо модель предсказывает значения временного ряда.


## Подход к решению
1. Считывание данных и проверка временного ряда на стационарность(был выбран визуальный метод оценки), включала в себя следующие шаги:
	* Считывание данных из файла [training.csv](https://github.com/GlebOlegovich/prac-2017-2018/blob/task2-mareev-meledin/submissions/task2/mareev-meledin/training.csv) с помощью функции ```read_csv``` из библиотеки ```Pandas```.
	* Отображения временного ряда с помощью метода ```plot``` объекта ```DataFrame``` из библиотеки ```Pandas```, для получения первоначального представления  о ряде.
	* Вычисления скользящего среднего и стандартного отклонения ряда с помощью метода ```rolling``` объекта ```DataFrame``` и методов ```mean``` и ```std``` объекта ```Rolling``` из библиотеки ```Pandas``` (для рассчета брались результаты за два года).
	* Отображение временного ряда и его статистик с помощью метода ```plot``` объекта ```DataFrame``` из библиотеки ```Pandas```.
	* Визуальная оценка стационарности (определение: если ли тренд или нет) и достоверности ряда.

1. Разложение временного ряда на составляющие в соответствие с аддитивной и мультипликативной моделями включало в себя следующие шаги:
	* Разложение ряда на составляющие в соответсвие с аддитивной моделью с помощью функции ```seasonal_decompose``` из библиотеки ```statsmodels```.
	* Отображение временного ряда, тренда, сезональности и остатка в соответствии с аддитивной моделью с помощью метода ```plot``` объекта ```DataFrame``` из библиотеки ```Pandas``` (отдельно были отображены сезональность и остаток, так как их значения значительно меньше значений тренда и временного ряда).
	* Разложение ряда на составляющие в соответсвие с мультипликативной моделью с помощью функции ```seasonal_decompose``` из библиотеки ```statsmodels```.
	* Отображение временного ряда, тренда, сезональности и остатка в соответствии с помощью метода ```plot``` объекта ```DataFrame``` из библиотеки ```Pandas``` (отдельно были отображены сезональность и остаток, так как их значения значительно меньше значений тренда и временного ряда).
	* Визуальная оценка полученных графиков на стационарность (определение: если ли тренд или нет).

1. Построение модели ```ARIMA``` для временного ряда, включала в себя следующие шаги:
	* Проверка ряда на интегрированность порядка ```k```, которая включает в себя следующие шаги:
		- Построение ряда первых разностей с помощью метода ```diff``` и ```dropna``` объекта ```DataFrame``` из библиотеки ```Pandas```.
		- Вычисления скользящего среднего и стандартного отклонения ряда первых разностей с помощью метода ```rolling``` объекта ```DataFrame``` и методов ```mean``` и ```std``` объекта ```Rolling``` из библиотеки ```Pandas``` (для рассчета брались результаты за два года).
		- Отображение ряда первых разностей и его статистик с помощью метода ```plot``` объекта ```DataFrame``` из библиотеки ```Pandas```.
		- Визуальная оценка стационарности (определение: если ли тренд или нет). Ряд оказался стационарен, следовательно, исходный временной ряд является интегрированным рядом порядка 1.
	* Поиск параметров ```p``` и ```q``` для модели ```ARIMA```, который включал в себя следующие шаги:
		- Построение графика автокорреляционной функции с помощью функции ```plot_acf``` из библиотеки ```statsmodels```.
		- Визуальная оценка графика для определения параметра ```q``` (для этого определяли до какого лага зависимость существенная).
		- Построение графика частично автокорреляционной функции с помощью функции ```plot_pacf``` из библиотеки ```statsmodels```.
		- Визуальная оценка графика для определения параметра ```p``` (для этого определяли до какого лага зависимость существенная).
	* Построение различных моделей ```ARIMA``` с помощью функции ```ARIMA``` и метода ```fit``` класса ```ARIMA``` из библиотеки ```statsmodels```.
	* Оценка моделей по критерию Акаике и коэффициенту детерминации на тренировочной выборке. Выбор лучшей модели. Этот пункт включал в себя следующие шаги:
		- Вычисление критерия Акаике с помощью библиотеки ```statsmodels``` (при построении модели он вычисляется автоматически).
		- Выбор лучшей модели.
		- Использование каждой модели для получения значений на тренировочной выборке с помощью метода ```predict``` объекта ```ARIMAResults``` из библиотеки ```statsmodels```.
		- Вычисление критерия детерминации с помощью функции ```r2_score``` из библиотеки ```sklearn```.
		- Выбор лучшей модели.
	* Загрузка тестовой выборки, из файла [testing.csv](https://github.com/GlebOlegovich/prac-2017-2018/blob/task2-mareev-meledin/submissions/task2/mareev-meledin/testing.csv) с помощью функции ```read_csv``` из библиотеки ```Pandas```.
	* Оценка моделей по критерию Акаике и коэффициенту детерминации на тестовой выборке. Выбор лучшей модели. Это пункт включал в себя следующие шаги:
		- Использование каждой модели для получения значений на тестовой выборке с помощью метода ```predict``` объекта ```ARIMAResults``` из библиотеки ```statsmodels```.
		- Вычисление критерия детерминации с помощью функции ```r2_score``` из библиотеки ```sklearn```.
		- Выбор лучшей модели.
	* Построение графиков моделей и тестовой выборки с помощью метода ```plot``` объекта ```DataFrame``` из библиотеки ```Pandas```.

## Инструкция по запуску
Открыть книгу **task2.ipynb** в Jupeter и выполнить: Cell -> Run All.

## Описание файлов
В каталоге с решением содержится четыре файла:
1. **task2.ipynb** - это Jupeter книга с решение задания.
1. **testing.csv** - тестовая выборка.
1. **training.csv** - тренировочная выборка.
1. **readme.md** - информация о выполненном задании (кто, что и как).

## Необходимое ПО

### Библиотеки языка Python
* **Pandas** - для работы с временными рядами (чтение, хранение, подсчет статистик и отображение).
* **Statsmodels** - для построение моделей ARIMA (подсчет статистик, построение, оценка).
* **Matplotlib** - для построения графиков.
* **Sklearn** - для вычисления критерия детерминации.
* **Seaborn** - для наведения красоты на графики.

### Программы
* Python 3.6
* Jupeter Notebook

## Работу выполними
**Меледин Станислав 312 группа** - [kvtvrvn](https://github.com/kvtvrvn) 
* Второй пункт задания.
* Советы по библиотеке **Pandas**.

**Мареев Глеб 312 группа** - [GlebOlegovich](https://github.com/GlebOlegovich) 
* Первый и третий пункты задания.
* Написание readme.
* Наведения красоты на графики.


## *Cпасибо,что прочли README, терерь вы понимаете на сколько ЭТО хрупкий механизм😂*
![](https://github.com/GlebOlegovich/Smthng/blob/master/nit.gif)

## **🎄С наступающим новым годом🎄**
![](https://github.com/GlebOlegovich/Smthng/blob/master/new-year-background-with-fireworks_23-2147703007.jpg)
