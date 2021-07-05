from Python_data.robot.new_class.module.Tony.functions import talk, listen
from tonybot import tony


state = True
while state:
    print('about to start listening')
    initial = listen().lower()
    print('stopped listening')
    print(initial)

    if 'tony' in initial:
        talk('hi, how can i help you today?')
        answer = listen().lower()
        print(tony(answer))

    if 'stop' in initial:
        state = False
else:
    talk('Alright, Thank you, have a nice day!')
