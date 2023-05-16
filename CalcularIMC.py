class IMC:
    def calcular(self, peso, altura):
        imc = peso / (altura ** 2)
        return imc

    def classificar(self, imc):
        if imc < 18.5:
            return "Magreza"
        elif 18.5 <= imc <= 24.9:
            return "Normal"
        elif 25.0 <= imc <= 30:
            return "Sobrepeso"
        else:
            return "Obesidade"


def main():
    calculadora = IMC()

    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))

    imc = calculadora.calcular(peso, altura)
    classificacao = calculadora.classificar(imc)

    print("IMC:", imc)
    print("Classificação:", classificacao)


if __name__ == "__main__":
    main()