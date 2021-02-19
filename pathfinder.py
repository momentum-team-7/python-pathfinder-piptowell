from PIL import Image
from PIL import ImageColor

file_small = 'elevation_small.txt'
file_large = 'elevation_large.txt'

file_test = 'testgrid.txt'

# im = Image.open('elevation_small.txt')
coordinates = []

# get dimensions of the photo [put in file // get out length and height]
# def get_dimensions(elevation_file):
#     with open(elevation_file) as file: 
#         for line in file.readlines():
#             coordinates.append(line.split())
#         print(len(coordinates[0]))
#         print(len(coordinates))

# for elem in coordinates:





# opens the file and creates a for loop for each line in the file
# for each line, append that line to coordinates, while making
# each piece of elevation in that line into a 'string'
# this allows us to preserve the order of the lists so that we can reconstruct them later
with open(file_small) as file: 
    for line in file.readlines():
        coordinates.append(line.split())
    # print(len(coordinates))
    # print(len(coordinates[0]))

print(coordinates[1][8])

for x in range(9):
        for y in range(9):
            print(x,y, )




# snags the minimum element and the maximum element from the list of lists
# that way we can determine what is going to be the darkest black(min_el)
# and the lightest white(max_el) for our grayscale 
min_el = int(min(map(min, coordinates)))
# print(min_el)

max_el = int(max(map(max, coordinates)))
# print(max_el)

minmax_range = int(max_el - min_el)
# print(minmax_range)

elevation = 4713
# print(coord)





# takes in an element from the list of lists, prints out the element in RGB format
def grayscale(elevation):
    diff = (elevation - min_el)
    # print(diff)
    percent_of_range = (diff/minmax_range)
    # print(percent_of_range)
    grayscale_value = (percent_of_range * 255)
    # print(grayscale_value)
    render_pixel = RGB(grayscale_value)
    print(render_pixel)


# changes the calculation from the grayscale function to RGB(X,X,X) format
def RGB(grayscale_value):
    return (int(grayscale_value), int(grayscale_value), int(grayscale_value))



grayscale(elevation)

im = Image.new('RGB', (600, 600))
for x in range(600):
    for y in range(600):
        im.putpixel((x, y), render_pixel)
im.save('elevation_small.png')   
print(im)



## Automate the Boring Stuff test code for .putpixel
im = Image.new('RGB', (100, 100))
for x in range(100):
    for y in range(50,100):
        im.putpixel((x,y), ImageColor.getcolor('darkgray', 'RGB'))
im.save('putPixel.png')