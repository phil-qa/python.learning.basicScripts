#get values for the dimensions of the area and the coverage of a tin as well as a price for each tin
width = int(input('How wide is the wall ?:'))
height = int(input('How High is the wall ?:'))
coverage = float(input('How much will one tin of paint cover ?:'))
cost = float(input('How much does a tin cost ?:'))

area = width * height
cans = area /coverage
if int(cans) < cans:
    cans = int(cans + 1)
total_cost = cost * cans


#Set to a function for repeatative operations



#include VAT

#Include doors

print(f"The area to cover is :{coverage}M(^2), which requires {cans} Cans of paint, at a cost of £{cost} ")