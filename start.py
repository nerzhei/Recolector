
from display.main import Main


class Main2():
    veces = 0
    funcionando = True

    def conectarButia(self):
        self.robot = get_butia()

    def conectarNXT(self):
        self.distancia = None
        self.nxt = get_nxt()
        get_nxt().MotorA.turn(20, 20)
        print get_nxt().Distance.get_sample()

    def moverMotores(self):
        self.funcionando = False
        self.robot.set2MotorSpeed(0, 0, 0, 0)
        # -------------------------------
        self.motorA.turn(-20, 160)
        self.motorB.turn(20, 640)
        try:
            self.motorA.turn(20, 220)
        except:
            self.motorB.turn(-20, 10)
            self.motorA.turn(20, 110)
        # -------------------------------
        self.motorB.turn(-20, 320)
        self.motorA.turn(-20, 110)
        self.motorB.turn(-20, 320)
        # self.motorA.turn(-20, 110)
        self.motorA.turn(20, 90)
        self.veces += 1
        if self.veces < 3:
            self.motorC.turn(-20, 450)
        else:
            sleep(2)
            self.motorA.turn(-20, 50)
            self.motorC.turn(20, 450 * 2)
            self.motorA.turn(20, 50)
            self.veces = 0
        thread.start_new_thread(self.esperar, ())

    def desconectarNxt(self):
        print "Saliendo..."
        self.robot.set2MotorSpeed(0, 0, 0, 0)
        try:
            self.brick.close()
        except:
            print "Brick desconectado"

    def esperar(self):
        print "Esperando la salida de los obstaculos"
        sleep(5)
        self.funcionando = True

    def __init__(self):
        if os.path.exists('modules/nxt_plugin'):
            sys.path.insert(0, 'modules/nxt_plugin')
        atexit.register(self.desconectarNxt)
        self.conectarButia()
        self.conectarNXT()
        print "Seguidor en funcionamiento..."
        while (True):
            if (self.robot.getGray(5) < 14000 and self.robot.getGray(2) < 40000):
                self.robot.set2MotorSpeed(1, 600, 1, 600)
            elif (self.robot.getGray(5) < 14000 and self.robot.getGray(2) > 40000):
                self.robot.set2MotorSpeed(1, 600, 0, 600)
            elif (self.robot.getGray(5) > 14000 and self.robot.getGray(2) < 40000):
                self.robot.set2MotorSpeed(0, 600, 1, 600)
            if self.distancia.get_sample() < 20:
                print "Accionar pala"
                if self.funcionando == True:
                    if self.veces < 3:
                        self.moverMotores()
                    else:
                        print "Todas las muestras han sido recolectadas."
        self.robot.set2MotorSpeed(0, 0, 0, 0)


if __name__ == "__main__":
    Main().run()