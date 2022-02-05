# BMP specification reference: https://en.wikipedia.org/wiki/BMP_file_format

# Import required libraries
import pygame, os

# Define BMP header data offsets
header_data = {
    "type": (0x0, 2),
    "size": (0x2, 4),
    "pixel_array": (0xa, 4),
    "width": (0x12, 4),
    "height": (0x16, 4),
    "col_depth": (0x1c, 2)
}

# Define functions

def open_image_file():

    image_file_path = input("Enter a file to open: ")

    try:
        image_file = open(image_file_path, "rb")
        return image_file, image_file_path

    except FileNotFoundError:
        print("Couldn't find that file!")

    if not validate_bmp_file(image_file, image_file_path):
        print("Invalid BMP file.")


def validate_bmp_file(image_file, image_file_path):
    # Return True or False depending on whether the file is an in-tact BMP file

    # First check the file starts with "BM" (0x42, 0x4D)
    image_file.seek(header_data["type"][0])
    header_file_type = image_file.read(header_data["type"][1])

    if header_file_type != b'\x42\x4d':
        return False

    # Confirm that the header's filesize matches the actual file size (to check for corruption)
    image_file.seek(header_data["size"][0])
    header_file_size = int.from_bytes(image_file.read(header_data["size"][1]), "little")
    actual_file_size = os.path.getsize(image_file_path)

    if header_file_size != actual_file_size:
        return False

    # If we've got this far then the BMP file must be valid, so return True
    return True


def get_colour_depth(image_file):
    # Return the colour-depth of the image as a integer
    image_file.seek(header_data["col_depth"][0])
    image_col_depth = int.from_bytes(image_file.read(header_data["col_depth"][1]), "little")
    return image_col_depth


def get_image_height(image_file):
    # Return the height of the image as an integer
    image_file.seek(header_data["height"][0])
    image_height = int.from_bytes(image_file.read(header_data["height"][1]), "little")
    return image_height


def get_image_width(image_file):
    # Return the width of the image as an integer
    image_file.seek(header_data["width"][0])
    image_width = int.from_bytes(image_file.read(header_data["width"][1]), "little")
    return image_width


def get_pixel_array_start(image_file):
    image_file.seek(header_data["pixel_array"][0])
    pixel_array_offset = int.from_bytes(image_file.read(header_data["pixel_array"][1]), "little")
    return pixel_array_offset


def byte_to_pixels(b):

    if type(b) != int:
        int_value = int.from_bytes(b, "little")
    else:
        int_value = b

    pixel_values = []

    binary_value = bin(int_value)  # Returns a string in the form "0bxxxxxxxx"

    binary_value = binary_value[2:]  # Cuts off the "0b" at the start

    binary_value = binary_value.zfill(8)  # Ensures 8-bit sequences for each byte

    for bit in binary_value:
        pixel_values.append(int(bit))

    return pixel_values


def get_pixels_for_row(image_file):

    global image_width

    # Extract a row of pixel values based on BMP's rules for 'packing' pixel rows to multiples of 4 bytes
    bytes_per_row = (image_width // 8)
    if image_width % 8 != 0:
        bytes_per_row += 1

    packed_bytes_per_row = bytes_per_row + 4 - (bytes_per_row % 4)

    row_bytes = image_file.read(packed_bytes_per_row)

    row_pixels = []

    for b in row_bytes:
        bit_string = bin(b)                 # Get the binary representation of byte b's value
        bit_string = bit_string[2:]         # Remove "0b" from the front
        bit_string = bit_string.zfill(8)    # Ensure that all bit strings are 8 bits long by prepending 0s to the start
        for bit in bit_string:
            row_pixels.append(int(bit))

    return row_pixels[:image_width]         # Return the pixel values up to the width of the image (discarding
                                            # additional "packed" byte values


def display_image(image_file):

    global windowDisplay, image_height, image_width

    colour_palette = {
        0: (0,0,0),
        1: (255, 255, 255)
    }

    image_file.seek(get_pixel_array_start(image_file))

    # for as many rows as there are in the file, display a row
    for y in range(image_height):

        # displaying a row involves reading the correct number of bytes for a row, converting them to pixel values
        # but only displaying as many are required by image_width
        row_pixels = get_pixels_for_row(image_file)

        for x in range(image_width):

            current_pixel = row_pixels[x]

            pygame.draw.rect(
                windowDisplay,                      # Where to display the rectangle - i.e. which window
                colour_palette[current_pixel],      # What colour the rectangle should be
                (x, image_height - y - 1, 1, 1)         # The position and size of the rectangle on the window
            )                                       # use image_height - y to flip the image

    pygame.display.update()  # Need this to actually display the 1x1 rectangles for each pixel!


# --------------------- Open file and display header information ---------------
# Get the name of the image file to read

image_file, image_file_path = open_image_file()

if not image_file:
    quit()

image_height = get_image_height(image_file)
image_width = get_image_width(image_file)
colour_depth = get_colour_depth(image_file)
pixel_array_start = get_pixel_array_start(image_file)

print("\nBMP file loaded successfully.\n\n"
    f"height: {image_height}, width: {image_width}, total pixels: {image_height*image_width}\n"
    f"Colour depth: {colour_depth}b/px, Pixel array starts at: {hex(pixel_array_start)}\n")
# ----------------------- Display window and bipmap data ----------------------
# Define the size of the game display window from the file size

# Get PyGame initialised
pygame.init()

# Setup surface / canvas (Entered as a Tuple () - return pygame object
windowDisplay = pygame.display.set_mode((image_width, image_height))

# Change the window title
pygame.display.set_caption(image_file_path)

# Display image


# --------------------------- Wait for the user to click to quit --------------

image_displayed = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Bye!')
            running = not running

    if not image_displayed:
        display_image(image_file)
        image_displayed = True

pygame.quit()