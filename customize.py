"""
This file calculates the cost and power generation
by a house, Assignment 1, Comp 130
"""

import math

def cost(living_wid, off_len, num_br, br_wid, br_len, mbr_wid, mbr_len):
    """
    This function calculates the cost of the house
    """
    # Creating Variable called area which stores total area
    area=0
    #Here in my garage
    area+=22*24
    #Kitchen + Living Area
    area+=24*living_wid
    #Master Bedroom
    area+=mbr_wid*mbr_len
    #Master Bathroom
    area+=12*mbr_len
    #All non MBR bedrooms
    area+=br_wid*br_len*num_br
    #Office
    area+=(4+br_wid)*off_len
    #Bathrooms
    area+=10*br_wid*2 #two Bathrooms
    #Hallway
    area+=4*(10+10+br_len*num_br)
    print("area is" + str(area))
    #Creating Perimeter Variable
    perim=0
    #Garage and Kitchen
    perim+=24+(22+living_wid)*2
    #MBR and MB
    perim+=mbr_len*2+(mbr_wid+12)*2-4-br_wid
    #Offices and stuff
    perim+=4+br_wid+(off_len+10+10+br_len*num_br)*2-24
    print("perim is "+str(perim))
    #Finally calculating cost
    return 80*perim+100*area


def solar(off_len, num_br, br_wid, br_len, mbr_len):
    """
    This function calculates the power generated by the house
    """
    sqr_meter = 0.092903
    #Shall we begin
    #Calculating area of solar panels
    solar_area =(4+br_wid)*(off_len+10+10+br_len*num_br+mbr_len)
    solar_area/=math.cos(25.9*math.pi/180)
    #Converting to meters
    slr_metres = solar_area*sqr_meter
    #Calculating Power
    power=slr_metres*6.1*0.22 #6.1KWH per day and 22% efficiency
    #I don't know why I didn't just return it earlier
    return power

print(cost(10,4,0,18,1,12,10))

# Uncomment the following two lines to use a visual interface to your code.
# Keep them commented when using OwlTest or submitting.
#import comp130_houseplan_display as display
#display.display(cost, solar)
