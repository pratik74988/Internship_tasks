import torch
import torch.nn as nn
import torchvision.models as models

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load pretrained VGG19
vgg = models.vgg19(pretrained=True).features.to(device).eval()

# Freeze parameters
for param in vgg.parameters():
    param.requires_grad = False


def gram_matrix(tensor):
    b, c, h, w = tensor.size()
    features = tensor.view(c, h * w)
    gram = torch.mm(features, features.t())
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
    for name, layer in model._modules.items():
        x = layer(x)
        if name in layers:
            features[layers[name]] = x
    return features


def style_transfer(content, style, steps=300, style_weight=1e6, content_weight=1):
    content_features = get_features(content, vgg)
    style_features = get_features(style, vgg)

    style_grams = {layer: gram_matrix(style_features[layer])
                   for layer in style_features}

    target = content.clone().requires_grad_(True).to(device)
    optimizer = torch.optim.Adam([target], lr=0.003)

    for step in range(steps):
        target_features = get_features(target, vgg)

        content_loss = torch.mean(
            (target_features['conv4_2'] - content_features['conv4_2']) ** 2
        )

        style_loss = 0
        for layer in style_grams:
            target_feature = target_features[layer]
            target_gram = gram_matrix(target_feature)
            style_gram = style_grams[layer]

            _, c, h, w = target_feature.shape
            layer_style_loss = torch.mean((target_gram - style_gram) ** 2)
            style_loss += layer_style_loss / (c * h * w)

        total_loss = content_weight * content_loss + style_weight * style_loss

        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()

    return target

