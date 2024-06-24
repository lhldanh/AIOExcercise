import torch
import torch.nn as nn
import unittest

class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        e_x = torch.exp(x)
        return e_x / e_x.sum()

class SoftmaxStable(nn.Module):
    def forward(self, x):
        shift_x = x - torch.max(x)
        e_x = torch.exp(shift_x)
        return e_x / torch.sum(e_x)

class TestSoftmaxMethods(unittest.TestCase):
    def test_softmax(self):
        softmax = Softmax()
        x = torch.tensor([2.0, 1.0, 0.1])
        output = softmax.forward(x)
        self.assertTrue(torch.allclose(output, torch.tensor([0.65900114, 0.24243297, 0.09856589]), atol=1e-6))

    def test_softmax_stable(self):
        softmax_stable = SoftmaxStable()
        x = torch.tensor([2.0, 1.0, 0.1])
        output = softmax_stable.forward(x)
        self.assertTrue(torch.allclose(output, torch.tensor([0.65900114, 0.24243297, 0.09856589]), atol=1e-6))

if __name__ == '__main__':
    unittest.main()
