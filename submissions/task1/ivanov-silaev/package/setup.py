from setuptools import setup

setup(name='nash_equilibrium', 		#Имя пакета.
      version='1.0.0',         		#Версия пакета.
      license='MIT',           		#Лицензия распространения.
      packages=['nash_equilibrium'],#Пакеты.
      zip_safe=False,               #Запрет на установку пакета в качестве архива.
      long_descriptions = open('README.txt').read(), #Описание пакета.
      )