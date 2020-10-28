
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #PINAGEM DA PLACA (1-40)
GPIO.setup(40, GPIO.OUT) #PINO 40 MODO SAÍDA

GPIO.output(40, 1)

time.sleep(3)

GPIO.output(40, 0)

GPIO.cleanup() #LIMPA GPIO