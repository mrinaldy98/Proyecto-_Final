from  pycreate2 import Create2
import time
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
port = '/dev/ttyUSB0' 
bot = Create2(port)
bot.start()
bot.full()
NRX = 6
NRY = 6
a = 3 #adelante
at = 1 #atras
i = 2 #izquierda
d = 4 #derecha
x = 0
y = 0
x1 = 0
y1 = 0
toque = 0
sensorizq=19
sensorder=16
sensorcolor=20
GPIO.setup(sensorcolor,GPIO.IN)
GPIO.setup(sensorizq,GPIO.IN)
GPIO.setup(sensorder,GPIO.IN)
sensors = bot.get_sensors()
print(sensors.battery_charge)

while(1):
    sensor1 = GPIO.input(sensorizq)
    sensor2 = GPIO.input(sensorder)

    
    if GPIO.input(sensorcolor) == 0:
        pos1 = 1
        pos2 = 1
        pos3 = 1 
        sensor1 = GPIO.input(sensorizq)
        sensor2 = GPIO.input(sensorder)
    
        if sensor1 == 1 and sensor2 == 1:
            
                
            bot.drive_straight(200)
            time.sleep(1)
            bot.drive_straight(1)
            time.sleep(2)
    ################################################################################################
            if x == 0 and y == 0:
                print("X =",x)
                print("Y =",y)
                if x1 == 0 and y1 == 1:
                #viene de la derecha
                    direc = 3
                    a = 4 
                    at = 2
                    i = 3
                    d = 1
                elif x1 == 1 and y1 == 0 :
                #viene de abajo
                    direc = 2
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == 0 and y1 == 0:
                #primer movimiento
                    direc = random.choice((2,3))
                    at = 1
                    i = 2
                    a = 3
                    d = 4
                    
                x1 = x
                y1 = y
                print("direc = ",direc)
                
                if direc == 2:
                    
                    y = y + 1
                    x = x
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)                        
                             
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
    
                
                elif direc == 3:
                    
                    y = y
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
    
    ########################################################################################################################
            if x == NRX-1 and y == 0:
                print("X =",x)
                print("Y =",y)
                if x1 == x-1 and y1 == y:
                    direc = 2 
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x and y1 == y+1:
                    direc = 1
                    a = 4
                    at = 2
                    i = 3
                    d = 1
                    
                x1 = x
                y1 = y
                print("direc = ",direc)
    
                if direc == 1:
                    
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 2:
                    
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
    #######################################################################################################################
            if x == NRX-1 and y == NRY-1:
                print("X =",x)
                print("Y =",y)
                if x1 == x and y1 == y-1:
                    direc = 1    
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x-1 and y1 == y :
                    direc = 4
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                    
                x1 = x
                y1 = y
                
    
                print("direc = ",direc)
                if direc == 1:
                    
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                elif direc == 4:
                    
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
    ########################################################################################################################
            if x == 0 and y == NRY-1:
                print("X =",x)
                print("Y =",y)
                if x1 == x+1 and y1 == y:
                    direc = 4
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = 3
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                    
                x1 = x
                y1 = y
                
    
                print("direc = ",direc)
                if direc == 3:
                    
                    y = y 
                    x = x - 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
    
                elif direc == 4:
                    
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
    ########################################################################################################################
            if x == 1 and y == 1:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                               

########################################################################################################################################
            if x == 1 and y == 2:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                              

########################################################################################################################################
            if x == 1 and y == 3:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
########################################################################################################################################
            if x == 1 and y == 4:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

########################################################################################################################################
            if x == 2 and y == 1:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                              

########################################################################################################################################
            if x == 2 and y == 2:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                              

########################################################################################################################################
            if x == 2 and y == 3:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

########################################################################################################################################
            if x == 2 and y == 4:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

                              

########################################################################################################################################
            if x == 3 and y == 1:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

                         

########################################################################################################################################
            if x == 3 and y == 2:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

                            

########################################################################################################################################
            if x == 3 and y == 3:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

                           

########################################################################################################################################
            if x == 3 and y == 4:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

                             

########################################################################################################################################
            if x == 4 and y == 1:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)


########################################################################################################################################
            if x == 4 and y == 2:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

                             

########################################################################################################################################
            if x == 4 and y == 3:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

                            

