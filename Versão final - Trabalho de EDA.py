class No:
  def __init__(self, chave):
      self.valor = chave
      self.prox = None
      self.esq = None
      self.dir = None

class Pilha_Encad:
  def __init__(self, chave):
      self.base = None
      self.topo = None
      self.tamanho = 0
      self.Empilhar(chave)

  def Empilhar(self, chave):
      novo = No(chave)
      novo.prox = self.topo
      self.topo = novo
      self.tamanho += 1

  def Desempilhar(self):
      if self.tamanho == 0:
          print('A lista está vazia.')
      else:
          print(self.topo.valor)
          aux = self.topo
          self.topo = self.topo.prox
          self.tamanho -= 1
          del aux

#Codigo da Arvore Binaria

class ArvoreBinaria:
  def __init__(self):
      self.raiz = None

  def busca(self, pont, chave, f):
      if pont is None:
          f = 0
      else:
          if chave == pont.valor:
              f = 1
          else:
              if chave < pont.valor:
                  if pont.esq is None:
                      f = 2
                  else:
                      pont, f = self.busca(pont.esq, chave, f)
              else:
                  if pont.dir is None:
                      f = 3
                  else:
                      pont, f = self.busca(pont.dir, chave, f)
      return pont, f

  def inserir(self, chave):
    if self.raiz is None:
        novo = No(chave)
        novo.esq = None
        novo.dir = None
        self.raiz = novo
    else:
        pont = self.raiz
        f = None
        pont, f= self.busca(pont, chave, f)
        if f == 1:
            print("Elemento já Existe!")
        else:
            novo = No(chave)
            novo.esq = None
            novo.dir = None
            if f == 2:
                pont.esq = novo
            else:
                pont.dir = novo

  def excluir(self, chave):
      f = None
      pont, pai, f = self.busca_pai(self.raiz, None, chave, f)
      if pont is not None:
          if pont.esq is None:
              if pont == self.raiz:
                  self.raiz = pont.dir
              else:
                  if pont == pai.esq:
                      pai.esq = pont.dir
                  else:
                      pai.dir = pont.dir
          else:
              if pont.dir is None:
                  if pont == self.raiz:
                      self.raiz = pont.esq
                  else:
                      if pont == pai.esq:
                          pai.esq = pont.esq
                      else:
                          pai.dir = pont.esq
              else:
                  pont_aux = pont.dir
                  pai_aux = pont

                  while pont_aux.esq is not None:
                      pai = pont_aux
                      pont_aux = pont_aux.esq
                  if pai_aux != pont:
                      pai_aux.esq = pont_aux.dir
                      pont_aux.dir = pont.dir
                  pont_aux = pont.esq
                  if pont == self.raiz:
                      self.raiz = pont_aux
                  else:
                      if pai.esq == pont:
                          pai.esq = pont_aux
                      else:
                          pai.dir = pont_aux
          del pont
          print("Chave excluída")
      else:
          print("Chave não encontrado!")

  def busca_pai(self, pont, pai, chave, f):
        if pont is None:
            f = 0
        else:
            if chave == pont.valor:
                f = 1
            else:
                if chave < pont.valor:
                    pai = pont
                    pont, pai, f = self.busca_pai(pont.esq, pai, chave, f)
                else:
                    pai = pont
                    pont, pai, f = self.busca_pai(pont.dir, pai, chave, f)

        return pont, pai, f

  def percurso(self):
      pont = self.raiz
      pilha = Pilha_Encad(pont)
      pilha.Empilhar(pont)
      
      while (pont is not None) and (pilha.topo is not None):
          pont = pilha.Desempilhar()
          print (pont.valor)
      
      if (pont.dir is not None):
          pilha.Empilhar(pont.dir)
      if (pont.esq is not None):
          pilha.Empilhar(pont.esq)

      
  def mostrar_arvore(self, pont, nivel=0):
        if pont is not None:
            self.mostrar_arvore(pont.dir, nivel + 1)
            print(" " * 4 * nivel + "->", pont.valor)
            self.mostrar_arvore(pont.esq, nivel + 1)
            
arv = ArvoreBinaria()
print("------------------------- Programa Árvore Binária ----------------------------------")
op = True

while op == True:
  print("*************************************************************")
  print("1°) Inserir Elemento")
  print("2°) Exclusão de Elemento")
  print("3°) Busca Elemento")
  print("4°) Exibir Árvore Binária")
  print("5°) Pecorrer Árvore Binária - Pré-Ordem")
  print("6°) Sair do programa")
  print("**************************************************************")

  op = int(input("Informe uma opção:"))
  if op == 1:
      chave = int(input("Informe o valor:"))
      arv.inserir(chave)
  elif op == 2:
      chave = int(input("Informe o valor:"))
      arv.excluir(chave)
      op = True
      
  elif op == 3:
    f = None
    chave = int(input("Informe o valor: "))
    pont, pai, f = arv.busca_pai(arv.raiz, None, chave, f)
    if pont is None:
        print("Chave não encontrada!")
    else:
        print("Chave encontrada!")
    op = True   
  elif op == 4:
      arv.mostrar_arvore(arv.raiz)
      op = True
  elif op == 5:
      arv.percurso()
  elif op == 6:
      op = False
  else:
      print("Opção Inválida!")
      op = True
