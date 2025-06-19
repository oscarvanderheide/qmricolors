#!/usr/bin/env python3
"""
Simple test for VisPy colormap without GUI.
"""

import numpy as np
import sys
import os

# Add the current directory to the path so we can import qmricolors
sys.path.insert(0, os.path.dirname(__file__))

import qmricolors

def test_vispy_colormap_simple():
    """Test vispy colormap functionality without GUI."""
    print("Testing VisPy colormap (no GUI)...")
    
    try:
        from vispy.color import get_colormap
        
        # Get our custom colormaps
        lipari_cmap = get_colormap('lipari')
        navia_cmap = get_colormap('navia')
        
        print(f"Lipari colormap: {lipari_cmap}")
        print(f"Navia colormap: {navia_cmap}")
        
        # Test colormap functionality
        test_values = np.linspace(0, 1, 10)
        lipari_colors = lipari_cmap.map(test_values)
        navia_colors = navia_cmap.map(test_values)
        
        print(f"Lipari colors shape: {lipari_colors.shape}")
        print(f"Navia colors shape: {navia_colors.shape}")
        print(f"First lipari color (RGBA): {lipari_colors[0]}")
        print(f"Last navia color (RGBA): {navia_colors[-1]}")
        
        print("✓ VisPy colormap test successful!")
        return True
        
    except Exception as e:
        print(f"✗ VisPy colormap test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_vispy_gui():
    """Test vispy with GUI - minimal example."""
    print("\nTesting VisPy with GUI...")
    
    try:
        from vispy import app, scene
        from vispy.color import get_colormap
        
        # Check if we can create an app
        vispy_app = app.use_app()
        print(f"Using backend: {vispy_app.backend_name}")
        
        if vispy_app.backend_name == 'None':
            print("No GUI backend available")
            return False
        
        # Create minimal canvas
        canvas = scene.SceneCanvas(
            size=(400, 300),
            title="qMRI Colors Test",
            show=False  # Don't show initially
        )
        
        # Test showing the canvas
        canvas.show()
        print("Canvas created and shown successfully")
        
        # Close after a short time
        canvas.close()
        print("✓ VisPy GUI test successful!")
        return True
        
    except Exception as e:
        print(f"✗ VisPy GUI test failed: {e}")
        return False

if __name__ == "__main__":
    print("qMRI Colors VisPy Test")
    print("======================")
    
    # Test colormap functionality
    success1 = test_vispy_colormap_simple()
    
    # Test GUI functionality
    success2 = test_vispy_gui()
    
    if success1 and success2:
        print("\n✓ All tests passed!")
    elif success1:
        print("\n⚠ Colormap works but GUI may have issues")
    else:
        print("\n✗ Tests failed")