# from ECE16Lib.Communication import Communication
# from ECE16Lib.CircularList import CircularList
# import numpy as np
# import matplotlib.pyplot as plt
# from time import time, sleep

# # Define a function to perform the required transformations
# def compute_transformations(ax, ay, az, ax_diff, ay_diff, az_diff, l2_norms, l1_norms):
#     # Compute averages
#     ax_avg = np.mean(ax)
#     ay_avg = np.mean(ay)
#     az_avg = np.mean(az)

#     # Compute differences
#     ax_diff.extend(np.diff(ax))
#     ay_diff.extend(np.diff(ay))
#     az_diff.extend(np.diff(az))

#     # Compute L2 and L1 norms for the most recent sample
#     l2 = np.sqrt(ax[-1]**2 + ay[-1]**2 + az[-1]**2)
#     l1 = abs(ax[-1]) + abs(ay[-1]) + abs(az[-1])

#     l2_norms.append(l2)
#     l1_norms.append(l1)

#     return ax_avg, ay_avg, az_avg, l2, l1

# if __name__ == "__main__":
#     num_samples = 250  # 5 seconds of data @ 50Hz
#     refresh_time = 0.1  # update the plot every 0.1s (10 FPS)

#     # Initialize CircularLists for raw data and transformations
#     times = CircularList([], num_samples)
#     ax = CircularList([], num_samples)
#     ay = CircularList([], num_samples)
#     az = CircularList([], num_samples)
#     ax_diff = CircularList([], num_samples)
#     ay_diff = CircularList([], num_samples)
#     az_diff = CircularList([], num_samples)
#     l2_norms = CircularList([], num_samples)
#     l1_norms = CircularList([], num_samples)

#     comms = Communication("COM3", 115200)
#     sleep(3)
#     comms.clear()
#     comms.send_message("wearable")

#     try:
#         previous_time = 0
#         fig, axs = plt.subplots(5)  # Create 5 subplots for each data and transformation

#         while True:
#             message = comms.receive_message()
#             if message:
#                 try:
#                     m1, m2, m3, m4 = message.split(',')
#                 except ValueError:        # if corrupted data, skip the sample
#                     continue

#                 # add the new values to the circular lists
#                 times.add(int(m1))
#                 ax.add(int(m2))
#                 ay.add(int(m3))
#                 az.add(int(m4))


#                 # Perform transformations
#                 ax_avg, ay_avg, az_avg, l2, l1 = compute_transformations(
#                     ax, ay, az, ax_diff, ay_diff, az_diff, l2_norms, l1_norms
#                 )

#                 # Plot data if enough time has elapsed
#                 current_time = time()
#                 if current_time - previous_time > refresh_time:
#                     previous_time = current_time
#                     axs[0].cla()
#                     axs[0].plot(ax, label='AX')
#                     axs[0].plot(ay, label='AY')
#                     axs[0].plot(az, label='AZ')
#                     axs[0].legend()

#                     axs[1].cla()
#                     axs[1].plot(ax_diff, label='AX Diff')
#                     axs[1].legend()

#                     axs[2].cla()
#                     axs[2].plot(ay_diff, label='AY Diff')
#                     axs[2].legend()

#                     axs[3].cla()
#                     axs[3].plot(az_diff, label='AZ Diff')
#                     axs[3].legend()

#                     axs[4].cla()
#                     axs[4].plot(l2_norms, label='L2 Norm')
#                     axs[4].plot(l1_norms, label='L1 Norm')
#                     axs[4].legend()

#                     plt.show(block=False)
#                     plt.pause(0.001)  # Pause to allow update

#     except (Exception, KeyboardInterrupt) as e:
#         print(e)  # Exiting the program due to exception
#     finally:
#         comms.send_message("sleep")  # Stop sending data
#         comms.close()



from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
import numpy as np
import matplotlib.pyplot as plt
from time import time, sleep


# def compute_transformations(ax, ay, az, ax_diff, ay_diff, az_diff, l2_norms, l1_norms):
#     # Compute averages
#     ax_avg = np.mean(ax)
#     ay_avg = np.mean(ay)
#     az_avg = np.mean(az)

#     # Compute differences
#     ax_diff.extend(np.diff(ax))
#     ay_diff.extend(np.diff(ay))
#     az_diff.extend(np.diff(az))

#     # Compute L2 and L1 norms for the most recent sample
#     l2 = np.sqrt(ax[-1]**2 + ay[-1]**2 + az[-1]**2)
#     l1 = abs(ax[-1]) + abs(ay[-1]) + abs(az[-1])

