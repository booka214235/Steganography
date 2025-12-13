def steganography_encoding(secret_message, input_image, output_image):
   
    if secret_message == "":                                                      #first edge case
        return("this is an empty message write any thing to encode")
    
    binary_message = ""
    for char in secret_message:
        if ord(char) > 127 or ord(char) < 0:                                      #second edge case joo
            return("the message contains undefined charachters")
        else:
            z = format(ord(char), "08b") 
            binary_message +=z
    binary_message += "00000000"                                             #delimiter 
    
    