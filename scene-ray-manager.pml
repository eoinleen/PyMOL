from pymol import cmd
import time
import os

python

save_dir = r"C:\Users\fbselee\OneDrive - University of Leeds\Documents\EZ-lab\science\data\RFdiffusion\K11-Ub2_binder\2MBO\2MBO-12.result\PSE-analysis"

for i in range(1, 12):
    print(f"Processing scene F{i}")
    cmd.scene(f"F{i}")
    time.sleep(2)
    
    # Scale up the viewport size for higher resolution
    viewport_width = cmd.get_viewport()[0]
    viewport_height = cmd.get_viewport()[1]
    cmd.ray(width=viewport_width*300/72, height=viewport_height*300/72)
    
    filename = os.path.join(save_dir, f"scene_F{i}.png")
    cmd.png(filename, dpi=300)
    print(f"Saved {filename}")

python end
