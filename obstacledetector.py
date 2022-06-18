from picarx import Picarx
from robot_hat import TTS

px = Picarx()
tts_robot = TTS()

while True:
    
    distance = px.ultrasonic.read()
    #print(distance)
    if distance <10:
        tts_robot.say("there is obstacle front of me. bring me back.")
