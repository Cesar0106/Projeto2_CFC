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
#   python3 -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
serialName = "/dev/ttyACM0"            # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
#serialName = "COM7"                  # Windows(variacao de)
def command():   
    comando1 = b'\xFF\x00'
    comando2 = b'\xFF'
    comando3 = b'\x00'
    comando4 = b'\xF0'
    comando5 = b'\x0F'
    comando6 = b'\x00\xFF'
    cs = [comando1,comando2,comando3, comando4, comando5, comando6]
    nc = int(input("How many commands"))
    i = 0
    cl = []
    while i != nc:
        cl.append(random.choice(cs))
        i += 1
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
        var1 = 1
        var2 = 2
        lista = []
        print("Começo da Transmissão")
        for comando in txBuffer:
            if len(comando) == 1:
                #lista.append(var1.to_bytes(1, 'big'))
                lista.append(comando)
            else:
                #lista.append(var2.to_bytes(1, 'big'))
                lista.append(comando)
        com1.sendData(len(lista).to_bytes(2, 'big'))
        print('Enviamos:', len(lista).to_bytes(2, 'big'))
        time.sleep(0.1)
        tamanho, nRx = com1.getData(2)
        print("Servidor recebeu :",tamanho)
        if tamanho == len(lista).to_bytes(2, 'big'):
            time.sleep(0.3)
            com1.sendData(np.asarray(lista))
            print(lista)
        else: 
            print('enviou lista errada')

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
