def meal_time(time):
  hours,minutes = time.split(":")
  hours = int(hours)
  if 8>=hours>=7:
    return "breakfast"
  if 13>=hours>=12:
    return "lunch"
  if 19>=hours>=18:
    return "dinner"
  else: 
    return "nothing right now"

print("14:00: ",meal_time("14:00"))
print("7:00: ",meal_time("7:00"))
print("6:59: ",meal_time("6:59"))
print("18:50: ",meal_time("18:50"))
###

def get_filename_extension(file):
  name,extension=file.split(".")
  return name
print(get_filename_extension("potato.csv"))
print(get_filename_extension("coffee.png"))
print(get_filename_extension("hello.txt"))
###


def is_image_file(file):
  name,extension=file.split(".")
  if extension=="png" or extension=="jpg" or extension=="jpeg" or extension=="gif" or extension=="tiff":
    return True
  else:
    return False
print("doge.jpeg:",is_image_file("doge.jpeg"))
print("benchy.gcode:",is_image_file("benchy.gcode"))
print("classified.txt:",is_image_file("classified.txt"))
print("elmo.gif:",is_image_file("elmo.gif"))