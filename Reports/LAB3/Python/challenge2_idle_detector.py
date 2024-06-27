from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from matplotlib import pyplot as plt
from time import time, sleep

# Define thresholds and durations
MOTION_THRESHOLD = 0.05  # Adjust based on your specific sensitivity requirements
IDLE_TIME_THRESHOLD = 5  # Seconds
ACTIVE_TIME_THRESHOLD = 1  # Seconds

def compute_average(l):
    return sum(l) / len(l) if len(l) > 0 else 0

def update_state(current_state, is_active, last_state_change_time):
    current_time = time()
    time_since_change = current_time - last_state_change_time

    if current_state == "idle" and is_active:
        if time_since_change >= ACTIVE_TIME_THRESHOLD:
            return "active", current_time
    elif current_state == "active" and not is_active:
        if time_since_change >= IDLE_TIME_THRESHOLD:
            return "idle", current_time

    return current_state, last_state_change_time

if __name__ == "__main__":
    num_samples = 250  # 5 seconds of data at 50Hz
    ax = CircularList([], num_samples)
    ay = CircularList([], num_samples)
    az = CircularList([], num_samples)

    comms = Communication("COM3", 115200)
    sleep(3)
    comms.clear()
    comms.send_message("wearable")

    current_state = "active"
    last_state_change_time = time()

    try:
        while True:
            message = comms.receive_message()
            if message:
                try:
                    _, x, y, z = message.split(',')
                    ax.add(float(x))
                    ay.add(float(y))
                    az.add(float(z))
                except ValueError:
                    continue

                avg_acceleration = compute_average([ax[-1], ay[-1], az[-1]])
                is_active = avg_acceleration > MOTION_THRESHOLD

                current_state, last_state_change_time = update_state(current_state, is_active, last_state_change_time)
                if current_state == "idle":
                    comms.send_message("idle_alert")
                elif current_state == "active":
                    comms.send_message("active_alert")

                # Update plot for live feedback
                current_time = time()
                if current_time - last_state_change_time > 0.1:  # Refresh plot every 0.1 seconds
                    plt.cla()
                    plt.plot(ax)
                    plt.show(block=False)
                    plt.pause(0.001)

    except (Exception, KeyboardInterrupt) as e:
        print(e)
    finally:
        comms.send_message("sleep")
        comms.close()
