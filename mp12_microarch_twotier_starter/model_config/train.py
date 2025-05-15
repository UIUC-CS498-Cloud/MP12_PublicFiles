import os
import torch
import torch.nn as nn
from torch.autograd import Variable
import time
import sys
from utils import get_dataset, get_model, train_model, save_model

def main():
    start_time = time.time()
    dataset_name = os.environ["DATASET"]
    model_name = os.environ["TYPE"]
    print("dataset:", dataset_name)

    input_size = 784  # The image size = 28 x 28 = 784
    hidden_size = 500  # The number of nodes at the hidden layer
    num_classes = 10  # The number of output classes. In this case, from 0 to 9
    num_epochs = 1  # The number of times entire dataset is trained
    batch_size = 100  # The size of input data took for one iteration
    learning_rate = 0.001  # The speed of convergence

    train_dataset, test_dataset = get_dataset(dataset_name, model_name)

    train_loader = torch.utils.data.DataLoader(
        dataset=train_dataset, batch_size=batch_size, shuffle=True
    )

    test_loader = torch.utils.data.DataLoader(
        dataset=test_dataset, batch_size=batch_size, shuffle=False
    )

    net = get_model(model_name, dataset_name, input_size, hidden_size, num_classes, pretrained=False)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=learning_rate)

    train_model(num_epochs, train_loader, model_name, net, criterion, optimizer)
    save_model(model_name, dataset_name, net)    

    end_time = time.time()
    print("Time passed: %.2f sec" % (end_time - start_time))


if __name__ == "__main__":
    main()
    sys.exit()
