import  qrcode
import image
difficulty = int(input("Enter the difficulty of the QR Code (5 - 15): "))
backColor = input("Enter the Background Color for the Image: ")
qr = qrcode.QRCode(
    version= difficulty, # controls the size of the QR Code/simply it increases
    box_size = 15, # Size of the box in which QR has to be generated
    border= 1, #white part of the image -- border in all 4 sides with color
)

data = input("Enter the URL to be coded: ") #"https://github.com/Musharraffaijaz"
qr.add_data(data)
qr.make(fit=True)
qr_img = qr.make_image(fill="black",  back_color = backColor)
qr_img.save("QRGeneratedImage.png")
print("The QR has been generated")