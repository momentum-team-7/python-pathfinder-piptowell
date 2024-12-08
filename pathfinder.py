from PIL import Image, ImageColor, ImageDraw
import random

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

# print(coordinates[1][0])

# print(coordinates)



# snags the minimum element and the maximum element from the list of lists
# that way we can determine what is going to be the darkest black(min_el)
# and the lightest white(max_el) for our grayscale 
min_el = int(min(map(min, coordinates)))
# print(min_el)

max_el = int(max(map(max, coordinates)))
# print(max_el)

minmax_range = (max_el) - (min_el)
# print(minmax_range)




# takes in an element from the list of lists, prints out the element in RGB format
def grayscale(elevation):
    int_elevation = int(elevation)
    diff = (int_elevation - min_el)
    # print(diff)
    percent_of_range = (diff/minmax_range)
    # print(percent_of_range)
    grayscale_value = (percent_of_range * 255)
    # print(grayscale_value)
    render_pixel = RGB(grayscale_value)
    # print(render_pixel)
    return render_pixel


# changes the calculation from the grayscale function to RGB(X,X,X) format
def RGB(grayscale_value):
    return (int(grayscale_value), int(grayscale_value), int(grayscale_value))


# allows for different images to be fed into the future render image function
dimensions = len(coordinates[0]), len(coordinates)


# generates the image from the .txt data with a nested loop; 
im = Image.new('RGB', (dimensions[0], dimensions[1]))
for x in range(dimensions[0]):
    for y in range(dimensions[1]):
        im.putpixel((y, x), grayscale(coordinates[x][y]))
im.save('elevation_small.png')   
print(im)

curr_cell = (0,300)


# takes current cell and outputs next cell choice based on closest elevation
# also handles equivalent elevation & coinflip edge cases 
def choose_path(curr_cell):
    fwd_cell = (curr_cell[0]+1, curr_cell[1])
    up_cell = (curr_cell[0]+1, curr_cell[1]-1)
    down_cell = (curr_cell[0]+1, curr_cell[1]+1)

    curr_cell_val = get_cell_value(curr_cell)
    fwd_cell_val = get_cell_value(fwd_cell)
    up_cell_val = get_cell_value(up_cell)
    down_cell = get_cell_value(down_cell)

    step_fwd = abs(curr_cell_vall - fwd_cell_val)
    step_up = abs(curr_cell_val - up_cell_val)
    step_down = abs(curr_cell_val - down_cell_val)

    if (step_fwd <= step_up) and (step_fwd <= step_down):
        next_cell = step_fwd
    elif (step_up < step_down):
        next_cell = step_up
    elif (step_down < step_up):
        next_cell = step_down
    else:
        up_or_down = [step_fwd, step_down]
        next_cell = coinflip(up_or_down)
        

    return next_cell


# takes in coordinates of cell and returns the value/elevation of coordinates
def get_cell_value(curr_cell):
    x = curr_cell[0]
    y = curr_cell[1]
    
    return int(coordinates[y,x])


# takes in both cell elevations in a list and returns one of their indexes randomly
def coinflip(up_or_down):
    return up_or_down[random.randint(0,1)]






# Greedy Algorithm
# X is always going to increment +1(right)
# Y might stay the same, or +1(down) or -1(up) depending on adjacent elevations
### this isn't what these variables actually are; just what you want to do if the algorithm's if statement chooses them; ie, how we increment the current cell based on the desired elevation choice



# start_pos = int(input("Where are you starting? (enter an integer from 0-9) "))

# start_pos = 4


# start of loop //// for each column in coordinates (refer to other loop?)

# gives you the elevation value in the cell
# current_elevation = coordinates[start_pos][0]

# gives you the x / y coordinates of the cell -- find a way to get this tomorrow (.indexOf)
# current_coordinate

# loop that gives us each coordinate, starting at 0,0 0,1 => 9,9
# for y in range(dimensions[1]):
#     for x in range(dimensions[0]):
            # print(y, x)


