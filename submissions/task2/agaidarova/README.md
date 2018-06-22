Задание 2
======================
Краткое описание задания
---------------
1. Считать данные из `training.csv`. Проверить является ли ряд стационарным в широком смысле.
      Это можно сделать двумя способами:
      * Провести визуальную оценку, отрисовав ряд и скользящую статистику(среднее, стандартное отклонение). Постройте график на котором будет отображен сам ряд и различные скользящие статистики.
      * Провести тест Дики - Фуллера.
 Сделать выводы из полученных результатов. Оценить достоверность статистики.

2. Разложить временной ряд на тренд, сезональность, остаток в соответствии с аддитивной, мультипликативной моделями. Визуализировать их, оценить стационарность получившихся рядов, сделать выводы.

3. Проверить является ли временной ряд интегрированным порядка k. Если является, применить к нему модель ARIMA, подобрав необходимые параметры с помощью функции автокорреляции и функции частичной автокорреляции. Выбор параметров обосновать. Отобрать несколько моделей. Предсказать значения для тестовой выборки. Визуализировать их, посчитать r2 score для каждой из моделей. Произвести отбор наилучшей модели с помощью информационного критерия Акаике. Провести анализ получившихся результатов.

Доп. задания:
* соблюдение PEP8
* использование для визуализации библиотеки seaborn.

Теоретический материал
------------------------
Мы будем называть ***временным рядом*** совокупность наблюдений некоторой величины в различные моменты времени. При этом наблюдение может характеризовать в аднный момент времени или характеризовать промежуток времени.

Временной ряд называется *стационарным*, если его параметры (*период времени и уровень ряда*) не зависят от времени или же если отсутствует тренд. 

*Тренд* - это изменение, определяющее общее направление развития, т.е. грубо говоря общее направление графика ряда. Именно для определения визуальной оценки и нужно исследовать тренд у графика.

`E[y] = Const, D[y] = Const, Cov[yk, y(k-1)] = R(k)`

Если нарушается хотя бы одно из этих условий, то ряд называется нестационарным.

*Сезонность* - строго периодические и связанные с календарным периодом отклонения от трендa.

*Остаток* - это разница между предсказанным и наблюдаемым значением.

*Скользящая средняя* - это среднее арифметическое значений исходной функции за установленный период.

*Стандартное отклонение* - величина, показывающая, на сколько в среднем отклонился ряд от средней вариации ряда от среднего арифметического. 

*Замечание:* объединение cкользящей средней и стандартного отклонениия образует скользящие статистики.

### Тест Дики - Фуллера 

*Тест Дики - Фуллера* — это тест, используемый для анализа временных рядов на проверку стационарности.  Он проверяет ряд на наличие так называемых единичных корней. Временной ряд имеет единичный корень (хотя бы один), если его первые разности образуют стационарный ряд.

`y(t) ~ I(1)` , т.е. `Δy(t)=y(t)-y(t-1) ~ I(0)` ,

где `Δ` - разностный оператор, `I(j)` - означает, что ряд является интегрированным порядка `j`,
`I(0)` - ряд стационарен.

Каждый уровень временного ряда может формироваться из трендовой (Т), сезонной (S), а также случайной (E) компоненты.

Модели, где временной ряд представлен в виде суммы перечисленных компонентов называются аддитивными, если в виде произведения – мультипликативными моделями.

**Аддитивная модель** имеет вид : `Y = T + S + E`

Как найти *сезонность*? Необходимо найти скользящее среднее, от скользящего среднего найти еще раз скользящее среднее - получим центрированное скользящее среднее. Тогда

`Сезонность = Временной ряд - Центрированное скользящее среднее`

Как найти *тренд*? С помощью метода наименьших квадратов приближается временной ряд, что и позволяет найти тренд временного ряда.

Как найти *остаток*?

`Остаток = Временной ряд - Тренд - Сезонность`

**Мультипликативная модель** имеет вид: `Y = T * S * E`

Аналогично аддитивной модели:

`Сезонность = Временной ряд / Центрированное скользящее среднее`

`Остаток = Временной ряд / Сезональность / Тренд`


### Интегрированность ряда

Временной ряд называется **интегрированным порядка `k`**, если разности ряда k-го порядка `Δ^k x(t)` являются стационарными,
а разности меньшего порядка (и сам временной ряд) не являются стационарными рядами.

Вообще говоря, тест Дики-Фуллера проверяет значение коэффициента a в авторегрессионном уравнении 1-го порядка.

