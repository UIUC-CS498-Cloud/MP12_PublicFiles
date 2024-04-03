import os
import torch
from torch.autograd import Variable
import time
import sys
from utils import get_dataset, get_model



def main():
    start_time = time.time()
    dataset_name = os.environ["DATASET"]
    model_name = os.environ["TYPE"]
    print("dataset:", dataset_name)

    input_size = 784  # The image size = 28 x 28 = 784
    hidden_size = 500  # The number of nodes at the hidden layer
    num_classes = 10  # The number of output classes. In this case, from 0 to 9
    batch_size = 100  # The size of input data took for one iteration

    _, test_dataset = get_dataset(dataset_name, model_name)

    test_loader = torch.utils.data.DataLoader(
        dataset=test_dataset, batch_size=batch_size, shuffle=False
    )

    net = get_model(model_name, dataset_name, input_size, hidden_size, num_classes, pretrained=True)

    correct = 0
    total = 0
    for images, labels in test_loader:
        if model_name == "ff":
            images = Variable(images.view(-1, 28 * 28))
        outputs = net(images)
        _, predicted = torch.max(
            outputs.data, 1
        )  # Choose the best class from the output: The class with the best score
        total += labels.size(0)  # Increment the total count
        correct += (predicted == labels).sum()  # Increment the correct count

    print(
        "Accuracy of the network on the 10K test images: %d %%"
        % (100 * correct / total)
    )
    

    end_time = time.time()
    print("Time passed: %.2f sec" % (end_time - start_time))


if __name__ == "__main__":
    main()
    sys.exit()
