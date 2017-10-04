
def draw_stars(arr):
    star_string = ''
    for thing in arr:
        if(type(thing) == str):
            for letter in range(len(thing)):
                star_string += str(thing[0])
            print star_string
            star_string = ''
        if(type(thing) == int):
            for star in range(0,thing):
                star_string += '*'
            print star_string
            star_string = ''

draw_stars([4,6,1,3,5,7,25])

x = [4, "Torn", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)