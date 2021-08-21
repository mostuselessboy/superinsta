from PIL import Image
def reshape(filename):
   def reshape_image(image):
       old_size = image.size
       max_dimension, min_dimension = max(old_size), min(old_size)
       desired_size = (max_dimension, max_dimension)
       position = int(max_dimension/2) - int(min_dimension/2) 
       blank_image = Image.new("RGB", desired_size, color='#1d1d1d')
       if image.height<image.width:
           blank_image.paste(image, (0, position))
       else:
           blank_image.paste(image, (position, 0))
       return blank_image
   test_image = Image.open(filename)
   new_image = reshape_image(test_image)
   new_image.save(filename)

