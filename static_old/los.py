import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def unit_vector_from_angles(heading_angle_degrees, incidence_angle_degrees):
    # Convert angles to radians
    heading_angle_start_at_east = 90 - heading_angle_degrees
    heading_los = heading_angle_start_at_east + 90
    heading_angle_radians = np.radians(heading_los)

    incidence_angle_sensor_to_ground = -(90 - incidence_angle_degrees)
    incidence_angle_radians = np.radians(incidence_angle_sensor_to_ground)

    # Calculate the vector components
    x_component = np.cos(heading_angle_radians) * np.cos(incidence_angle_radians)
    y_component = np.sin(heading_angle_radians) * np.cos(incidence_angle_radians)
    z_component = np.sin(incidence_angle_radians)

    # Create a NumPy array for the vector
    vector = np.array([x_component, y_component, z_component])

    # Normalize the vector to obtain the unit vector
    unit_vector = (vector / np.linalg.norm(vector)).round(5)

    return unit_vector


def unit_vector_to_rgb(unit_vector):
    centered_rgb = (unit_vector * 127.5) + 127.5
    rounded = centered_rgb.round(0).astype(int)
    return rounded


def angles_to_rgb(heading_angle_degrees, incidence_angle_degrees, hex=False):
    unit_vector = unit_vector_from_angles(heading_angle_degrees, incidence_angle_degrees)
    rgb = unit_vector_to_rgb(unit_vector)
    r, g, b = rgb
    if hex:
        hex_color = f'#{r:02X}{g:02X}{b:02X}'
        return hex_color
    return rgb


def create_mogi(size, delta_V):
    # Define Mogi source parameters
    # delta_V = 100.0  # Volume change (cubic meters)
    depth = 5.0  # Depth of the source (meters)
    nu = 0.25  # Poisson's ratio

    # Create a grid of (x, y) coordinates
    x = np.linspace(-10, 10, size)  # Adjust the range and resolution as needed
    y = np.linspace(-10, 10, size)
    X, Y = np.meshgrid(x, y)

    # Calculate surface displacements for each point in the grid
    mogi = (delta_V / (np.pi * (1 - nu))) * (depth / (X**2 + Y**2 + depth**2) ** (3 / 2))
    return mogi


def plot_mogi():
    size = Element('test-input').element.value

    if size == '':
        size = 100

    mogi = create_mogi(100,size)

    fig, ax = plt.subplots(dpi=300)
    ax.imshow(mogi)
    display(fig)
