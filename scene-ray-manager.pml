from pymol import cmd
import time
import os

python

# Set the save directory to where your .pse file is
save_dir = r"C:\Users\fbselee\OneDrive - University of Leeds\Documents\EZ-lab\science\data\RFdiffusion\K11-Ub2_binder\2MBO\2MBO-12.result\PSE-analysis"

# Force PyMOL to run through all scenes
for i in range(1, 12):
    print(f"Processing scene F{i}")
    cmd.scene(f"F{i}")
    time.sleep(2)
    cmd.ray(600)
    filename = os.path.join(save_dir, f"scene_F{i}.png")
    cmd.png(filename)
    print(f"Saved {filename}")

python end