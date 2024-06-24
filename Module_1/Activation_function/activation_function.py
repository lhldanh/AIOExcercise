import math

def sigmoid_func(x):
    return 1 / (1 + math.e ** (-x))

def relu_func(x):
    return 0 * (x <= 0) + x * (x > 0)

def elu_func(x, alpha = 0.1):
    return alpha * (math.e ** (x) - 1) * (x <= 0) + x * (x > 0)

def activation_func(x, func_name):
      
    if (func_name == 'sigmoid'):
        return sigmoid_func(x)
    if (func_name == 'relu'):
        return relu_func(x)
    if (func_name == 'elu'):
        return elu_func(x)

def main():
    x = input("x = ")
    func = input("Activation Function ( sigmoid | relu | elu ): ")

    func_name_lst = ['sigmoid', 'relu', 'elu']
    if (func not in func_name_lst):
        print(func, 'is not supported')
        return
    
    if (not x.isdigit()):
        print('x must be a number')
        return
    
    x = float(x)
    print(activation_func(x, func))

if __name__ == '__main__':
    main()
    