class quicksort():
    def __init__(self,listaOrdenar):
        self.listaOrdenar = listaOrdenar
        self.p = 0
        self.r = (len(listaOrdenar)-1)
        self.quicksort(listaOrdenar,self.p, self.r)

    def quicksort(self,listaOrdenar,p,r):
    #condicao de parada( ou de existencia)
        if p < r:
            q = self.particionar(listaOrdenar, p, r)
            self.quicksort(listaOrdenar, p, q-1)#pivotar a esquerda(ordenar menor q pivo)
            self.quicksort(listaOrdenar, q+1, r)#pivotar a direita(ordenar maior q pivo)
    def particionar (self,listaOrdenar, p, r):
        l = listaOrdenar[r]#primeiro elemento a esq
        j = p-1
        for i in range(p, r+1, 1):
             if listaOrdenar[i] <= l:
                 j += 1
                 if j<i:
                     z = listaOrdenar[j]
                     listaOrdenar[j] = listaOrdenar[i]
                     listaOrdenar[i] = z
        return j
 
def splitInt(lista):
    lista1 = lista.split(' ')
    lista2 = []
    for x in lista1:
        lista2.append(int(x))
    return lista2

t = int(input(''))
for i in range(t):
    string = ''
    lista = input('')
    listaComInteiro = splitInt(lista)
    quicksort(listaComInteiro)
    for x in range(0, len(listaComInteiro)):
        if x == len(listaComInteiro)-1:
            string+=str(listaComInteiro[x])
        else:
            string+=str(listaComInteiro[x])+' '
    
    print(string)