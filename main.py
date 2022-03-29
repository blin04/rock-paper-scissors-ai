import cv2
import os
import matplotlib.pyplot as plt
import numpy as np


def winner(player1, player2):
    # igrac moze odigrati: "rock", "paper", "scissors"
    # moguci ishodi: 1, 2, 0
    if player1 == player2:
        # nereseno
        return 0
    if player1 == "rock":
        if player2 == "paper":
            # pobedio je igrac 2
            return 2
        else:
            # pobedio je igrac1
            return 1
    elif player1 == "paper":
        if player2 == "scissors":
            return 2
        else:
            return 1
    else:
        if player2 == "rock":
            return 2
        else:
            return 1


def load_images(folder, label):
    img_data = []
    class_name = []  # labels

    for file in os.listdir(folder):
        image_path = os.path.join(folder, file)
        image = cv2.imread(image_path, cv2.COLOR_BGR2RGB)
        # imamo sliku kao trodimenzionalni niz sa vrednostima od 0 do 255
        image = np.array(image)
        # pretvaramo vrednosti u interval [0, 1]
        image = image.astype('float32')
        image /= 255
        img_data.append(image)
        class_name.append(label)

    return img_data, class_name


def create_dataset(img_folder):
    # ucitava slike i pravi od njih dataset
    data = []
    labels = []
    # zanimaju nas slova A, B, i V

    # privremena lista za skladistenje ucitanih slika, kako bi smo ih lakse
    # spojili u dataset
    for label in ["A"]:     # ovde bi trebalo biti ["A", "B", "V"]

        path = img_folder + "/" + label
        temp_data, temp_labels = load_images(path, label)

        data = data + temp_data
        labels = labels + temp_labels

    return data, labels


img_folder = "data/archive/asl_alphabet_train/asl_alphabet_train"
data, labels = create_dataset(img_folder)

plt.imshow(data[4])
plt.show()

