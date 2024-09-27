'''
Thomas Butkiewicz
This Code is an algorithm to determine the postage cost for entered mail
CS2
9/26/24
Bugs: 
'''


def main():                                                                # main function
    print("Welcome to the GCDS Post Office!")                              # prints welcome
    data = input("Enter height, length, thickness, zipcode1, zipcode2: ")  # input data to analyse

    dimensions = data.split(",")                                           # where the data splits
    height = float(dimensions[0])                                          # where the height data goes
    length = float(dimensions[1])                                          # where the length data goes
    thickness = float(dimensions[2])                                       # where the thickness data goes
    zipcode1 = int(dimensions[3])                                          # stores the zipcode1
    zipcode2 = int(dimensions[4])                                          # stores the zipcode2

    mailtype = postage_size( height, length, thickness)                    # when you enter the dimensions 
    print (mailtype)
    
    cost = 0 
    distance = 0

    distance = getZones(zipcode1) - getZones(zipcode2)


    if mailtype == "POST CARD":
        cost = .20 + .03 * distance
    
    elif mailtype == "LARGE POST CARD":
        cost = .37 + .03 * distance

    elif mailtype == "ENVELOPE":
        cost = .37 + .04 * distance
    
    elif mailtype == "LARGE ENVELOP":
        cost = .60 + .05 * distance

    elif mailtype == "PACKAGE":
        cost = 2.95 + .25 * distance

    elif mailtype == "LARGE PACKAGE":
        cost = 3.95 + .35 * distance
   
def getZones(zip):                                              # zipcode function

    if zip >= 1 and zip <= 6999:
        return 1
    
    if zip >= 7000 and zip <= 19999:
        return 2

    if zip >= 20000 and zip <= 35999:
        return 3

    if zip >= 36000 and zip <= 62999:
        return 4

    if zip >= 63000 and zip <= 84999:
        return 5
    
    if zip >= 85000 and zip <= 99999:
        return 6

def postage_size(height, length, thickness):

    if height >= 3.5 and height <= 6 and length >= 3.5 and length <= 4.25 and thickness >= .007 and thickness <= .016:
        return "POST CARD"
    
    elif height >= 6 and height <= 11.5 and length >= 4.25 and length <= 6 and thickness >= .007 and thickness <= .015:
        return "LARGE POST CARD"
    
    elif height >= 5 and height <= 11.5 and length >= 3.5 and length <= 6.125 and thickness >= .016 and thickness <= .025:
        return "ENVELOPE"
    
    elif height >= 11 and height <= 18 and length >= 6.125 and length<= 24 and thickness >= .25 and thickness <= .5:
        return "LARGE ENVELOP"
    
    elif height >=18 and length >=24 and thickness >= .5 and 2*length + 2*thickness <= 84:
        return "PACKAGE"

    elif length + 2*height + 2*thickness >= 84 and length + 2*height + 2*thickness <= 130:
        return "LARGE PACKAGE"
    else:
        return "THIS PACKAGE IS UNMAILABLE"
        sys.exit
    
def get_cost(postage_type, zones):
    pass
main()





















































