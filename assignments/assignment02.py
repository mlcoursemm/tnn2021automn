
def ROCAUC():
    return 0.5
    
def ROC():
    return [(0.0, 0.0), (0.0,1.0), (1.0, 1.0)]

def a(x):
    return -1
    

if __name__ == '__main__':

    with open('assignment02_task1.txt', 'w') as f:
        f.write('%.3f' % ROCAUC())

    with open('assignment02_task2.txt', 'w') as f:
        for i in range(-50, 50):
            x1 = i/10.0
            for j in range(-50, 50):
                x2 = j/10.0
                y = a([x1, x2])
                f.write('%d ' % y) 
    