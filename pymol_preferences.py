#!/usr/bin/env python
"""
PyMOL preferences script
This script sets up custom visualization preferences in PyMOL.
Can be run directly in PyMOL or imported as a module.

Usage in PyMOL:
run path/to/pymol_preferences.py

Or import in another script:
import pymol_preferences
"""

from pymol import cmd

def set_preferences():
    """Set custom PyMOL visualization preferences"""
    # Cartoon appearance
    cmd.set('cartoon_highlight_color', 'grey90')
    cmd.set('cartoon_fancy_helices', 'on')
    cmd.set('cartoon_dumbbell_length', 1.2)
    cmd.set('cartoon_rect_length', 1.2)
    cmd.set('cartoon_rect_width', 0.25)
    
    # Lighting
    cmd.set('ray_shadow', 'off')

# Run preferences if script is executed directly
if __name__ == '__main__':
    set_preferences()
    print("PyMOL preferences have been set successfully!")