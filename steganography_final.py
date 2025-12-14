#Encoding function 
def steganography_encoding(input_image, output_image):

    password = input("enter password to encode: ")                              #making password for extra security
    if password !="12345":
        return("wrong password try again") 
    
    choice = input("if you want to type the secret message type 1: \nif you want to upload text file type 2:\n")  #dual input that enables uploading file or message
    if choice == "1":
        secret_message = input("Enter message: ")
    
    elif choice == "2":
        filename = input("Enter filename: ")
        try:
            with open(filename, 'r') as file:
                secret_message = file.read()
        except FileNotFoundError:                                               #checks if text file doesn't exist
            return f"file {filename} not found"
        except:
            return f"Cannot read {filename}"
    else:
        return ("Invalid choice please enter 1, 2, or 3")

    if secret_message == "":                                                    #first edge case to see if the message was empty
        return("this is an empty message write any thing to encode")
    
    binary_message = ""
    for char in secret_message:
        if ord(char) > 127 or ord(char) < 0:                                    #second edge case to see if there was any unsported chrachter
            return("the message contains undefined charachters")
        else:
            z = format(ord(char), "08b") 
            binary_message +=z
    binary_message += "1111111100000000"                                       #delimiter that will force decoding function to stop  
    
    try:
        with open(input_image, 'rb') as file:
            data = bytearray(file.read())
    except FileNotFoundError:                                                   #third edge case file is not found
        return f"Error: File {input_image} not found!"
    except:
        return f"Error: Cannot read {input_image}!"                                                              
    
    if data[:2] != b'BM':                                                       #fourth edge case that checks if the image is an bmp extension
        return("This is not a bmp image ") 
    
    if len(binary_message) > len(data) - 54:                                    #fifth edge case that checks if the length of message is bigger than image size
        return("the message is too long that cannot fit the image")
    
    byte_index = 54                                                             #starting from 54 since first 54 byte is for bmp header. BMP bytes 54+ represent: B1, G1, R1, B2, G2, R2, ...
    for bit in binary_message: 
        data[byte_index] = (data[byte_index] & 0b11111110) | int(bit) 
        byte_index+=1
        if byte_index >= len(data):                                
            break
    
    with open(output_image, "wb") as file:
        file.write(data)
    return("messaage was hidden succssufully")

#----------------------------------------------------------------------------------------------------------------------

#Decoding function 
def decode_steganography(image_file):
    password = input("enter password to decode: ")                            #making password for extra security
    if password !="12345":
        return("wrong password try again")
    
    try:
        with open(image_file, 'rb') as file:                      
            data = bytearray(file.read())
    except FileNotFoundError:                                                 #checks if text file doesn't exist
        return f"File {image_file} not found"
    except:
        return f"Cannot read {image_file}"

    byte_index = 54                                                           #we start extracting LSB from bit-54 since we started editing in the 
    bits = ""
    message_bits = ""

    while byte_index < len(data):
        bits += str(data[byte_index] & 1)
        byte_index += 1

        if bits.endswith ("1111111100000000"):                                 #Delimiter check  
            message_bits = bits[0:-16]
            break

    message = ''
    for i in range(0,len(message_bits),8):
        message += chr(int(message_bits[i:i+8], 2))
    return message
#------------------------------------------------------------------------------------------------------------------

#user interface 
while True:
    print("----------------------------------------------------------------------------------")
    print("STEGANOGRAPHY APPLICATION")
    print("----------------------------------------------------------------------------------")
    print("1 Encode a message")
    print("2 Decode a message")
    print("3 Exit")
    print("----------------------------------------------------------------------------------")
    
    user_choice = input("Enter your choice 1, 2, or 3: ")                       #simple user interface to provide options 
    
    if user_choice == "1":
        input_image = input("Enter input BMP image: ")
        output_image = input("Enter output BMP image name: ")
        result = steganography_encoding(input_image, output_image)
        print(result)
        
    elif user_choice == "2":
        image_file = input("Enter encoded BMP image: ")
        result = decode_steganography(image_file)
        print(result)
        
    elif user_choice == "3":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice please enter 1, 2, or 3.")