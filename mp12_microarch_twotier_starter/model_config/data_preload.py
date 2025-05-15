import torchvision.datasets as dsets

if __name__ == "__main__":
    dsets.MNIST(root='./data', download=True)
    dsets.KMNIST(root='./data', download=True)
