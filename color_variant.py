
def color_variant(hex_color, brightness_offset=-20):
    """ takes a color like #87c95f and produces a lighter or darker variant. Default: darker 20%"""
    if len(hex_color) != 7:
        raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
    rgb_hex = [hex_color[x:x + 2] for x in [1, 3, 5]]
    new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
    rgb = [min([255, max([0, i])]) for i in new_rgb_int]  # make sure new values are between 0 and 255
    return "#{:02X}{:02X}{:02X}".format(rgb[0], rgb[1], rgb[2])


def start():
    print("Color variant program")
    print("Takes a color: str like #87c95f and produces a lighter (pos int) or darker (neg int) variant. Default: darker 20%")

    while True:
        color_hex = input("Enter hex: ")
        brightness = input("Enter brightness offset (optional):")
        brightness = int(brightness) if brightness != "" else -20
        print("New color: ", color_variant(color_hex, brightness))


start()
