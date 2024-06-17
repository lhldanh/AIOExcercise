import math
import numpy as np

def mae_loss(y, y_hat):
    integrand = [y[i] - y_hat[i] for i in range(0, len(y))]
    return 1 / len(y) * sum(integrand)

def mse_loss(y, y_hat):
    integrand = [(y[i] - y_hat[i]) ** 2 for i in range(0, len(y))]
    return 1 / len(y) * sum(integrand)

def rmse_loss(y, y_hat):
    return math.sqrt(mse_loss(y, y_hat))

def main():
    n = input("Number sample: ")
    if (not n.isnumeric()):
        print('number of samples must be an integer number')
        return

    loss_name = input("Loss name (MAE, MSE, RMSE): ")

    for i in range(0, int(n)):
        y = np.random.uniform(0, 10, 5) # từ 0 đến 10 tạo 5 phần tử
        y_hat = np.random.uniform(0, 10, 5)
        loss = mae_loss(y, y_hat) * (loss_name == 'MAE') + mse_loss(y, y_hat) * (loss_name == 'MSE') + rmse_loss(y, y_hat) * (loss_name == 'RMSE')
        print('loss name:', loss_name, ', sample: ', i)
        print('pred: ', y_hat)
        print('target: ', y)
        print('loss: ', loss)
    
    
if __name__ == '__main__':
    main()