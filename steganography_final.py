def steganography_encoding(secret_message, input_image, output_image):
   

    password = input("enter password to encode: ")                              #making password for extra security
    if password !="12345":
        return("wrong password try again") 

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