# Ladder driver for arduino


### Installation

Create python env directory and install requirements
```
virtualenv env
source ./env/bin/activate
pip install -r requirements.txt
```

### Usage

1) First connect your Arduino at the COM port of your computer.
2) Connect your outputs (engines, lights, etc) at the relay module of the Arduino.
3) Open PLC_Safa.py.
4) Start creating your ladder logic.
5) Then when it's ended switch on the coils and see the magic.

Coil 1 ---> relay 1
Coil 2 ---> relay 2
Coil 3 ---> relay 3
Coil 4 ---> relay 4
Coil 5 ---> relay 5
Coil 6 ---> relay 6
Coil 7 ---> relay 7
Coil 8 ---> relay 8

### Flux diagram

![alt text](https://github.com/giulicrenna/Ladder-driver-for-Arduino/blob/main/lib/image.jpg?raw=true)
