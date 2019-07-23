# *-* coding: utf-8 *-*

import torch  # root package
import torch.autograd as autograd  # computation graph
import torch.nn as nn  # neural networks
import torch.nn.functional as F  # layers, activations and more
import torch.optim as optim  # optimizers e.g. gradient descent, ADAM, etc.
from torch import Tensor  # tensor node in the computation graph
from torch.jit import script  # hybrid frontend decorator and tracing jit
from torch.jit import trace
from torch.utils.data import Dataloader  # dataset representation and loading
from torch.utils.data import Dataset


def main():
    print(torch.__version__)

if __name__ == "__main__":
    main()
