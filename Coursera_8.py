def area_triangle(base, height):
    area = (base * height) / 2
    return area
area_a=area_triangle(10, 5)
area_b=area_triangle(7, 3)
sum=area_a + area_b
print("The total area of the two triangles is: " + str(sum))