from stepfg import generate_step

# Coordinates outlining the flat-bottomed base and organic spine profile
chameleon_profile = [
    [150, 400], [235, 400], [280, 360], [320, 350], [350, 400], # Flat base & legs
    [550, 400], [570, 350], [600, 320], [650, 330], [760, 330],
    [800, 195], [830, 230], [870, 170], [700, 200], [450, 100], # Upper back and tail arcs
    [250, 110], [130, 150], [150, 250]
]

# Extrude the 2D path into a 3D CAD solid along the Z-axis (80mm deep lamp body)
step_data = generate_step(
    polygons=[chameleon_profile],
    z_range=[0, 80],
    scale=1.0
)

# Instantly saves a valid, native ISO 10303-21 STEP asset to your computer
with open("chameleon_lamp_base.step", "w") as f:
    f.write(step_data)

print("SUCCESS: 'chameleon_lamp_base.step' has been created for your P1S printer!")
