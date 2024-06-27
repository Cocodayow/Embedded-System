# ECE16 LAB2 Report

Prepared by: Jiawen Wang Date: 04/28/2024

**LAB2** This is the folder for LAB1, includes *Arduino* for the ino file *Challenge_1*, *Challenge_2*, *Challenge_3*, *Tutorial_DisplayI2C*, *Tutorial_AnalogInputPart1*, *Tutorial_AnalogInputPart2*, *Tutorial_AnalogInputPart1*,*Tutorial_AnalogOutputPart2*,*Tutorial_Sampling*
*Documentation* for the gifs in folder *Fig* and *README* file for LAB2

**Tutorial_DisplayI2C** OLED display, setup OLED and output data to be displayed to different rows of the OLED.

**Tutorial_Sampling** Sample from read world data- analog, the frequency of sampling is important because otherwise we might get weird results.

**Analog_output**

Pulse width modulation, for less duty cycle, the output is HIGH, for greater duty cycle, the output is LOW. Showing the results in builtin led and buzzer motor. The greater the value is, the more intense it buzz.

**Analog_input**

Accelerometer is a type of sensor that measures X,Y,Z axis acceleration, interfaces with MCU through ADC. Read from accelerometer and visualize it in serial monitor and serial plotter.

**Challenge_1** This challenge involves detecting different gestures- Up, down, shaking with accelerometer and display the gesture in OLED.

1. Describe in plain english the logic behind your algorithm. What is the rule for each gesture? 

UP: When acceleration on the z-axis is much greater compared to acceleration on x-axis and y-axis, and the value for all 3 axis reamins relatively stable. Acceleration varies within a range of 10.

DOWN: When acceleration on the z-axis is much smaller compared to acceleration on x-axis and y-axis, and the value for all 3 axis reamins relatively stable. Acceleration varies within a range of 10.

SHAKING: When acceleration on either x, y or z axis varies rapidly, the value of acceleration for either of the axis varies greater than the range of 10. 

2. Describe 3 different tests you tried in order to work towards your working algorithm. This might be something around showing the algorithm different variations. Shaking the accelerometer in different ways. BE DESCRIPTIVE. You should have at least 3 sentences describing each test and a GIF to help illustrate each test. 

TEST1: 
Have the thing facing upward, shake it rapidly at a small angle(more horitzontal), see if the gesture is shaking when shaking, and up when shaking stopped. Making sure that up is correctly identified and marked, and distinguishes between not moving and moving rapidly.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c1_test1.gif)

TEST2:
Have the thing facing downward, shake it rapidly at a small angle(more horitzontal), see if the gesture is shaking when shaking, and up when shaking stopped. Making sure that down is correctly identified and marked, and distinguishes between not moving and moving rapidly.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c1_test2.gif)

TEST3: 
Have the thing facing upward, shake it gently at a small angle(more horizontal), see if the gesture is shaking when shaking and up when shaking stopped. Making sure that non rapid changes are identified too.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c1_test3.gif)

3. Come up with 2 ways that will confuse your algorithm. If your algorithm is really really robust, describe 2 scenarios that were difficult for you to have tuned your algorithm to be robust

Confusion1:
When I tap the accelerometer very quickly in fast succession less gently, my algorithm will still mark it as shaking even when it's not moving. One of the ways I tried to solve the problem is make it harder to be identified as shaking - increase the range for it to be idenfied as shaking. When shaking, the accelerations will change more rapidly compared to tapping.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c1_confusion1.gif)


Confusion2:
When shaking at a extreme angle that is more vertical and less horizontal angle, my algorithtm will still mark it as shaking even when it's not moving. One of the ways I tried to solve it is to decrease the threshold to be identified as up. After that my algorithm distinguishes it as up even when at a extreme angle.


![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c1_confusion2.gif)

4. Show in one single GIF the accelerometer in each of the gestures and while in the same frame the serial monitor showing the state. 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c1_summary.gif)

**Challenge_2** This challenge involves a timer controlled by two buttons - one add button and one reset button.
Starting in state wait, awaiting for user inputs(press add button),  if press add(addButtonState changed from high to low), go to add state. When in state add, for every 300ms, timer +=1, if press add(addButtonState changed from high to low) and reset button is not pressed(remain at HIGH) then move state subtract. In state subtract, timer -=1 every 300ms and if add button is pressed (from high to low) before timer == 0, move to state add; if no button pressed and eventually timer == 0, move to state vibration. In state vibration, keeps motor vibrate until reads a press of reset button, move to state wait and set timer to 0, stop vibration.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c2_fsm.gif)

TEST1:
A GIF showing the following sequence: 1) add 5 seconds, 2) let it count to 0, 3) let motor shake for a few seconds, and 4) hit reset to disengage motor

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c2_test1.gif)

TEST2:
A GIF showing the following sequence: 1) add 10 seconds, 2) let it count to 5, 3) hit reset

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c2_test2.gif)

TEST3:
A GIF showing the following sequence: 1) while at 0 seconds, hit reset, 2) add 5 seconds, 3) let it count to 0, 4) let motor shake for a few seconds, 5) and hit reset to disengage motor. 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c2_test3.gif)

TEST4:
A GIF showing the following sequence: 1) add 10 seconds, 2) let it count to 5, 3) add 5 seconds, 4) let it count to 0, 5) let motor shake for a few seconds, 6) and hit reset to disengage motor. 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c2_test4.gif)


**Challenge3** This challenge involves a timer controlled by gestures - Down for pressing add time button, shake for pressing reset button, up for no button pressed.
Starting in state wait, awaiting for user inputs(down gesture),  if down gesture detected, go to add state. When in state add, for every 300ms, timer +=1, if detects up gesture then move state subtract. In state subtract, timer -=1 every 300ms and if down gesture is detected again before timer == 0, move to state add; if no down gesture detected and eventually timer == 0, move to state vibration. In state vibration, keeps motor vibrate until read a shake gesture, move to state wait and set timer to 0, stop vibration.


![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c3_1.jpg)

TEST1:
A GIF showing the following sequence: 1) add 5 seconds, 2) let it count to 0, 3) let motor shake for a few seconds, and 4) hit reset to disengage motor

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c3_test1.gif)

TEST2:
A GIF showing the following sequence: 1) add 10 seconds, 2) let it count to 5, 3) hit reset

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c3_test2.gif)

TEST3:
A GIF showing the following sequence: 1) while at 0 seconds, hit reset, 2) add 5 seconds, 3) let it count to 0, 4) let motor shake for a few seconds, 5) and hit reset to disengage motor. 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c3_test3.gif)

TEST4:
A GIF showing the following sequence: 1) add 10 seconds, 2) let it count to 5, 3) add 5 seconds, 4) let it count to 0, 5) let motor shake for a few seconds, 6) and hit reset to disengage motor. 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB2/Documentation/Fig/c3_test4.gif)

I pull it out from the cup and leave it outside so that it won't affect accelerometer that much especially accelerameter is inside the cup and the cup is pretty thick.




