# ECE16 LAB3 Report

Prepared by: Jiawen Wang Date: 06/09/2024

**LAB4** This is the folder for LAB4, includes *Arduino* for the ino file *Accelerometer.ino", "Communication.ino", "Display.ino", "Sampling.ino", "TutorialPlottingWearable.ino" from the lab3 tutorial. *Python* for "challenge1", "challenge2", "challenge3" and tutorials.
*Documentation* for the gifs in folder *Fig*, *README* file, and data collected for LAB4

**Tutorial 1_ Offline Data Analysis -> tutorial_file_io.py** 

In this tutorial, we collect accelerometer data, save it to a csv with the first column being time stamp, first, second, third column being ax, ay and az. Then load and visualize the data to observe patterns that counts steps.

**Tutorial 2: Digital Signal Processing (DSP)**
Process data using various signal processing techniques in time and frequency domains. Makes it more accurate to detect steps.

**Tutorial 3: Pedometer Class**
Pedometer class that helps to process accelerometer data. Using live or recorded data to validate its effectiveness.


**Challenge_1** This challenge involves collecting 500 samples of accelerometer data, save it to a file, then load and visualize the data to observe patterns that might represent steps. This practice is fundamental when testing algorithms that require understanding the physical activity being monitored, like walking in the case of a pedometer. 

In my algorithm, I used L1 norm which combines the x, y, and z components of acceleration to reduce the orientation dependency.
Detrending: Remove the changes bring by gravity focusing more on the changes caused by steps themselves.
Low-pass Filtering: Apply a low-pass filter to remove high-frequency noise and preserve the main signal related to stepping.
Gradient Calculation: Compute the derivative to emphasize changes in the steps.
Moving Average Smoothing: Smooth the gradient and make there less noise, making peaks more obvious.
After all these processes, we have a smooth enough graph that represents the steps well, making it easier to identify he peaks which are representative of the steps.


![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB4/Documentation/Fig/challenge1_plot.png)

**Challenge_2** 
How did you ensure that your data samples have as much variety as possible? What different scenarios did you choose and why?

To guarantee a diverse set of data samples, individuals carried the device in various ways: the first person held it in their left hand, the second in their right, and the third carried it in their pocket, with step counts ranging from 3 to 30. This variation was chosen to reflect the natural differences in walking styles, which can vary significantly from person to person. By allowing individuals to carry the device in the manner they are most familiar with,  based on their dominant hand, I want to minimize potential biases. This approach ensures that our data collection represemts a wide range of realistic scenarios, thereby enhancing the robustness of the algorithm. 

Things might confuse the algorithm:


1. When people do other things similar to walking, e.g. running and other rhythmic activities that follows a pattern. The accelerometer signals are similar to to those generated during walking, which makes them being identified as walking patterns as well.
   
2. When the person is walking but hands shaked to a great angle, the signal is also similar to the walking pattern. There will be a peak in the graph, and the algorithm will identify that as a step. 

The R-value in the plot was around 0.16, which indicates a weak linear relationship between the estimated steps and the actual steps. This suggests that the algorithm does not consistently predict the step count accurately across different scenarios. 

The scatter plot shows a horizontal clustering of points at several intervals along estimated steps, which suggests that for varying actual step counts, the algorithm estimates similar step counts. This might indicate that the algorithm is not sensitive enough to changes in actual step counts, likely due to the movements similar to walk.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB4/Documentation/Fig/challenge2_plot.png)

**Challenge_3** 

Since it is so hard to record the exact number on the OLED while walking, I have to mimic walking pattern while sitting at a place stationary (this is hard too)

The latency of the algorithm depends on several factors:

Sampling Rate (fs = 50 Hz):

The MCU collects data every 20 milliseconds (ms) at 50 HZ. This is the rate which any new information can be gathered.

Number of Samples (num_samples = 250):

Collect 250 samples within 5 seconds, there's a  5-second window on which data is gathered before the next collection.

Process Time (1 second):

The algorithm processes the data once every second. The data is collected every 5 seconds but updating every second means processing every second of data.

Maximum Latency: Up to 5 seconds (due to the 5-second data collection window) + a small amount of additional latency for processing and output. Theoritically, the latency is 5 seconds maximum. Step count is updated every 1 second, so computation and responsiveness of the system is updated every second.

![](https://github.com/UCSD-ECE16/ece16-assignment-Cocodayow/blob/master/LAB4/Documentation/Fig/challenge3.gif)