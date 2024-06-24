def MD_nRE(y, y_hat, n, p):
    return (y ** (1/n) - y_hat ** (1/n)) ** p

if __name__ == '__main__':
    print(MD_nRE(y= 100 , y_hat= 99.5 , n= 2 , p= 1))