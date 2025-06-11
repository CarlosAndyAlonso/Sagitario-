import numpy as np
import trimesh
from trimesh.creation import box

def create_voxel_sphere(radius=10, num_cubes=500, cube_size=1.0, filename='voxel_sphere.glb'):
    # Parameter sampling
    root_n = int(np.sqrt(num_cubes))
    theta_vals = np.linspace(0, 2 * np.pi, root_n)
    phi_vals = np.linspace(0, np.pi, root_n)

    meshes = []

    for theta in theta_vals:
        for phi in phi_vals:
            x = radius * np.cos(theta) * np.sin(phi)
            y = radius * np.sin(theta) * np.sin(phi)
            z = radius * np.cos(phi)

            # Create cube at (x, y, z)
            cube = box(extents=(cube_size, cube_size, cube_size))
            cube.apply_translation([x, y, z])
            meshes.append(cube)

    # Combine all cubes
    full_mesh = trimesh.util.concatenate(meshes)

    # Export as GLB
    full_mesh.export(filename)
    print(f"Exported to {filename}")

# Run it
create_voxel_sphere(radius=10, num_cubes=500, cube_size=0.6)