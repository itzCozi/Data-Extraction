# this is a color file that can switch the color of the terminal/text 
# https://www.geeksforgeeks.org/color-cmd-command/ use this and remove colorama from the project

class colorCodes():
  black = 0
  blue = 1
  green = 2
  aqua = 3
  red = 4
  purple = 5
  yellow = 6
  white = 7
  grey = 8
  light_blue = 9
  light_green = A
  light_aqua = B
  light_red = C
  light_purple = D
  light_yellow = E
  light_white = F


class text():
  def Black():
    os.system("Color " + colorCodes.black)
    return "black"
  
  def Blue():
    os.system("Color " + colorCodes.blue)
    return "blue"


