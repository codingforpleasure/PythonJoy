# I have binded my Smartphone's MAC address to IPv4 192.168.0.102 in my
# home router's configuration.

__author__ = 'gil'
import subprocess
import time

isHere = False

while (1):
    myProcess = subprocess.Popen(["ping", "-c 1", "192.168.0.102"], stdout=subprocess.PIPE)
    output = myProcess.communicate()[0]
    #print(output)
    if (output.decode().find("100% packet loss") == -1):
        if (isHere == False):
            isHere = True
            print("Smartphone has just now got connected to your home network!")

            # I have arrived to my home,
            # so now the Raspberry pi should sweep the servo and flash the leds strip

        time.sleep(120) # For avoiding the scenario of hogging the CPU
                        # and injecting too many icmp request/echo into the LAN
    else:
        print("Smartphone is disconnected!")
        isHere = False
        time.sleep(2)
