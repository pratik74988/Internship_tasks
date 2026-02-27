# utils.py

from torchvision import transforms
from PIL import Image
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_image(image, max_size=256):
    transform = transforms.Compose([
        transforms.Resize(max_size),
        transforms.ToTensor()
    ])

    image = transform(image).unsqueeze(0)
    return image.to(device)