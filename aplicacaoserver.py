#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 


from enlace import *
import time
import numpy as np

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
serialName = "/dev/ttyACM1"            # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
#serialName = "COM7"                  # Windows(variacao de)


def main():
    try:
        timei = time.time()
        com1 = enlace(serialName)
        print("Comunicação com client aberta")
        com1.enable()
        intc = 0
        lista=[]
        comando = b'\xAA'
        print("Recepção vai Comear")
        while comando != b'\xee':
            tamComando, nRx = com1.getData(1)
            time.sleep(0.3)
            print("tamanho do comando", tamComando)
            intc = int.from_bytes(tamComando, byteorder="big")
            print(intc)
            if intc ==2 :
                comando, nRx = com1.getData(2)
                print("pegou o comando{0}".format(comando))
                lista.append(comando)
            elif intc ==1 :
                comando, nRx = com1.getData(1)
                print("pegou o comando{0}".format(comando))
                lista.append(comando)
            else:
                print("Achou fim")
                print(lista)

        
        timef = time.time()
        print(timef-timei)


        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
