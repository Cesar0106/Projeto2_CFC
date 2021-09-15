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
        print("-------------------------")
        print("Recepção vai Comear")
        print("-------------------------")
            
        tamComando, nRx = com1.getData(2)
        print("tamanho do comando", tamComando) 
        intc = int.from_bytes(tamComando, byteorder="big")
        print("Client enviou ", intc)
        com1.sendData(tamComando)
        comandos, nRx = com1.getData(intc)
        print(comandos)
        lista = []
        for i in comandos:
            if i == '\x01':
                lista.append([comandos[i]])
            elif i == '\x02':
                lista.append([comandos[i]+ comandos[i+1]])
            else:
                continue
        com1.sendData(comandos)    
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
