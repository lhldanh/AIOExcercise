import torch
import torch.nn as nn


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


softmax = Softmax()
softmax_stable = SoftmaxStable()

x = torch.tensor([2.0, 1.0, 0.1])

output_softmax = softmax.forward(x)
print("Softmax output:", output_softmax)

output_softmax_stable = softmax_stable.forward(x)
print("SoftmaxStable output:", output_softmax_stable)
