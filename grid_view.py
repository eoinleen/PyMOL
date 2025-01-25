"""
PyMOL Grid Visualization Script
Authors: Claude (Anthropic) & Dr Eoin Leen
Date: January 25, 2025

Purpose:
Automatically loads all PDB files from current directory into a grid layout with consistent coloring and styling.

Usage:
1. Open PyMOL
2. Navigate to directory containing PDB files: cd path/to/pdbs
3. Run script: run path/to/script/grid_view.py

Features:
- Loads all .pdb files from current directory
- Arranges structures in numerical order grid
- Colors chains: A (green), B (cyan), C (orange)
- Applies consistent cartoon representation and styling
"""

import glob, os
from pymol import cmd

cmd.delete('all')
pdbs = glob.glob("*.pdb")
pdbs.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

cmd.set('grid_mode', 1)
for pdb in pdbs:
   cmd.load(pdb)
   
cmd.set('grid_slot', -1)
cmd.show_as('cartoon')
cmd.color("green", "chain A and *")
cmd.color("cyan", "chain B and *")
cmd.color("orange", "chain C and *")

cmd.set('cartoon_highlight_color', 'grey90')
cmd.set('cartoon_fancy_helices', 'on')
cmd.set('cartoon_dumbbell_length', 1.2)
cmd.set('cartoon_rect_length', 1.2)
cmd.set('cartoon_rect_width', 0.25)
cmd.set('ray_shadow', 'off')