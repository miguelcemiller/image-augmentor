import Augmentor

# create pipeline
p = Augmentor.Pipeline("image/", output_directory='../destination/')

# define augmentation techniques
p.rotate(probability=0.5, max_left_rotation=10, max_right_rotation=10)
p.shear(probability=0.5, max_shear_left=10, max_shear_right=10)
p.flip_random(probability=0.5)
p.zoom_random(1, percentage_area=0.8)
p.random_brightness(probability=0.5, min_factor=0.5, max_factor=0.5)

# generate 10 augmented images
p.sample(10)

