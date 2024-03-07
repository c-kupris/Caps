import pyvista as pv


def create_cap_stl_file(face_width, face_height, output_path='cap_model.stl'):
    # Convert diameter from inches to meters
    cap_diameter = 0.508  # 20 inches in meters

    # Calculate cap radius
    cap_radius = face_width / 2

    cap_height = face_height

    cap_mesh = pv.Cylinder(radius=cap_radius,
                           height=cap_height,
                           center=(0, 0, cap_height / 2),
                           direction=(0, 0, 1))

    # Save the STL file
    cap_mesh.save(output_path)


if __name__ == "__main__":
    # REPLACE THE 'face_width' AND 'face_height'
    # VARIABLES BELOW IN LINE 24 WITH YOUR MEASUREMENTS FOR THOSE RESPECTIVE THINGS.

    # Create and save the STL file
    create_cap_stl_file(face_width, face_height, output_path='~/Desktop/cap_model.stl')
    print("STL file saved to the desktop.")
