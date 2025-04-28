import sympy as sp
from sympy.abc import rho, phi, theta, r, x, y, z

def coordinate_converter():
    print("Coordinate Equation Converter")
    print("Supported coordinate systems: cartesian, cylindrical, spherical")
    
    # Get user input
    equation_str = input("Enter the equation (use x, y, z for cartesian; r, phi, z for cylindrical; rho, theta, phi for spherical): ")
    original_system = input("Enter the original coordinate system (cartesian/cylindrical/spherical): ").lower()
    target_system = input("Enter the target coordinate system (cartesian/cylindrical/spherical): ").lower()
    
    # Parse the equation
    try:
        equation = sp.sympify(equation_str)
    except:
        print("Invalid equation format. Please use proper symbolic notation.")
        return
    
    # Conversion dictionaries
    cartesian_to_cylindrical = {
        x: r * sp.cos(phi),
        y: r * sp.sin(phi),
        z: z
    }
    
    cylindrical_to_cartesian = {
        r: sp.sqrt(x**2 + y**2),
        phi: sp.atan2(y, x),
        z: z
    }
    
    cartesian_to_spherical = {
        x: rho * sp.sin(theta) * sp.cos(phi),
        y: rho * sp.sin(theta) * sp.sin(phi),
        z: rho * sp.cos(theta)
    }
    
    spherical_to_cartesian = {
        rho: sp.sqrt(x**2 + y**2 + z**2),
        theta: sp.acos(z / sp.sqrt(x**2 + y**2 + z**2)),
        phi: sp.atan2(y, x)
    }
    
    cylindrical_to_spherical = {
        r: rho * sp.sin(theta),
        phi: phi,
        z: rho * sp.cos(theta)
    }
    
    spherical_to_cylindrical = {
        rho: sp.sqrt(r**2 + z**2),
        theta: sp.atan2(r, z),
        phi: phi
    }
    
    # Perform the conversion
    try:
        if original_system == "cartesian":
            if target_system == "cylindrical":
                converted = equation.subs(cartesian_to_cylindrical)
            elif target_system == "spherical":
                converted = equation.subs(cartesian_to_spherical)
            else:
                converted = equation
                
        elif original_system == "cylindrical":
            if target_system == "cartesian":
                converted = equation.subs(cylindrical_to_cartesian)
            elif target_system == "spherical":
                converted = equation.subs(cylindrical_to_spherical)
            else:
                converted = equation
                
        elif original_system == "spherical":
            if target_system == "cartesian":
                converted = equation.subs(spherical_to_cartesian)
            elif target_system == "cylindrical":
                converted = equation.subs(spherical_to_cylindrical)
            else:
                converted = equation
        else:
            print("Invalid coordinate system specified.")
            return
            
        # Simplify the result
        converted = sp.simplify(converted)
        
        print("\nOriginal equation in", original_system, "coordinates:")
        print(sp.pretty(equation))
        print("\nConverted equation in", target_system, "coordinates:")
        print(sp.pretty(converted))
        
    except Exception as e:
        print("An error occurred during conversion:", str(e))

if __name__ == "__main__":
    coordinate_converter()