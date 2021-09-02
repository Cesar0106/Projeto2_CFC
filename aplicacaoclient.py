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
import random
import numpy as np

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
serialName = "/dev/ttyACM0"            # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
#serialName = "COM7"                  # Windows(variacao de)
def command():   
    comando1 = [b'\xFF',b'\x00']
    comando2 = b'\xFF'
    comando3 = b'\x00'
    comando4 = b'\xF0'
    comando5 = b'\x0F'
    comando6 = [b'\x00',b'\xFF']
    cs = [comando1,comando2,comando3, comando4, comando5, comando6]
    nc = int(input("How many commands"))
    i = 0
    cl = []
    while i != nc:
        cl.append(random.choice(cs))
        i += 1
    cl.append("EE")#Comando que finaliza leitura
    return cl

def main():
    try:
        timei = time.time()
        com1 = enlace(serialName)
        print("Comunicação com client aberta")
        com1.enable()
        txBuffer = command()
        print(txBuffer)
        print(len(txBuffer))
        
        print("Começo da Transmissão")
        bytesize = (-1)
        for comando in txBuffer:
            if len(comando) == 2:
                numBytes = 1
            else:
                numBytes = 2
            print("numBytes enviado")
            com1.sendData((numBytes).to_bytes(2, byteorder = "big"))
            bytesize += numBytes
            print("comando enviado")
            com1.sendData(np.asarray(comando))

        print(bytesize)
        txSize = com1.tx.getStatus()
        print("Recepção vai Comear")
        txLen = len(txBuffer)
        rxBuffer, nRx = com1.getData(txLen)
        print(com1.rx.getBufferLen())
        print("recebeu {}" .format(rxBuffer))
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
