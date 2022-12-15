# Import math module so that math.pi can be 
# used in this program.
import math


def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} = {storage_efficiency:.2f}")

    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} = {storage_efficiency:.2f}")


    name = "#2"
    radius = 8.73
    height = 11.59
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} = {storage_efficiency:.2f}")

    name = "#2.5"
    radius = 10.32
    height = 11.91
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} = {storage_efficiency:.2f}")

    name = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} = {storage_efficiency:.2f}")

    name = "#5"
    radius = 13.02
    height = 14.29
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} = {storage_efficiency:.2f}")

    name = "#6Z"
    radius = 5.40
    height = 8.89
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} = {storage_efficiency:.2f}")

    name = "#8Z short"
    radius = 6.83
    height = 7.62
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} = {storage_efficiency:.2f}")

    name = "#10"
    radius = 15.72
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} = {storage_efficiency:.2f}")

    name = "#211"
    radius = 6.83
    height = 12.38
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} = {storage_efficiency:.2f}")
    
    name = "#300"
    radius = 7.62
    height = 11.27
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} = {storage_efficiency:.2f}")
    
    name = "#303"
    radius = 8.10
    height = 11.11
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} = {storage_efficiency:.2f}")

def compute_volume(radius, height):
    '''Compute and return the volume of the cylinder
    Parameters 
        radius of the cylinder
        height of the cylinder 
    Return: the volume of the cylinde.    
    '''
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    '''Compute and return the surface area of the cylinder
    Parameters 
        radius of the cylinder
        height of the cylinder 
    Return: the surface area of the cylinde.    
    '''
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

print()
main()