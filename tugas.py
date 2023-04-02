import math

def linear_naik(a, b, x):
    if x <= a:
        return 0
    elif x >= b:
        return 1
    else:
        return (x-a)/(b-a)

def linear_turun(a, b, x):
    if x <= a:
        return 1
    elif x >= b:
        return 0
    else:
        return (b-x)/(b-a)

def segitiga(a, b, c, x):
    if x <= a or x >= c:
        return 0
    elif x == b:
        return 1
    elif x < b:
        return (x-a)/(b-a)
    else:
        return (c-x)/(c-b)

def trapesium(a, b, c, d, x):
    if x <= a or x >= d:
        return 0
    elif x >= b and x <= c:
        return 1
    elif x < b:
        return (x-a)/(b-a)
    else:
        return (d-x)/(d-c)

def sigmoid(a, c, x):
    return 1/(1 + math.exp(-a*(x-c)))

def gauss(a, c, sigma, x):
    return math.exp(-(a*(x-c))**2/(2*sigma**2))

def beta(a, b, alpha, beta, x):
    return ((x-a)**(alpha-1)*(b-x)**(beta-1))/((b-a)**(alpha+beta-1)*math.gamma(alpha)*math.gamma(beta))

# main program
while True:
    print("\nPilih fungsi keanggotaan yang ingin dihitung:")
    print("1. Linear Naik")
    print("2. Linear Turun")
    print("3. Segitiga")
    print("4. Trapesium")
    print("5. Sigmoid")
    print("6. Gauss")
    print("7. Beta")
    print("8. Keluar")

    choice = int(input("Masukkan pilihan: "))

    if choice == 1:
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        x = float(input("Masukkan nilai x: "))
        print(f"Hasil: {linear_naik(a, b, x)}")
    elif choice == 2:
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        x = float(input("Masukkan nilai x: "))
        print(f"Hasil: {linear_turun(a, b, x)}")
    elif choice == 3:
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        c = float(input("Masukkan nilai c: "))
        x = float(input("Masukkan nilai x: "))
        print(f"Hasil: {segitiga(a, b, c, x)}")
    elif choice == 4:
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        c = float(input("Masukkan nilai c: "))
        d = float(input("Masukkan nilai d: "))
        x = float(input("Masukkan nilai x: "))
        print(f"Hasil: {trapesium(a, b, c, d, x)}")
    elif choice == 5:
        a = float(input("Masukkan nilai a: "))
        c = float(input("Masukkan nilai c: "))
        x = float(input("Masukkan nilai x: "))
        print(f"Hasil: {sigmoid(a, c, x)}")
    elif choice == 6:
        a = float(input("Masukkan nilai a: "))
        c = float(input("Masukkan nilai c: "))
        sigma = float(input("Masukkan nilai sigma: "))
        x = float(input("Masukkan nilai x: "))
        print(f"Hasil: {gauss(a, c, sigma, x)}")
    elif choice == 7:
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        alpha = float(input("Masukkan nilai alpha: "))
        beta = float(input("Masukkan nilai beta: "))
        x = float(input("Masukkan nilai x: "))
        print(f"Hasil: {beta(a, b, alpha, beta, x)}")
    elif choice == 8:
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.") 

    
