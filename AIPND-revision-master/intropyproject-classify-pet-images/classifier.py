import ast
from PIL import Image
import torchvision.transforms as transforms
import torch
import torchvision.models as models

# Load pretrained models
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

models_dict = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Obtain ImageNet labels
with open(r'C:\\Users\\Hp\\OneDrive\\Desktop\\Udacity\\clone\\Udacity Project\\AIPND-revision-master\\intropyproject-classify-pet-images\\imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classifier(img_path, model_name):
    # Load the image
    img_pil = Image.open(img_path)

    # Define transforms
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # Preprocess the image
    img_tensor = preprocess(img_pil)
    
    # Resize the tensor (add dimension for batch)
    img_tensor = img_tensor.unsqueeze(0)
    
    # Apply model to input
    model = models_dict[model_name]
    
    # Put model in evaluation mode
    model.eval()
    
    # Disable gradient calculation
    with torch.no_grad():
        # Apply data to model
        output = model(img_tensor)
    
    # Return index corresponding to predicted class
    pred_idx = output.data.numpy().argmax()

    return imagenet_classes_dict[pred_idx]

# Example usage
if __name__ == "__main__":
    image_path = r'C:\\Users\\Hp\\OneDrive\\Desktop\\Udacity\\clone\\Udacity Project\\AIPND-revision-master\\intropyproject-classify-pet-images\\pet_images\\Golden_retriever_05195.jpg'  # Replace with your actual image path
    model_name = "vgg"  # Choose from 'resnet', 'alexnet', or 'vgg'
    prediction = classifier(image_path, model_name)
    print(f"Predicted Class: {prediction}")





