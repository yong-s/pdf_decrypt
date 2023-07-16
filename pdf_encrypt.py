import os
from PyPDF2 import PdfReader, PdfWriter

def encrypt_pdf(input_path: str, output_path: str, password: str):
    # 如果输出文件路径为空，则使用默认的文件名格式
    if output_path == "":
        output_path = input_path + "_encrypted.pdf"

    reader = PdfReader(input_path)
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Add a password to the new PDF
    writer.encrypt(password)

    # Save the new PDF to a file
    with open(output_path, "wb") as f:
        writer.write(f)

# 调用函数进行加密
if __name__ == "__main__":
    input_path = input("Enter the path to the encrypted PDF file: ")
    password = input("Enter the path to the password: ")

    encrypt_pdf(input_path, password)


