from torchvision import transforms
from torchvision import models
import torch


class Model():
    def __init__(self):
        self.resnet50 = models.resnet50(pretrained=True)
        self.resnet50.eval()

        self.transform = transforms.Compose([transforms.Resize(256),
                                             transforms.CenterCrop(224),
                                             transforms.ToTensor(),
                                             transforms.Normalize(
                                             mean=[0.485, 0.456, 0.406],
                                             std=[0.229, 0.224, 0.225])])

    def check_similarity(self, image):
        image_tensor = torch.unsqueeze(self.transform(image), 0)
        out = self.resnet50(image_tensor)
        similarity = torch.nn.functional.softmax(out, dim=1)[0] * 100
        goldfish_similarity = similarity[1].item() # [1] is the goldfish class

        return goldfish_similarity
