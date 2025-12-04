def Pascal(k):
    if k == 0:
        return [1]
    else:
        p = [1]
        previous_p = Pascal(k - 1)
        for i in range(len(previous_p) - 1):
            p.append(previous_p[i] + previous_p[i + 1])    
        p.append(1)
        return p

def main():
    k = int(input('Введите число: '))
    for i in range(k):
        print(Pascal(i))

if __name__ == "__main__":                              #Выполнение кода, если он запущен как самостоятельный файл
    main()
