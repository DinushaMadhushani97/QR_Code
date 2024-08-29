#Import necessary Libraries
import qrcode 
import image # 

qr = qrcode.QRCode(
    version = 15, # Version parameter controls the size of the QR code. Higher numbers mean larger size with more data.
    box_size = 10, #size of the box
    border =5 #white of the image --which is the border in all 4 slides with white color.

)

#Scanned Message
data = "Hi, Welcomer"

# Adding the data to the QR code
qr.add_data(data)
qr.make(fit = True)

# Creating an image of the QR code with specified colors
img = qr.make_image(fill="black", back_color = "white")

# Saving the generated QR code as a PNG image
img.save("test.png")
