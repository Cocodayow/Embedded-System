from ECE16Lib.Communication import Communication
from ECE16Lib.Pedometer import Pedometer
import numpy as np
from time import time, sleep

def main():
    fs = 50  # Sampling rate in Hz
    num_samples = 250  # Number of samples corresponding to 5 seconds of data at 50 Hz
    process_time = 1  # Time interval in seconds to process data


    ped = Pedometer(num_samples, fs, [])


    comms = Communication("COM3", 115200)  
    comms.clear()
    comms.send_message("wearable")  

    try:
        previous_time = time()
        while True:
            message = comms.receive_message()
            if message:
                try:
                    _, ax, ay, az = map(int, message.split(','))
                    ped.add(ax, ay, az) 
                
                    if time() - previous_time > process_time:
                        previous_time = time()
                        steps, peaks, filtered = ped.process()
                        print(f"Step count: {steps}")
                        comms.send_message(str(steps)) 
                except ValueError:
                    continue  

    except KeyboardInterrupt:
        print("Operation cancelled by user.")

    finally:
        comms.send_message("sleep")
        comms.close()
        print("Communication closed.")

if __name__ == "__main__":
    main()