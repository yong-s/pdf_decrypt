from PyPDF2 import PdfReader

def decrypt_pdf(pdf_path: str, password_dir: str):
    reader = PdfReader(pdf_path)
    
    # Try to decrypt the PDF using passwords from a file
    with open(password_dir, 'r') as f:
        passwords = f.readlines()
        success = False  # 标记是否成功解密
        
        for password in passwords:
            password = password.strip()
        
            try:
                print("正在破解，使用密码：", password)
                
                if reader.is_encrypted:
                    reader.decrypt(password)
                    
                    if len(reader.pages) > 0:
                        print("破解成功，密码是：", password)
                        success = True  # 成功解密
                        break  # 结束循环
                else:
                    print("该文件未加密!")
                
            except:
                print("破解失败，换个密码试试")

    if not success:
        print("无法破解该文件。")

    # 返回成功或失败的标志
    return success
                           
            
if __name__ == "__main__":
    pdf_path = input("Enter the path to the encrypted PDF file: ")
    password_dir = input("Enter the path to the password file: ")

    decrypt_pdf(pdf_path, password_dir)
