# pip install googletrans==3.1.0a0

import googletrans

class Tradutor():
    def __init__(self, frase, lingua):
        self.frase = frase;
        self.lingua = lingua;
        self.tradutor = googletrans.Translator()
    
    def traduzir(self):
        traducao = self.tradutor.translate(self.frase, dest=self.lingua)
        return traducao.text

    def mostrar_traducao(self):
        print("\n - Frase original:", self.frase)
        print(f"\n - Frase traduzida para '{self.lingua}':", self.traduzir())
        
if __name__ == '__main__':
    sentenca = str(input(" - Digite uma frase: "))
    obj_tradutor = Tradutor(sentenca, "en")
    obj_tradutor.mostrar_traducao()