### lots of work done to figure out how to get the future function to work
# y = 4
# x = 0

# curr_cell_list = []
# potential_cells = []
# curr_coord_list = []
# pot_path_list = []

# # print(y, x)
# current_cell = (x, y)
# print('current cell is ', current_cell)
# curr_coord_list.append(current_cell)
# print(curr_coord_list)
# ## gives us the elevation
# # print(coordinates[y][x])
# curr_cell_elev = int(coordinates[y][x])
# print('current cell elev is ', curr_cell_elev)
# curr_cell_list.append(curr_cell_elev)



# fwd_cell = (x+1, y)
# print('fwd_cell is: ', fwd_cell)
# fwd_cell_elev = coordinates[y][x+1]
# pot_path_list.append(fwd_cell)
# print('fwd_cell_elev is: ', fwd_cell_elev)
# potential_cells.append(fwd_cell_elev)

# up_cell = (x+1, y-1)
# print('up_cell is ', up_cell)
# pot_path_list.append(up_cell)
# up_cell_elev = coordinates[y-1][x+1]
# print('up_cell_elev is ', up_cell_elev)
# potential_cells.append(up_cell_elev)

# down_cell = (x+1, y+1)
# print('down cell is ', down_cell)
# pot_path_list.append(down_cell)
# down_cell_elev = coordinates[y+1][x+1]
# print('down_cell_elev is ', down_cell_elev)
# potential_cells.append(down_cell_elev)

# # convert potential_cells list to integers to do absolute value math
# potential_cells = list(map(int, potential_cells))
# print('potential cells list: ', potential_cells)

# # check our cell lists
# print(curr_coord_list)
# print(pot_path_list)

# # do absolute value math
# nearest = min(potential_cells, key=lambda v: abs(curr_cell_elev-v))
# print(nearest)

# # delete first index from current cell list (old current cell, replace with new)
# curr_cell_list.append(nearest)
# print(curr_cell_list)
# del curr_cell_list[0]
# print(curr_cell_list)

# # clear potential_cells list for next loop
# potential_cells.clear()
# print(potential_cells)




# need code to put a pixel down here [function]

#take inventory of cells around you, add those variables to a new list [function]
# fwd_cell = coordinates[start_pos][x+1]
# up_cell = coordinates[start_pos-1][x+1]
# down_cell = coordinates[start_pos+1][x+1]
# potential_cells = []
# potential_cells.append(fwd_cell)
# potential_cells.append(up_cell)
# potential_cells.append(down_cell)

#  -- do comparison / absolute value math to determine which cell to move in to
# 
# 
# Stack Overflow example for finding nearest integer using absolute value3


# > nearest
# 600
# that cell becomes new current_cell? ( = current_cell /// reassign current_cell)
# empty potential_cells list?

# start loop over?

# (x in the loop will always increment once)
# if current_cell 




# loop over with new current cell

# handle edge cases with a coin flip and situations with equal elevations where forward cell always gets precedence for next current cell





# current_cell_elevation = coordinates[0][1]
## this yields the cell value of x 1 y 0 (you're in the first list[0], at index [1])
# print(current_cell_elevation)
## prints 4710 -- the value in the cell
# adj_cells = [(x+1,y)(x+1,y+1)(x+1,y-1)]
# fwd_cell = (x+1,y)
# up_cell = (x+1,y-1) 
# down_cell = (x+1,y+1)









# draws a one pixel line bisecting the image
# draw = ImageDraw.Draw(im)
# draw.line([(0,start_pos), (600,300)], fill=(255, 0, 0), width=1)
# im.save('elevation_small.png')



## Automate the Boring Stuff test code for .putpixel
# im = Image.new('RGB', (100, 100))
# for x in range(100):
#     for y in range(50,100):
#         im.putpixel((x,y), ImageColor.getcolor('darkgray', 'RGB'))
# im.save('putPixel.png')


