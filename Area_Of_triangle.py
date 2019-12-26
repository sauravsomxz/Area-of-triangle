# Author : Saurav Ranajan Maharana
# Date : 23rd November, 2019
# Purpose : Learning Py!
# Contact : saurav.maharana07@gmail.com
# Title : Finding area of triangle using sides

side1 = float(input("Enter Side 1 : "))
side2 = float(input("Enter Side 2 : "))
side3 = float(input("Enter Side 3 : "))
semi_perimeter = (side1+side2+side3)/2
area_of_triangle = (semi_perimeter*(semi_perimeter-side1)*(semi_perimeter-side2)*(semi_perimeter-side3)) ** 0.5
area_of_triangle = round(area_of_triangle, 2)
print("Semi-perimeter is : ", semi_perimeter)
print("Area of Triangle is : ", area_of_triangle)
