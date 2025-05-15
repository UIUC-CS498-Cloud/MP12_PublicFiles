import torchvision.transforms as transforms
import torchvision.datasets as dsets
import torch
from torch.autograd import Variable
from models import FFNN, CNN


def get_dataset(dataset_name, model_name):
    train_dataset = []
    test_dataset = []
    trans = transforms.ToTensor()
    if model_name == "cnn" or model_name == "cnv":
        trans = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
        )
    if dataset_name == "mnist":
        train_dataset = dsets.MNIST(
            root="./data",
            train=True,
            transform=trans,
            # download=True
        )

        test_dataset = dsets.MNIST(root="./data", train=False, transform=trans)
    elif dataset_name == "kmnist":
        train_dataset = dsets.KMNIST(
            root="./data",
            train=True,
            transform=trans,
            # download=True
        )

        test_dataset = dsets.KMNIST(root="./data", train=False, transform=trans)

    return train_dataset, test_dataset


def get_model(model_name, dataset_name, input_size, hidden_size, num_classes, pretrained=False):
    if model_name == "ff":
        net = FFNN(input_size, hidden_size, num_classes)
    elif model_name == "cnn" or model_name == "cnv":
        net = CNN(num_classes)
        model_name = "cnn"

    if not pretrained:
        return net

    print(f"Loading model from ./models/{model_name}_{dataset_name}_model.pkl")
    net.load_state_dict(torch.load(f"./models/{model_name}_{dataset_name}_model.pkl"))
    return net


def save_model(model_name, dataset_name, net):
    if model_name == "cnn" or model_name == "cnv":
        model_name = "cnn"
    torch.save(net.state_dict(), f"./models/{model_name}_{dataset_name}_model.pkl")


def train_model(num_epochs, train_loader, model_name, net, criterion, optimizer):
    for epoch in range(num_epochs):
        for i, (images, labels) in enumerate(
            train_loader
        ):  # Load a batch of images with its (index, data, class)
            if model_name == "ff":
                images = Variable(
                    images.view(-1, 28 * 28)
                )  # Convert torch tensor to Variable: change image from a vector of size 784 to a matrix of 28 x 28
            labels = Variable(labels)

            optimizer.zero_grad()  # Intialize the hidden weight to all zeros
            outputs = net(
                images
            )  # Forward pass: compute the output class given a image
            loss = criterion(
                outputs, labels
            )  # Compute the loss: difference between the output class and the pre-given label
            loss.backward()  # Backward pass: compute the weight
            optimizer.step()  # Optimizer: update the weights of hidden nodes
            if (i + 1) % 100 == 0:  # Logging
                print(
                    "Epoch [%d/%d], Step [%d/%d], Loss: %.4f"
                    % (
                        epoch + 1,
                        num_epochs,
                        i + 1,
                        len(train_loader),
                        loss.data,
                    )
                )