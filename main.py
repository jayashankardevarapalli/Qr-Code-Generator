import qrcode

i = input("\nEnter the data you want to store inside a qrcode!: ")

qrg = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,  border=2, box_size=20)
qrg.add_data(i)
qrg.make(fit=True)

qrc = qrg.make_image(fill_color="black", back_color="white")
o = input("\n Enter the output file name: ")
qrc.save(o + ".png")
print("\n\n\t\tQR Code Generated Successfully!!")
