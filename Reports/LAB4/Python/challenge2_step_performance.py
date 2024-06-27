import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy.stats import pearsonr
from ECE16Lib.Pedometer import Pedometer

def load_data(filename):
    return np.genfromtxt(filename, delimiter=",")

def process_steps_samples(folder_path):
    filenames = glob.glob(folder_path + '/*.csv')
    gnd = [] 
    est = []  
  
    for filename in filenames:
        data = load_data(filename)
        ax, ay, az = data[:,1], data[:,2], data[:,3]
        pedometer = Pedometer(num_samples=len(data), fs=50, data=[]) 
        pedometer.add(ax, ay, az)
        steps, _, _ = pedometer.process()
        est.append(steps)
        actual_steps = int(filename.split('_')[-1].split('.')[0])  
        gnd.append(actual_steps)

    return np.array(gnd), np.array(est)

def analyze_performance(gnd, est):
    [R,p] = pearsonr(gnd, est)
    plt.figure(1)
    plt.clf()
    plt.subplot(121)
    plt.plot(gnd,gnd)
    plt.scatter(gnd,est)
    plt.text(min(gnd) + 2,max(est)+2,"R="+str(round(R,2)))
    plt.ylabel("estimate steps (Steps)")
    plt.xlabel("reference steps (Steps)")

    avg = (gnd + est) / 2
    dif = gnd - est
    std = np.std(dif)
    bias = np.mean(dif)
    upper_std = bias + 1.96 * std
    lower_std = bias - 1.96 * std
    plt.subplot(122)
    plt.scatter(avg, dif)
    plt.plot([np.min(avg),np.max(avg)],[bias,bias])
    plt.plot([np.min(avg),np.max(avg)],[upper_std, upper_std])
    plt.plot([np.min(avg),np.max(avg)],[lower_std, lower_std])
    plt.text(np.max(avg)+5,bias,"mean="+str(round(np.mean(gnd-est),2)))
    plt.text(np.max(avg)+5,upper_std,"1.96STD="+str(round(upper_std,2)))
    plt.text(np.max(avg)+5,lower_std,"-1.96STD="+str(round(lower_std,2)))
    plt.ylabel("Difference of Est and Gnd (Steps)")
    plt.xlabel("Average of Est and Gnd (Steps)")
    plt.show()
    

if __name__ == "__main__":
    folder_path = './data/challenge2_data' 
    gnd, est = process_steps_samples(folder_path)
    analyze_performance(gnd, est)