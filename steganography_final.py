def steganography_encoding(input_image, output_image):

    password = input("enter password to encode: ")                              #making password for extra security
    if password !="12345":
        return("wrong password try again") 
    
    choice = input("if you want to type the secret message type 1: \nif you want to upload text file type 2:\n")  #dual input that enables uploading file or message
    if choice == "1":
        secret_message = input("Enter message: ")
    
    elif choice == "2":
        filename = input("Enter filename: ")
        with open(filename, 'r') as f:
            secret_message = f.read()

    if secret_message == "":                                                    #first edge case to see if the message was empty
        return("this is an empty message write any thing to encode")
    
    binary_message = ""
    for char in secret_message:
        if ord(char) > 127 or ord(char) < 0:                                    #second edge case to see if there was any unsported chrachter
            return("the message contains undefined charachters")
        else:
            z = format(ord(char), "08b") 
            binary_message +=z
    binary_message += "11111111000000000"                                       #delimiter that will force decoding function to stop  
    
    with open(input_image, 'rb') as file:
        data = bytearray(file.read())                                                             
    
    if data[:2] != b'BM':                                                       #third edge case that checks if the image is an bmp extension
        return("This is not a bmp image ") 
    
    if len(binary_message) > len(data) - 54:                                    #fourth edge case that checks if the length of message is bigger than image size
        return("the message is too long that cannot fit the image")