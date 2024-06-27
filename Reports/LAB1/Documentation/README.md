# ECE16 LAB1 Report

Prepared by: Jiawen Wang Date: 04/19/2024

**LAB1** This is the folder for LAB1, includes *Arduino* for the ino file *HW1_C1*, *HW1_C2*, *HW1_C3*, *Tutorial_Digital_Communication*, *Tutorial_Serial_Communication*. 
*Documentation* for the gifs *c1_part1_a*, *c1_part1_b*, *c1_part1_c, *c1_part2_a**, *c1_part2_b*, *c1_part2_c* in folder *Fig* and *README* file for LAB1

**Tutorial_Digital_Communication** follows the digital communication tutorial; Whent he button is pressed light up either the builtin LED or another LED connected. 

**Tutorial_Serial_Communication** follows the serial communication tutorial; Prints data in the serial monitor, or send data from laptop waiting for the data to get to arduino then get back.

**Challenge1, HW1_C1** This challenge involves blink a red LED at 1 Hz, blink a blue LED at 5 Hz, blink a yellow LED at 10 Hz; It also includes blink a red LED with 1s on and 100ms off, blink a blue LED with 200ms on and 50ms off, blink a yellow LED with 20ms on and 10ms off; The circuits are in parallel, and there's a 220Ohm resistor in each circuit.
blink a red LED at 1 Hz 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c1_part1_a.gif)

blink a blue LED at 5 Hz 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c1_part1_b.gif)

blink a yellow LED at 10 Hz 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c1_part1_c.gif)

blink a red LED with 1s on and 100ms off 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c1_part2_a.gif)

blink a blue LED with 200ms on and 50ms off 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c1_part2_b.gif)

blink a yellow LED with 20ms on and 10ms off 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c1_part2_c.gif)

**Challenge2, HW1_C2** This challenge involves counting how long the button is pushed (defined as transition going from high to low), designed a 3 state machine.
Starts with state STOPPED, if detects first push move to state RUNNING. In RUNNING, continue increment counter by 1 every second until reads a push. If so, move to state PAUSED and stop increasing counter. In state PAUSED, if reads a push, move to state RUNNING, and continue incrementing counter.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/statemachine_pic/hw1_c2_state-machine.png)

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c2.gif)


**Challenge3, HW1_C3** This challenge involves counting how many times the button is pushed (defined as transition going from high to low). Every time the push button is pushed, the timer will increment by 1. If the button has not been pushed in the last 3 seconds, the timer will begin to count down by 1 every second. Once the timer value reaches 0, do not decrease it further.
Starts with state STOPPED, if detects first push move to state ADDING. In ADDING, if no push detected in the last 3 seconds, move to state COUNTDOWN. If push detected, increment timer. In state COUNTDOWN, subtract 1 from timer every second while timer is still positive untill reads a push. If reads a push move to ADDING. 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/statemachine_pic/hw1_c3_state-machine.png)


![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c3.gif)


