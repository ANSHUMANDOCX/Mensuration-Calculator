import math

def circle_area(r, pi):
    return round(pi * (r ** 2), 2)

def circle_vol(r, pi):
    return round((4 / 3) * pi * (r ** 3), 2)

def circle_sa(r, pi):
    return round(4 * pi * (r ** 2), 2)

def rectangle_area(l, b):
    return round(l * b, 2)

def rectangle_vol(l, b, h):
    return round(l * b * h, 2)

def rectangle_sa(l, b, h):
    return round(2 * (l * b + b * h + l * h), 2)

def triangle_area(a1, a2, a3):
    s = (a1 + a2 + a3) / 2
    return round((s * (s - a1) * (s - a2) * (s - a3)) ** 0.5, 2)

def triangle_perimeter(a1, a2, a3):
    return round(a1 + a2 + a3, 2)

def cylinder_vol(r, h, pi):
    return round(pi * (r ** 2) * h, 2)

def cylinder_sa(r, h, pi):
    return round(2 * pi * r * (r + h), 2)

def cone_vol(r, h, pi):
    return round((1 / 3) * pi * (r ** 2) * h, 2)

def cone_sa(r, h, pi):
    return round(pi * r * (r + (r ** 2 + h ** 2) ** 0.5), 2)

def sphere_vol(r, pi):
    return round((4 / 3) * pi * (r ** 3), 2)

def sphere_sa(r, pi):
    return round(4 * pi * (r ** 2), 2)

def frustum_vol(R, r, h, pi):
    return round((1 / 3) * pi * h * (R ** 2 + R * r + r ** 2), 2)

def frustum_sa(R, r, h, pi):
    slant_height = ((R - r) ** 2 + h ** 2) ** 0.5
    return round(pi * (R + r) * slant_height + pi * R ** 2 + pi * r ** 2, 2)

def main():
    pi = math.pi
    shape = int(input("Select the shape \n1. Circle\n2. Rectangle\n3. Triangle\n4. Hollow objects\n5. Frustum\n"))
    
    if shape == 1:
        r = float(input("Enter the radius: "))
        option = int(input("Select the function \n1. Area\n2. Volume\n3. Surface Area\n"))
        if option == 1:
            print(circle_area(r, pi))
        elif option == 2:
            print(circle_vol(r, pi))
        elif option == 3:
            print(circle_sa(r, pi))
    
    elif shape == 2:
        l = float(input("Enter the length: "))
        b = float(input("Enter the breadth: "))
        h = float(input("Enter the height: "))
        option = int(input("Select the function \n1. Area\n2. Volume\n3. Surface Area\n"))
        if option == 1:
            print(rectangle_area(l, b))
        elif option == 2:
            print(rectangle_vol(l, b, h))
        elif option == 3:
            print(rectangle_sa(l, b, h))
    
    elif shape == 3:
        a1 = float(input("Enter the 1st side: "))
        a2 = float(input("Enter the 2nd side: "))
        a3 = float(input("Enter the 3rd side: "))
        option = int(input("Select the function \n1. Area\n2. Perimeter\n"))
        if option == 1:
            print(triangle_area(a1, a2, a3))
        elif option == 2:
            print(triangle_perimeter(a1, a2, a3))
    
    elif shape == 4:
        obj_type = int(input("Select the shape \n1. Cylinder\n2. Cone\n3. Sphere\n"))
        if obj_type == 1:
            r = float(input("Enter the radius: "))
            h = float(input("Enter the height: "))
            option = int(input("Select the function \n1. Volume\n2. Surface Area\n"))
            if option == 1:
                print(cylinder_vol(r, h, pi))
            elif option == 2:
                print(cylinder_sa(r, h, pi))
        elif obj_type == 2:
            r = float(input("Enter the radius: "))
            h = float(input("Enter the height: "))
            option = int(input("Select the function \n1. Volume\n2. Surface Area\n"))
            if option == 1:
                print(cone_vol(r, h, pi))
            elif option == 2:
                print(cone_sa(r, h, pi))
        elif obj_type == 3:
            r = float(input("Enter the radius: "))
            option = int(input("Select the function \n1. Volume\n2. Surface Area\n"))
            if option == 1:
                print(sphere_vol(r, pi))
            elif option == 2:
                print(sphere_sa(r, pi))
    
    elif shape == 5:
        frustum_type = int(input("Select the function \n1. Volume\n2. Surface Area\n"))
        R = float(input("Enter the radius of the larger base: "))
        r = float(input("Enter the radius of the smaller base: "))
        h = float(input("Enter the height: "))
        if frustum_type == 1:
            print(frustum_vol(R, r, h, pi))
        elif frustum_type == 2:
            print(frustum_sa(R, r, h, pi))
    
    else:
        print("Wrong option selected")


if __name__ == "__main__":
    main()