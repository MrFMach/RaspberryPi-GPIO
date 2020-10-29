
import RPi.GPIO as gpio
import time

# Todo o código no bloco try para tratamento de erros
try:
    
    # Desativa os avisos da GPIO
    gpio.setwarnings(False)
    # Referecia pela pinagem da placa (1-40)
    gpio.setmode(gpio.BOARD)
    # Configuração das saídas
    gpio.setup(31, gpio.OUT, initial=gpio.LOW)
    gpio.setup(33, gpio.OUT, initial=gpio.LOW)
    gpio.setup(35, gpio.OUT, initial=gpio.LOW)
    gpio.setup(37, gpio.OUT, initial=gpio.LOW)
    # Configuração das entradas
    gpio.setup(3, gpio.IN)
    gpio.setup(5, gpio.IN)
    gpio.setup(7, gpio.IN)


    while 1:
        
        if gpio.input(3) == False:
            print("Botão 3 pressionado")
            gpio.output(33, 1)
            time.sleep(0.1)
            gpio.output(33, 0)
            time.sleep(0.1)

        elif gpio.input(5) == False:
            print("Botão 5 pressionado")
            gpio.output(37, 1)
            time.sleep(0.1)
            gpio.output(37, 0)
            time.sleep(0.1)
     
        elif gpio.input(7) == False:
            print("Botão 7 pressionado")
            gpio.output(35, 1)
            time.sleep(0.1)
            gpio.output(35, 0)
            time.sleep(0.1)
        else:
            print("Nenhum botão pressionado")
            gpio.output(31, 1)
            time.sleep(0.3)
            gpio.output(31, 0)
            time.sleep(0.3)

# Se pressionar Ctrl+C, executa o que está no 'except' e vai para 'finally'
except KeyboardInterrupt:
    print ("Você saiu do programa")
    
finally:
    gpio.cleanup()