########################################################################################################################################
            if x == 4 and y == 4:
                print("X =",x)
                print("Y =",y)
                
                if x1 == x-1 and y1 == y: 
                #viene de arriba
                    direc = random.choice((2,3,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x+1 and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == y-1:
                    direc = random.choice((1,3,4))
                #viene de izquierda
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == y+1:
                #viene de derecha
                    direc = random.choice((1,2,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1           
   
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)   
                            
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                                
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)


########################################################################################################################################

            if x == 1 and y == 0:
                print("X =",x)
                print("Y =",y)
                if x1 == (x-1) and y1 == y:                                
                #viene de arriba
                    direc = random.choice((2,3))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == (x+1) and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == (y+1):
                #viene de derecha
                    direc = random.choice((1,3))
                    a = 4
                    at = 2
                    i = 3
                    d = 1            
                    
                x1 = x
                y1 = y
                
    
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 

#####################################################################################################################################

        if x == 2 and y == 0:
print("X =",x)
                print("Y =",y)
                if x1 == (x-1) and y1 == y:                                
                #viene de arriba
                    direc = random.choice((2,3))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == (x+1) and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == (y+1):
                #viene de derecha
                    direc = random.choice((1,3))
                    a = 4
                    at = 2
                    i = 3
                    d = 1            
                    
                x1 = x
                y1 = y
                
    
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
 
#####################################################################################################################################
    
        if x == 3 and y == 0:
print("X =",x)
                print("Y =",y)
                if x1 == (x-1) and y1 == y:                                
                #viene de arriba
                    direc = random.choice((2,3))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == (x+1) and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == (y+1):
                #viene de derecha
                    direc = random.choice((1,3))
                    a = 4
                    at = 2
                    i = 3
                    d = 1            
                    
                x1 = x
                y1 = y
                
    
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 

#####################################################################################################################################
    
        if x == 4 and y == 0:
print("X =",x)
                print("Y =",y)
                if x1 == (x-1) and y1 == y:                                
                #viene de arriba
                    direc = random.choice((2,3))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == (x+1) and y1 == y:
                #viene de abajo
                    direc = random.choice((1,2))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == (y+1):
                #viene de derecha
                    direc = random.choice((1,3))
                    a = 4
                    at = 2
                    i = 3
                    d = 1            
                    
                x1 = x
                y1 = y
                
    
                print("direc = ",direc)
                if direc == 1:
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                            
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                        
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                            
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion  
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 

#####################################################################################################################################
            
            if x == 1 and y == NRY-1:
                print("X =",x)
                print("Y =",y)
                if x1 == (x-1) and y1 == y:
                #viene de arriba
                    direc = random.choice((3,4)) #1
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == (x+1) and y1 == y:
                #viene de abajo
                    direc = random.choice((1,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == (y-1):
                #viene de izquierda
                    direc = random.choice((3,1))
                    a = 2
                    at = 4
                    i = 1
                    d = 3      
                    
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                    
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  

##########################################################################################################################                                            
            
            if x == 2 and y == NRY-1:
                print("X =",x)
                print("Y =",y)
                if x1 == (x-1) and y1 == y:
                #viene de arriba
                    direc = random.choice((3,4)) #1
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == (x+1) and y1 == y:
                #viene de abajo
                    direc = random.choice((1,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == (y-1):
                #viene de izquierda
                    direc = random.choice((3,1))
                    a = 2
                    at = 4
                    i = 1
                    d = 3      
                    
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                    
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

##########################################################################################################################                                            
            
            if x == 3 and y == NRY-1:
                print("X =",x)
                print("Y =",y)
                if x1 == (x-1) and y1 == y:
                #viene de arriba
                    direc = random.choice((3,4)) #1
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == (x+1) and y1 == y:
                #viene de abajo
                    direc = random.choice((1,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == (y-1):
                #viene de izquierda
                    direc = random.choice((3,1))
                    a = 2
                    at = 4
                    i = 1
                    d = 3      
                    
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                    
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

##########################################################################################################################                                            
            
            if x == 4 and y == NRY-1:
                print("X =",x)
                print("Y =",y)
                if x1 == (x-1) and y1 == y:
                #viene de arriba
                    direc = random.choice((3,4)) #1
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == (x+1) and y1 == y:
                #viene de abajo
                    direc = random.choice((1,4))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == (y-1):
                #viene de izquierda
                    direc = random.choice((3,1))
                    a = 2
                    at = 4
                    i = 1
                    d = 3      
                    
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                    
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

##########################################################################################################################                                            

            if x == NRX-1 and y == 1:
                print("X =",x)
                print("Y =",y)
                if x1 == (x-1) and y1 == y:
                #viene de arriba
                    direc = random.choice((2,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x and y1 == (y-1):
                #viene de izquierda
                    direc = random.choice((1,2))
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == (y+1):
                #viene de derecha
                    direc = random.choice((1,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1          
                    
                x1 = x
                y1 = y
                
    
                print("direc = ",direc)
                if direc == 1:
                    
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
       
########################################################################################################################

            if x == NRX-1 and y == 2:
                print("X =",x)
                print("Y =",y)
                if x1 == (x-1) and y1 == y:
                #viene de arriba
                    direc = random.choice((2,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x and y1 == (y-1):
                #viene de izquierda
                    direc = random.choice((1,2))
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == (y+1):
                #viene de derecha
                    direc = random.choice((1,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1          
                    
                x1 = x
                y1 = y
                
    
                print("direc = ",direc)
                if direc == 1:
                    
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
       
########################################################################################################################

            if x == NRX-1 and y == 3:
                print("X =",x)
                print("Y =",y)
                if x1 == (x-1) and y1 == y:
                #viene de arriba
                    direc = random.choice((2,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x and y1 == (y-1):
                #viene de izquierda
                    direc = random.choice((1,2))
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == (y+1):
                #viene de derecha
                    direc = random.choice((1,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1          
                    
                x1 = x
                y1 = y
                
    
                print("direc = ",direc)
                if direc == 1:
                    
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)       
########################################################################################################################

            if x == NRX-1 and y == 4:
                print("X =",x)
                print("Y =",y)
                if x1 == (x-1) and y1 == y:
                #viene de arriba
                    direc = random.choice((2,4))
                    a = 3
                    at = 1
                    i = 2
                    d = 4
                elif x1 == x and y1 == (y-1):
                #viene de izquierda
                    direc = random.choice((1,2))
                    a = 2
                    at = 4
                    i = 1
                    d = 3
                elif x1 == x and y1 == (y+1):
                #viene de derecha
                    direc = random.choice((1,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1          
                    
                x1 = x
                y1 = y
                
    
                print("direc = ",direc)
                if direc == 1:
                    
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
       
########################################################################################################################

            if x == 0 and y == 1:
                print("X =",x)
                print("Y =",y)
                if x1 == x and y1 == (y+1):
                #viene de derecha
                    direc = random.choice((3,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1    
                elif x1 == (x+1) and y1 == y:
                #viene de abajo
                    direc = random.choice((4,2))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == (y+1):
                #viene de izquierda
                    direc = random.choice((3,2))
                    a = 2
                    at = 4
                    i = 1
                    d = 3       
                    
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                    
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

    ########################################################################################################################

            if x == 0 and y == 2:
                print("X =",x)
                print("Y =",y)
                if x1 == x and y1 == (y+1):
                #viene de derecha
                    direc = random.choice((3,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1    
                elif x1 == (x+1) and y1 == y:
                #viene de abajo
                    direc = random.choice((4,2))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == (y+1):
                #viene de izquierda
                    direc = random.choice((3,2))
                    a = 2
                    at = 4
                    i = 1
                    d = 3       
                    
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                    
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
    ########################################################################################################################

            if x == 0 and y == 3:
                print("X =",x)
                print("Y =",y)
                if x1 == x and y1 == (y+1):
                #viene de derecha
                    direc = random.choice((3,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1    
                elif x1 == (x+1) and y1 == y:
                #viene de abajo
                    direc = random.choice((4,2))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == (y+1):
                #viene de izquierda
                    direc = random.choice((3,2))
                    a = 2
                    at = 4
                    i = 1
                    d = 3       
                    
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                    
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

    ########################################################################################################################

            if x == 0 and y == 4:
                print("X =",x)
                print("Y =",y)
                if x1 == x and y1 == (y+1):
                #viene de derecha
                    direc = random.choice((3,4))
                    a = 4
                    at = 2
                    i = 3
                    d = 1    
                elif x1 == (x+1) and y1 == y:
                #viene de abajo
                    direc = random.choice((4,2))
                    a = 1
                    at = 3
                    i = 4
                    d = 2
                elif x1 == x and y1 == (y+1):
                #viene de izquierda
                    direc = random.choice((3,2))
                    a = 2
                    at = 4
                    i = 1
                    d = 3       
                    
                x1 = x
                y1 = y
                
                
                print("direc = ",direc)
                if direc == 1:
                    
                #Va para arriba
                    y = y 
                    x = x - 1
                    
                    if at == 1:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 1:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 1:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 1:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 2:
                #Va para derecha
                    y = y + 1
                    x = x 
                    
                    if at == 2:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 2:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1) 
                    if a == 2:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 2:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 3:
                #Va para abajo
                    y = y 
                    x = x + 1
                    
                    if at == 3:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 3:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 3:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 3:
                        #mover el robot 90 grados hasta intercepcion
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)  
                        
                elif direc == 4:
                #Va para izquierda
                    y = y - 1
                    x = x 
                    
                    if at == 4:
                        #mover el robot 180 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(4.2)
                        bot.drive_stop()
                        time.sleep(1)
                    if d == 4:
                        #mover el robot -90 grados hasta intercepcion
                        bot.drive_turn(-75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)
                    if a == 4:
                        #mover el robot 0 grados hasta intercepcion
                        bot.drive_straight(1)
                        time.sleep(1)
                    if i == 4:
                        #mover el robot 90 grados hasta intercepcion 
                        bot.drive_turn(75,1)
                        time.sleep(2.1)
                        bot.drive_stop()
                        time.sleep(1)

    ########################################################################################################################

        elif sensor1 == 0 and sensor2 == 0:
            
            bot.drive_straight(100)
            time.sleep(0.1)
                
        elif sensor1 == 0 and sensor2 == 1:

           
            bot.drive_turn(100, -180)
            time.sleep(0.1)
        elif sensor1 == 1 and sensor2 == 0:


            bot.drive_turn(100, 180)
            time.sleep(0.1)
    else:
        bot.drive_stop()