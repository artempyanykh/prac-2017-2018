import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def spectrum(P):
    t = 0
    for i in range(len(P)):
        if P[i] > 0 :
         t += 1
    if t == len(P):
        return "Спектр полон"
    elif t == 1 :
        return "Спектр состоит из одной точки"
    else :
        return "Спектр неполон"

def graph(P,Q):
    fig1 = plt.figure()                
    plt.axis([0, len(P) + 1, 0, 1.1])  # деления на осях в заданных промежутках
    for i in range(1, len(P) + 1, 1):
        plt.plot([i, i], [0.0, P[i-1]], 'b', lw = 0.6, alpha = 0.4)
        plt.scatter(i, P[i-1], s = 20, color = 'b')
    plt.xlabel('Стратегии', family = "serif")
    plt.ylabel('Вероятности', family = "serif")
    plt.minorticks_on()                   # мелкие деления на осях
    
 
    a = spectrum(P)
    b = 'Спектр первого игрока ' + '('  + a + ')'
    plt.title(b, family = "serif")
    plt.savefig('out/fig1.png')
 #   plt.show()
     
    
    fig2 = plt.figure()
    plt.axis([0, len(Q) + 1, 0, 1.1])
    for j in range(1, len(Q) + 1, 1):
        plt.plot([j,j], [0, Q[j-1]], 'b', lw = 0.6, alpha = 0.4)
        plt.scatter(j, Q[j-1], s = 20, color = 'b')
    plt.xlabel('Стратегии', family = "serif")
    plt.ylabel('Вероятности', family = "serif")
    plt.minorticks_on()

    a = spectrum(Q)
    b = 'Спектр второго игрока ' + '('  + a + ')'
    plt.title(b, family = "serif")
    plt.savefig('out/fig2.png')
 #   plt.show()