Оно имеет вид: `y(t) = a * y(t-1) + ε(t), ε(t)` - ошибка

   1. a=1 => есть единичные корни => стационарности нет
   2. |a|<1 => нет единичных корней => есть стационарность
   3. |a|>1 => не свойственно для временных рядов, которые встречаются в реальной жизни - требуется более сложный анализ
   
 
### Модель ARIMA

*AR- (autoregressive model)* — модель временных рядов, в которой значения временного ряда в данный момент линейно зависят от предыдущих значений этого же ряда. Авторегрессионный процесс порядка p (`AR(p)`-процесс) определяется следующим образом:
 
`Y_t = c + Σ(from i=1 to p)a_i * X_(t-i) + e_t`, 

где `a_i` - параматеры модели (коэффициенты авторегрессии), `c` — постоянная

*MA (moving average model)* - модель скользящего среднего, в которой моделируемый уровень временного ряда можно представить как линейную функцию прошлых ошибок, т.е. разностей между прошлыми фактическими и теоретическими уровнями.

`Y_t = Σ(from j=0 to q)b_j * e_(t-j)`, 

где `b_j` - параматеры модели



***ARIMA*** (*autoregressive integrated moving average*) - интегрированная модель авторегрессии - скользящего среднего - модель и методология анализа временных рядов.

Необходимо построить модель - `ARIMA(p, d, q)`,

где `p` - порядок `AR(p)`, `d` - порядок интегрированности, `q` - порядок `MA(q)`

`Δ^d(Y_t) = c + Σ(from i=1 to p) * a_i * Δ^d(Y_(t-1)) + Σ(from j=1 to q)b_j * e_(t-j)`

***R2 score***: *коэффициент детерминации (R^2)* - доля дисперсии зависимой переменной, объясняемая рассматриваемой моделью зависимости.

Лучший результат, который может дать R2 score - это 1.0.

***AIC***: информационный критерий (AIC) - критерий, применяющийся исключительно для выбора из нескольких статистических моделей. 

Реализация решения
--------------------
1. Читаем данные из `training.csv`

2. Вычисляем скользящее среднее и стандартное отклонение с помощью команд вида `ts.rolling().mean()` , `ts.rolling().std()` - 

3. Проводим тест Дики-Фуллера функцией вида `ts.adfuller()` , анализируем полученные из функции параметры и делаем вывод о стационарности ряда

4. Визуализируем тренд, сезонность и остаток, прогоняя через тест Дики-Фуллера для стационарности.
С помощью функции `seasonal_decompose` раскладываем временной ряд на тренд, сезонность и остаток.

`seasonal_decompose(data.Value, model)`, где `data.Value` - столбец значений временного ряда, `model` - отвечает за рассмотрение моделей 'additive' или ‘multiplicate’

Возвращает decompose:
 * -.trend - тренд исходного ряда
 * -.resid - остаток исходного ряда
 * -.seasonal - сезонность исходного ряда
 
 5. Ищем коэффициент интегрируемости ряда `order` основываясь также на результатах теста Дики-Фуллера
 
 6. Подбираем нужные параметры с помощью функции автокорреляции и функции частичной автокорреляции и визуализируем
      
      Функция вида `sm.graphics.tsa.plot_acf(ts, lags, ax)` находит и визуализирует автокорреляцию временного ряда,

    `ts` - временной ряд, `lags` - число лагов для автокорреляции, `ax` - параметр для построения подграфика
   
   Для частичной автокорреляции аналогично только для функции  -pacf-

7. Cтроим модель ARIMA на основе временного ряда ts с помощью функции вида `ARIMA()`.  Стром график, на котором изображены данные из файла `testing.csv`. Считаем R2 - коэффициент детерминации, чтобы понять какой процент наблюдений описывает данная модель и критерий Акаике (AIC). 

Используемые библиотеки
---------------------

* Pandas (для работы с временными рядами)
* Numpy (для работы с массивами)
* Matplotlib.pylab (для визуализации графиков)
* Statsmodels (для использования статистических функций и постороения модели ARIMA)
* Sklearn.metrics (для нахождения метрики R2-score)

Необходимые программые
---------------
Оболочка Jupyter (вызываем в окне терминала комндой `jupyter notebook`)

Инструкции по запуску
-----------------
Cell -> Run All



Выполнила
-------------
Агайдарова Айганым, 311 гр.



