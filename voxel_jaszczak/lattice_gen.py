import numpy as np

# ============================================================
# PHITS LATTICE COORDINATES
# ============================================================

xmin, xmax = 0, 19
ymin, ymax = -11,11
zmin, zmax = -11, 11

nx = xmax - xmin + 1
ny = ymax - ymin + 1
nz = zmax - zmin + 1

# Create the entire lattice as Universe 1
grid_3d = np.full((nz, ny, nx), 1, dtype=int)

# Fill the interior with Universe 2
grid_3d[1:-1, 1:-1, 1:-1] = 2
# ============================================================
# VOXEL PLACEMENT USING PHITS COORDINATES
# ============================================================

def set_voxel(x, y, z, universe):

    # Check PHITS lattice boundaries
    if not (xmin <= x <= xmax):
        raise ValueError(f"X={x} outside [{xmin}, {xmax}]")

    if not (ymin <= y <= ymax):
        raise ValueError(f"Y={y} outside [{ymin}, {ymax}]")

    if not (zmin <= z <= zmax):
        raise ValueError(f"Z={z} outside [{zmin}, {zmax}]")

    # Convert PHITS indices to NumPy indices
    ix = x - xmin
    iy = y - ymin
    iz = z - zmin

    grid_3d[iz, iy, ix] = universe


# ============================================================
# PLACE VOXELS HERE
# ============================================================






# ============================================================
# EXPORT
# ============================================================

chunk_size = 40

with open("lattice_3d.txt", "w") as f:
    for z in range(nz):
        for y in range(ny):
            row = grid_3d[z, y, :]

            for i in range(0, len(row), chunk_size):
                chunk = row[i:i + chunk_size]
                f.write("     " + " ".join(map(str, chunk)) + "\n")

print(f"Exported lattice_3d.txt ({nx}x{ny}x{nz} voxels).")
