import os
import platform

class ping:

    def execute(self, ip):
        if ip.startswith("192."):
            self.executeFree(ip)
        else:
            print("")
            print("No se puede hacer ping. La ip debe comenzar con 192.")

    def executeFree(self, ip):
        if platform.system().lower() == "windows":
            param = "-n"
        else:
            param = "-c"
        command = f"ping {param} 10 {ip}"
        result = os.system(command)

        if result == 0:
            print("Ping exitoso")
        else:
            print("Error en el ping")


class pingProxy:
    
    def __init__(self):
        self.ip = None
        self.ping = ping()

    def execute(self):
        if self.ip == "192.168.0.254":
            self.ping.executeFree("www.google.com")
        else:
            self.ping.execute(self.ip)

pingProxy = pingProxy()

#Prueba de ping a Google
pingProxy.ip = "192.168.0.254"
pingProxy.execute()

#Prueba sin 192.
pingProxy.ip = "8.8.8.8"
pingProxy.execute()

#Prueba con 192.
pingProxy.ip = "192.168.0.1"
pingProxy.execute()