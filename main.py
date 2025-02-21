import numpy as np
from PIL import Image
import qrcode

def inject():
    input("Prepare the original.png and qr.png, and press Enter.")
    
    with Image.open("original.png") as input_img:
        input_img.load()
    input_img = input_img.convert("RGBA")
    img_array = np.array(input_img)
    
    with Image.open("qr.png") as input_qr:
        input_qr.load()
    qr_array = np.array(input_qr)
    
    channel = int(input("Select the channel (1 - R, 2 - G, 3 - B): "))
    channel -= 1
    
    qr_size = qr_array.shape[0]
    width = img_array.shape[1]
    height = img_array.shape[0]
    
    print("Select QR code placement:")
    print("1    2    3    4    5")
    print("□■   ■□   ■■   ■■   Custom\n■■   ■■   □■   ■□")
    pos_option = input()
    if pos_option == "1":
        pos_x = 0
        pos_y = 0
    elif pos_option == "2":
        pos_x = width - qr_size
        pos_y = 0
    elif pos_option == "3":
        pos_x = 0
        pos_y = height - qr_size
    elif pos_option == "4":
        pos_x = width - qr_size
        pos_y = height - qr_size
    else:
        pos_x, pos_y = map(int, input().split())
    
    print("Injecting...")
    for col in range(qr_size):
        for row in range(qr_size):
            pix_img = img_array[pos_y + row, pos_x + col][channel]
            pix_qr = qr_array[row, col]
            
            sign = 1
            if pix_img == 255:
                sign = -1
            
            img_array[pos_y + row, pos_x + col][channel] += ((pix_img % 2) ^ pix_qr) * sign
    
    output_img = Image.fromarray(img_array)
    output_img.save("injected.png")
    print("Done (injected.png).")
    
    print()

def qr_gen():
    input("Prepare the text.txt and press Enter.")
    
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1,
    )
    
    filename = "text.txt"
    with open(filename, encoding="utf8") as file:
        text = file.read()
    
    qr.add_data(text)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr.png")
    print("QR code generated.")
    
    print()

def inspect():
    input("Prepare the injected.png and press Enter.")
    
    with Image.open("injected.png") as input_img:
        input_img.load()
    input_img = input_img.convert("RGBA")
    img_array = np.array(input_img)
    
    channel = int(input("Select the channel (1 - R, 2 - G, 3 - B): "))
    channel -= 1
    
    print("Transforming...")
    width = img_array.shape[1]
    height = img_array.shape[0]
    for col in range(width):
        for row in range(height):
            img_array[row, col][channel] = (img_array[row, col][channel] % 2) * 255
            img_array[row, col][(channel + 1) % 3] = 0
            img_array[row, col][(channel + 2) % 3] = 0
    
    output_img = Image.fromarray(img_array)
    output_img.save("inspected.png")
    
    print("Done (inspected.png). Enter anything to show the image, enther nothing to skip.")
    show_img = input()
    if show_img != "":
        output_img.show()
    
    print()

def main():
    print("Enter the number:")
    print("1 - Inject QR code into image")
    print("2 - Generate QR code from text file")
    print("3 - Trasform image for inspection")
    print("0 - Exit")
    command = input()
    print()
    
    if command == "0":
        return True
    elif command == "1":
        inject()
    elif command == "2":
        qr_gen()
    elif command == "3":
        inspect()
    
    return False

quit_ = False
while quit_ == False:
    quit_ = main()
