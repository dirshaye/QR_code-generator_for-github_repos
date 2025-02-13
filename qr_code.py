import qrcode

def generate_qr_code(data, filename="qrcode.png", size=10, border=4):
    """
    Generates a QR code and saves it as an image file.
    
    :param data: The data to encode in the QR code.
    :param filename: The name of the output image file (default is 'qrcode.png').
    :param size: The size of the QR code (default is 10).
    :param border: The border size of the QR code (default is 4).
    """
    qr = qrcode.QRCode(
        version=None,  # Adjusts the size automatically
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    data = input("Enter the data to encode in the QR code: ")
    filename = input("Enter the output filename (or press Enter for default 'qrcode.png'): ") or "qrcode.png"
    generate_qr_code(data, filename)
