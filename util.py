import time
from colorama import Fore, Back, Style, init

start_color = Fore.RED
end_color = Fore.BLUE


def apply_two_color_gradient(ascii_art, start_color, end_color):
    lines = ascii_art.split("\n")

    for line in lines:
        gradient_length = len(line)
        colored_line = ""

        for i, char in enumerate(line):
            if i < gradient_length // 2:
                color = start_color
            else:
                color = end_color
            colored_line += color + char

        print(colored_line)
        time.sleep(0.05)


def generate_gradient(start, end, steps):
    gradient = []

    for i in range(steps):
        r1, g1, b1 = int(start[1:3], 16), int(start[3:5], 16), int(start[5:7], 16)
        r2, g2, b2 = int(end[1:3], 16), int(end[3:5], 16), int(end[5:7], 16)

        r = int(r1 + (r2 - r1) * (i / (steps - 1)))
        g = int(g1 + (g2 - g1) * (i / (steps - 1)))
        b = int(b1 + (b2 - b1) * (i / (steps - 1)))

        gradient.append(f"\033[38;2;{r};{g};{b}m")

    return gradient


def apply_gradient_to_ascii(ascii_art, color1, color2):
    def hex_to_rgb(hex_color):
        return tuple(int(hex_color[i : i + 2], 16) for i in (1, 3, 5))

    def rgb_to_hex(rgb_color):
        return "#" + "".join(f"{x:02X}" for x in rgb_color)

    def interpolate_colors(color1, color2, t):
        return (
            int(color1[0] + (color2[0] - color1[0]) * t),
            int(color1[1] + (color2[1] - color1[1]) * t),
            int(color1[2] + (color2[2] - color1[2]) * t),
        )

    color1_rgb = hex_to_rgb(color1)
    color2_rgb = hex_to_rgb(color2)

    ascii_lines = ascii_art.splitlines()
    num_lines = len(ascii_lines)

    gradient_ascii = []

    for i, line in enumerate(ascii_lines):
        t = i / (num_lines - 1) if num_lines > 1 else 0
        interpolated_color = interpolate_colors(color1_rgb, color2_rgb, t)
        hex_color = rgb_to_hex(interpolated_color)

        colored_line = "".join(
            f"\033[38;2;{interpolated_color[0]};{interpolated_color[1]};{interpolated_color[2]}m{char}"
            for char in line
        )
        gradient_ascii.append(colored_line)

    return "\n".join(gradient_ascii)


def print_gradient(text, color_start="#FF0000", color_end="#0000FF"):
    colored_ascii = apply_gradient_to_ascii(text, color_start, color_end)
    print(colored_ascii)
