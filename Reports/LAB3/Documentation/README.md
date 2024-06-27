# ECE16 LAB3 Report

Prepared by: Jiawen Wang Date: 05/19/2024

**LAB3** This is the folder for LAB3, includes *Arduino* for the ino file *TutorialPySerial*, *TutorialPlottingWearable*; *Python* for the py file 


*Documentation* for the gifs in folder *Fig* and *README* file for LAB3

**tutorial_numpy.py** 
Question 1:

Make a NumPy array called array1 from a list [0, 10, 4, 12]. Subtract 20 from array1. What is the result? What is the shape of array1?

The result after subtracting 20 from each element will be [-20, -10, -16, -8].
The shape of array1 will be (4,). It is a one-dimensional array with 4 elements

Question 2:

Make a 2D array2 from [0, 10, 4, 12], [1, 20, 3, 41]. Use array restructuring and indexing to create a new array array2_new that is a 2x2 array with values [[4, 12], [1, 20]]. What methods did you use?

Use indexing first to select specific elements from array2. Then use array construction-np.array() function to assemble the selected elements into the new 2D array array2_new.

Question 5: 

Make an array called array5 using linspace() that goes from 0 to 100 with 49 steps. How does this differ from arange()? When might you use one over the other?

np.linspace(start, stop, num): Creates evenly spaced numbers over a specified interval, inclusive of both endpoints. Specify the total number of points.
np.arange(start, stop, step): Creates values from start up to (but not including) stop, increasing by step. Specify the step size, and the number of elements is determined automatically.
Use linspace when need a fixed number of evenly spaced points. Use arange when step size is more important than the number of elements.

**tutorial_plotting_basic.py**

When a 2D array is passed to plt.plot(), Matplotlib interprets each row as a separate dataset. Each row generates a separate line on the plot, with each line's points connected in the order they appear in the row.

**Tutorial_Sampling** Sample from read world data- analog, the frequency of sampling is important because otherwise we might get weird results.

**Analog_output**

Pulse width modulation, for less duty cycle, the output is HIGH, for greater duty cycle, the output is LOW. Showing the results in builtin led and buzzer motor. The greater the value is, the more intense it buzz.

**Analog_input**

Accelerometer is a type of sensor that measures X,Y,Z axis acceleration, interfaces with MCU through ADC. Read from accelerometer and visualize it in serial monitor and serial plotter.

**Challenge_1** This challenge involves detecting different gestures- Up, down, shaking with accelerometer and display the gesture in OLED.

1.Describe in plain english the logic behind your algorithm. What is the rule for each gesture? 

UP: When acceleration on the z-axis is much greater compared to acceleration on x-axis and y-axis, and the value for all 3 axis reamins relatively stable. Acceleration varies within a range of 10.

DOWN: When acceleration on the z-axis is much smaller compared to acceleration on x-axis and y-axis, and the value for all 3 axis reamins relatively stable. Acceleration varies within a range of 10.

SHAKIING: When acceleration on either x, y or z axis varies rapidly, the value of acceleration for either of the axis varies greater than the range of 10. 

2.Describe 3 different tests you tried in order to work towards your working algorithm. This might be something around showing the algorithm different variations. Shaking the accelerometer in different ways. BE DESCRIPTIVE. You should have at least 3 sentences describing each test and a GIF to help illustrate each test. 

TEST1: 
Have the thing facing upward, shake it rapidly at a small angle(more horitzontal), see if the gesture is shaking when shaking, and up when shaking stopped. Making sure that up is correctly identified and marked, and distinguishes between not moving and moving rapidly.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c1_part1_a.gif)

TEST2:
Have the thing facing downward, shake it rapidly at a small angle(more horitzontal), see if the gesture is shaking when shaking, and up when shaking stopped. Making sure that down is correctly identified and marked, and distinguishes between not moving and moving rapidly.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c1_part1_b.gif)

TEST3: 
Have the thing facing upward, shake it gently at a small angle(more horizontal), see if the gesture is shaking when shaking and up when shaking stopped. Making sure that non rapid changes are identified too.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c1_part2_c.gif)

3.Come up with 2 ways that will confuse your algorithm. If your algorithm is really really robust, describe 2 scenarios that were difficult for you to have tuned your algorithm to be robust

Confusion1:
When I tap the accelerometer very quickly in fast succession less gently, my algorithm will still mark it as shaking even when it's not moving. One of the ways I tried to solve the problem is make it harder to be identified as shaking - increase the range for it to be idenfied as shaking. When shaking, the accelerations will change more rapidly compared to tapping.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c1_part2_c.gif)


Confusion2:
When shaking at a extreme angle that is more vertical and less horizontal angle, my algorithtm will still mark it as shaking even when it's not moving. One of the ways I tried to solve it is to decrease the threshold to be identified as up. After that my algorithm distinguishes it as up even when at a extreme angle.


![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/Fig/c1_part2_c.gif)

4.
Show in one single GIF the accelerometer in each of the gestures and while in the same frame the serial monitor showing the state. 

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/statemachine_pic/hw1_c2_state-machine.png)

**Challenge_2** This challenge involves a timer controlled by two buttons - one add button and one reset button.
Starting in state wait, awaiting for user inputs(press add button),  if press add(addButtonState changed from high to low), go to add state. When in state add, for every 300ms, timer +=1, if press add(addButtonState changed from high to low) and reset button is not pressed(remain at HIGH) then move state subtract. In state subtract, timer -=1 every 300ms and if add button is pressed (from high to low) before timer == 0, move to state add; if no button pressed and eventually timer == 0, move to state vibration. In state vibration, keeps motor vibrate until reads a press of reset button, move to state wait and set timer to 0, stop vibration.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/statemachine_pic/hw1_c2_state-machine.png)


**Challenge3** This challenge involves a timer controlled by gestures - Down for pressing add time button, shake for pressing reset button, up for no button pressed.
Starting in state wait, awaiting for user inputs(down gesture),  if down gesture detected, go to add state. When in state add, for every 300ms, timer +=1, if detects up gesture then move state subtract. In state subtract, timer -=1 every 300ms and if down gesture is detected again before timer == 0, move to state add; if no down gesture detected and eventually timer == 0, move to state vibration. In state vibration, keeps motor vibrate until read a shake gesture, move to state wait and set timer to 0, stop vibration.


![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB1/Documentation/statemachine_pic/hw1_c3_state-machine.png)


I pull it out from the cup and leave it outside so that it won't affect accelerometer that much especially accelerameter is inside the cup and the cup is pretty thick.




