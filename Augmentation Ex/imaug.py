import torchvision.transforms as transforms
from torchvision.utils import save_image
import glob
import os
from PIL import Image

images_path = '../dataset_captioning/Flicker8k_Dataset/'
target_path = 'image_output'

preprocessing = transforms.Compose([
            transforms.RandomHorizontalFlip(p=1),
            transforms.RandomResizedCrop(size=(224, 224))
        ])

img = glob.glob(images_path + '*.jpg')  # read images name in folder

for i in img:
    img_pil = Image.open(i).convert("RGB")
    proc_img = preprocessing(img_pil)
    filename = i[len(images_path):-4]
    filepath = os.path.join(target_path, f"{filename}_4.jpg")
    proc_img.save(filepath)
