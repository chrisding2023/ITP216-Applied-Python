# Ding Wencan Chrisdin@usc.edu
# 4511303572
# Lab 11
# Description:
# Write a program which will visualize the three trigonometric functions (sin, cos, and tan) in two different ways
# each.
import numpy as np
from matplotlib import pyplot as plt

def main():
    fig, ax = plt.subplots(2,3)
    fig.suptitle("Trig!")

    x = np.arange(-1 * np.pi, np.pi, 0.1)
    y = np.sin(x)
    ax[0,0].plot(x,y)
    ax[0,0].set(title="sin(x)", xlabel="x",ylabel="y")

    y2 = np.sinh(x)
    ax[1,0].plot(x,y2)
    ax[1,0].set(title="sinh(x)",xlabel="x",ylabel="y")

    y3 = np.cos(x)
    ax[0,1].plot(x,y3)
    ax[0,1].set(title="cos(x)",xlabel="x",ylabel="y")

    y4 = np.cosh(x)
    ax[1,1].plot(x,y4)
    ax[1,1].set(title="cosh(x)",xlabel="x",ylabel="y")

    y5 = np.tan(x)
    ax[0,2].plot(x,y5)
    ax[0,2].set(title="tan(x)",xlabel="x",ylabel="y")

    y6 = np.tanh(x)
    ax[1,2].plot(x,y6)
    ax[1,2].set(title="tanh(x)",xlabel="x",ylabel="y")

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()