#     l2_norms.append(l2)
#     l1_norms.append(l1)

#     return ax_avg, ay_avg, az_avg, l2, l1
def compute_transformations(ax, ay, az, ax_diff, ay_diff, az_diff, l2_norms, l1_norms, ax_avg_list, ay_avg_list, az_avg_list):
    ax_array = np.array(ax)
    ay_array = np.array(ay)
    az_array = np.array(az)

    # Compute averages
    ax_avg = np.mean(ax_array)
    ay_avg = np.mean(ay_array)
    az_avg = np.mean(az_array)

    # Append averages to their respective lists
    ax_avg_list.append(ax_avg)
    ay_avg_list.append(ay_avg)
    az_avg_list.append(az_avg)

    # Existing code for other calculations
    ax_diff.extend(np.diff(ax_array))
    ay_diff.extend(np.diff(ay_array))
    az_diff.extend(np.diff(az_array))

    l2 = np.sqrt(ax_array[-1]**2 + ay_array[-1]**2 + az_array[-1]**2)
    l1 = abs(ax_array[-1]) + abs(ay_array[-1]) + abs(az_array[-1])
    l2_norms.append(l2)
    l1_norms.append(l1)

    return ax_avg, ay_avg, az_avg, l2, l1

if __name__ == "__main__":
    num_samples = 250  # 5 seconds of data @ 50Hz
    refresh_time = 0.1  # update the plot every 0.1s (10 FPS)

    # Initialize CircularLists for raw data and transformations
    times = CircularList([], num_samples)
    ax = CircularList([], num_samples)
    ay = CircularList([], num_samples)
    az = CircularList([], num_samples)
    ax_diff = CircularList([], num_samples)
    ay_diff = CircularList([], num_samples)
    az_diff = CircularList([], num_samples)
    ax_avg_list = CircularList([], num_samples)
    ay_avg_list = CircularList([], num_samples)
    az_avg_list = CircularList([], num_samples)

    l2_norms = CircularList([], num_samples)
    l1_norms = CircularList([], num_samples)

    comms = Communication("COM3", 115200)
    sleep(3)
    comms.clear()
    comms.send_message("wearable")

    try:
        previous_time = 0
        fig, axs = plt.subplots(2) 

        while True:
            message = comms.receive_message()
            if message:
                try:
                    m1, m2, m3, m4 = message.split(',')
                except ValueError:       
                    continue


                times.add(int(m1))
                ax.add(int(m2))
                ay.add(int(m3))
                az.add(int(m4))


                # Perform transformations
                ax_avg, ay_avg, az_avg, l2, l1 = compute_transformations(
                    ax, ay, az, ax_diff, ay_diff, az_diff, l2_norms, l1_norms, ax_avg_list, ay_avg_list, az_avg_list
                )

                # Plot data if enough time has elapsed
                current_time = time()
                if current_time - previous_time > refresh_time:
                    previous_time = current_time
                    #part1 average
                    axs[0].cla()
                    axs[0].plot(ax, label='AX')
                    axs[0].plot(ay, label='AY')
                    axs[0].plot(az, label='AZ')
                    axs[0].legend()
                    # plt.cla()
                    # plt.plot(ax, label='AX')
                    # plt.plot(ay, label='AY')
                    # plt.plot(az, label='AZ')
                    # plt.legend()
                     
                    # axs[1].cla()
                    # axs[1].plot(ax_avg_list, label='AX Average')
                    # axs[1].plot(ay_avg_list, label='AY Average')
                    # axs[1].plot(az_avg_list, label='AZ Average')
                    # axs[1].legend()

                    # axs[1].cla()
                    # axs[1].plot(ax_diff, label='AX Diff')
                    # axs[1].legend()

                    # axs[1].cla()
                    # axs[1].plot(ay_diff, label='AY Diff')
                    # axs[1].legend()

                    # axs[1].cla()
                    # axs[1].plot(az_diff, label='AZ Diff')
                    # axs[1].legend()

                    # axs[1].cla()
                    # axs[1].plot(l2_norms, label='L2 Norm')
                    # axs[1].legend()
                    axs[1].cla()
                    axs[1].plot(l1_norms, label='L1 Norm')
                    axs[1].legend()

                    plt.show(block=False)
                    plt.pause(0.001)  # Pause to allow update

    except (Exception, KeyboardInterrupt) as e:
        print(e)  # Exiting the program due to exception
    finally:
        comms.send_message("sleep")  # Stop sending data
        comms.close()
