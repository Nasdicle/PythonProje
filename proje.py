1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 
Örnek olarak:
x: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
y: []
 for z in x:
  if type(z)== int:
    x.append(x)
  elif type(z) != int:
    x.extend(x)

2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine 
döndürün. Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
         
def Ters(liste):
    liste.reverse()
    return liste
 print(Ters(liste))
         
