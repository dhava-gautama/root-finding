import numpy as np #Mengimport numpy

def bisection(f,atas,bawah,batas_iterasi):
    if f(atas)*f(bawah) < 0:
        for j in range(1,batas_iterasi+1):
            tengah = (atas + bawah)/2
            if f(atas)*f(tengah) < 0:
                atas = atas
                bawah = tengah
            elif f(bawah)*f(tengah) < 0:
                atas = tengah
                bawah = bawah
            elif f(tengah) == 0:
                return tengah
    else:
        print("Nilai kali fungsi atas dan fungsi bawah lebih dari nol!")
    return (atas + bawah)/2
    
def f(x): #Membuat fungsi
    fungsi=(np.exp(x)-(5*(x**2))) # Mendefinisikan fungsi
    return fungsi #Mengembalikan hasil fungsi
    
bisection(f,0,1,10)
