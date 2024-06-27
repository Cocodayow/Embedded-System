from ECE16Lib.Communication import Communication
import time

if __name__ == "__main__":
    try:
        comms = Communication("COM3", 115200)
        comms.clear() 

        for i in range(1, 31):  
            message = f"{i} seconds"
            comms.send_message(message)  
            time.sleep(1)  
            response = comms.receive_message()
            if response:
                print(response)  

    except KeyboardInterrupt:
        print("User stopped the program with CTRL+C input")
    finally:
        comms.close()  
        print("Cleaning up and exiting the program")
