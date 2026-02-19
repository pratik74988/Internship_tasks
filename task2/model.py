import torch
import torch.nn as nn
import torchvision.models as models

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

vgg = models.vgg19(pretrained = True).features.to(device).eval()

for param in vgg.parameters():
    param.requires_grad = False

def gram_matrix (tensor):
    b, c ,h ,w = tensor.size()
    features = tensor.view(c, h * w) 
    gram = torch.mm (features, features.t())
    return gram

def get_features(image, model):
    layers = {
        '0': 'conv1_1',
        '5': 'conv2_1',
        '10': 'conv3_1',
        '19': 'conv4_1',
        '21': 'conv4_2',  # content layer
        '28': 'conv5_1'
    }

    features = {}
    x = image
    for name, layer in models._modules.items():
        x = layer(x)
        if name in layers:
            features[layers[name]] = x
    return features

