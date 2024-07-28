import random

import matplotlib.pyplot as plt

def estimate_pi(num_points):
    points_inside_circle = 0
    points_total = 0
    estimation = []

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1

        points_total += 1

        pi_estimate = 4 * (points_inside_circle / points_total)
        estimation.append(pi_estimate)
    return estimation

def visualize_pi_estimation(num_points):
    x_inside_circle = []
    y_inside_circle = []
    x_outside_circle = []
    y_outside_circle = []

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = x**2 + y**2

        if distance <= 1:
            x_inside_circle.append(x)
            y_inside_circle.append(y)
        else:
            x_outside_circle.append(x)
            y_outside_circle.append(y)

    pi_estimate = 4 * (len(x_inside_circle) / num_points)
    print(f"Estimated value of pi: {pi_estimate}")

    plt.scatter(x_inside_circle, y_inside_circle, color='blue', label='Inside Circle', zorder=2)
    plt.scatter(x_outside_circle, y_outside_circle, color='red', label='Outside Circle', zorder=1)
    
    plt.title('Monte Carlo Estimation of Pi')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.axis([-1.1, 1.1, -1.1, 1.1])  
    plt.show()


mode = input("Choose mode (estimate/visualize): ")

if mode == 'estimate':
    num_points = int(input("Enter number of points for test: "))
    num_tests = int(input("Enter number of tests: "))
    series_estimation = {} 
    for i in range(num_tests):
        estimation = estimate_pi(num_points)
        series_estimation[i] = estimation
    # Plotting all the estimation series
    for i, estimation in series_estimation.items():
        plt.plot(estimation, label=f"Estimation {i+1}")

    plt.title('Monte Carlo Estimation of Pi')
    plt.xlabel('Number of Points')
    plt.ylabel('Estimated Value of Pi')
    plt.legend()
    plt.show()

    
elif mode == 'visualize':
    num_points = int(input("Enter number of points for visualization: "))
    visualize_pi_estimation(num_points)
