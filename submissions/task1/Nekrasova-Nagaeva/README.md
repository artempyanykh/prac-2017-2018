  Постановка задачи
====================
  В этом задании необходимо было решить антагонистическую матричную игру, проиллюстрировать решение некоторых примеров, оформить решение в виде пакета и написать unit-тесты для функции nash_equilibrium.
 
  Игрой называется тройка <N, {Si} i из N, {Hi} i из N>, где N = {1,2, ..., n} - множество занумерованных игроков, Si - множество возможных действий i-го игрока; s = (s1,...,sn) - ситуация, si из Si, Hi(s) называется функцией выигрыша игрока i. 

  Матричная игра называется антагонистической, если в ней участвуют два игрока и значения функций выигрыша в каждой ситуации равны по величине и противоположны по знаку.

Решением матричной игры называется процесс нахождения ее значения и оптимальных стратегий игроков.

Чистой стратегией игрока называется  стратегия, однозначно выбираемая игроком.

Смешанной стратегией игрока называется произвольное распределение вероятностей на множестве его чистых стратегий.

Любую матричную игру можно свести к паре двойственных друг другу задач линейного программирования. Благодаря этому становится возможным применение симплекс-метода для решения матричных игр.

Необходимо минимизировать F = x1+...+xm = 1/V , где V - выигрыш, xi = pi/V , а pi - компоненты вектора стратегии первого игрока. Аналогично необходимо максимизировать F = y1+...yn = 1/V , где yi = qi/V , а qi - компоненты вектора стратегии второго игрока.  Считаем V>0, иначе прибавляем ко всей матрице M>0, что не меняет оптимальных стратегий игроков и увеличивает решение на M.
При этом имеется система неравенств: a1j * x1 + … amj * xm >= 1 для всех j от 1 до n в первом случае и  ai1 * y1 + … ain * yn <= 1 для всех i от 1 до m во втором. При этом все xi,yj >= 0.  

Воспользуемся функцией linprog, которая решает задачу минимизации при ограничениях системы неравенств вида = и <= и ограничений самих  переменных. Для сведения первого случая к минимизации, F и систему неравенств  домножаем на (-1). 

Получаем вектор-решение и значение функции F. Выигрыш V = 1/ (значение функции F) - M. 

Спектром смешанной стратегии игрока в конечной антагонистической игре называется множество всех его чистых стратегий, вероятность которых согласно этой стратегии положительна.

Решение задачи
==============
Решение матричной игры:
-----------------------

### Запуск программы(через терминал):

Находясь в директории, содержащей файл main.py, директории in и out и пакет matrix_game, запускаем питон:

			python3
      
Чтобы воспользоваться функцией main, сообщаем о ней интерпретатору:

			from main import main
      
Запускаем

			main(‘in/example_1.in’, ‘out/1.out’)

Потребуются библиотеки numpy, scipy и matplotlib

			sudo pip3 install numpy
			sudo pip3 install scipy
			sudo pip3 install matplotlib

### Структура программы:

1. Главная функция - ***main(fin, fout)*** , где ***fin*** - файл с матрицей игры, ***fout*** - файл, содержащий результаты программы: построчно - цена игры, стратегия первого игрока, стратегия второго. Файлы для fin лежат в папке ‘in’, fout сохраняются в ‘out’

***H = np.loadtxt(fin)***	-	получаем представление матрицы игры в виде списка
(Функция ***loadtxt()*** построчно преобразует текстовый файл в массив. Каждая строка в файле должна иметь одинаковое количество значений.)

***sol = nash_equilibrium(H)***	-	в результате работы функции в sol[0] цена игры, в sol[1] - стратегия первого игрока, в sol[2] - стратегия второго игрока

***graph(sol[1], sol[2])***		-	вызываем graph для визуализации результатов

2. Функция ***nash_equilibrium(a)*** получает на вход матрицу игры, сводит нахождение стратегий игроков к паре задач линейного программирования: максимизирует минимальный выигрыш первого игрока и минимизирует максимальный выигрыш второго

***m = a.shape[0]***	-	в матрице m строк - количество чистых стратегий первого игрока

***c = np.ones((m))***	-	создаем стобец длины m, заполняем его “1” 

***A_ub = a.T***		-	транспонируем матрицу игры
                                    
***res = linprog(c, A_ub, b_ub)***	 -	с помощью функции linprog получаем решение задачи:

𝑐𝑇*𝑥 → 𝑚𝑖𝑛

𝐴_𝑢𝑏*𝑥 ≤ 𝑏_𝑢𝑏 

𝐴_𝑒𝑞*𝑥 = 𝑏_𝑒𝑞 

𝑥 ≥ 0

3. Функция ***graph(P, Q)***  - строит графики, визуализирующие оптимальные стратегии игроков.

***fig1 = plt.figure()***	-	создаем график для первого игрока

***plt.axis([0, len(P) + 1, 0, 1.1])***		-	деления на осях в заданных промежутках

***plt.plot([i, i], [0.0, P[i-1]], 'b', lw = 0.6, alpha = 0.4)***	-	рисуется столбец от координаты i до i по оси x, от 0 до значения функции по оси y, цветом “b”, прозрачностью alpha, толщиной lw 
 
***plt.scatter(i, P[i-1], s = 20, color = 'b')***			-	рисуется точка, размером “20” и цветом “b”

***plt.xlabel('Стратегии', family = "serif")***	-	подпись оси x шрифтом “serif”

***plt.minorticks_on()***	-	мелкие деления на осях

***plt.title(b, family = "serif")***	-	написание заголовка шрифтом “serif”

***plt.show()***	-	вывод изображения на экран

4. Функция ***spectrum(P)***  - по заданной стратегии P определяет тип спектра:

Спектр, состоящий из одной точки - только для одной чистой стратегии игрока вероятность положительна. Полный спектр - вероятность каждой чистой стратегии положительна. Неполный спектр - существует такая чистая стратегия, вероятность которой 0.

Тестирование:
---------------

Для тестирования нам потребуется пакет python-nose, его установка:

   		 pip3 install python-nose
  
Запускаем тесты:

  		nosetests -v unit_test.py
  
Структура тестов:

Каждая функция по соглашению должна начинаться со слова "test", т.е иметь вид ***“test_*** SOMETHING” . Задача каждого теста - определить, верны ли результаты функции для конкретных входных данных, путем сравнения этих результатов с точными (полученными другим методом).

Пакет:
---------

Пакеты используются для хранения модулей - в нашем случае, файлов nash_equilibrium.py и graph.py. Пакет matrix_game кроме этих модулей содержит файл __ init __ .py, в котором прописано из какого модуля мы импортируем какую функцию при подключении этого пакета. Строчка from … import *  позволяет использовать все прописанные в __ init __ .py функции.

Работа с графической веб-оболочкой ***Jupyter*** 
--------------------------------------------------

Файл ***main_1.ipynb*** реализует то же, что и ***main.py*** , для запуска из командной строки пропишем

		jupyter notebook main_1.ipynb 
	
Если jupyter не установлен, делаем

		pip3 install jupyter	

Задание выполняли Некрасова Мария и Нагаева Варвара, группа 312
----------------------------------------------------------------

Некрасова Мария:

* Функция nash_equilibrium()

* Работа с графиками

* Тесты для unit-тестов

* Примеры входных данных для получения различных спектров


Нагаева Варвара:

* Работа с графиками

* Тестирование, тесты

* Пакеты

* Примеры входных данных для получения различных спектров

