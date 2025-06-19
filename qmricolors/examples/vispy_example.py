#!/usr/bin/env python3
"""
VisPy example for qMRI Colors package.

This script demonstrates how to use the custom colormaps with VisPy.
"""

import numpy as np
import sys
import os

# Add the parent directory to the path so we can import qmricolors
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Import qmricolors - this automatically registers the colormaps
import qmricolors


def vispy_example():
    """Demonstrate vispy usage."""
    print("Creating vispy example...")
    
    try:
        from vispy import app, scene
        from vispy.color import get_colormap
        import vispy
        
        print(f"VisPy version: {vispy.__version__}")
        
        # Check available backends
        print("Available backends:", app.backends.BACKEND_NAMES)
        
        # Create sample data
        data = np.random.rand(100, 100)
        
        # Get our custom colormap
        lipari_cmap = get_colormap('lipari')
        print(f"Successfully loaded lipari colormap: {lipari_cmap}")
        
        # Create an app instance
        vispy_app = app.use_app()
        print(f"Using backend: {vispy_app.backend_name}")
        
        # Create a canvas and add an image
        canvas = scene.SceneCanvas(
            keys='interactive',
            show=True,
            size=(800, 600),
            title="qMRI Colors - Lipari Colormap Example"
        )
        view = canvas.central_widget.add_view()
        
        # Add image with custom colormap
        image = scene.visuals.Image(data, cmap=lipari_cmap, parent=view.scene)
        view.camera = scene.PanZoomCamera(aspect=1)
        view.camera.set_range()
        
        print("VisPy window should be visible now.")
        print("Press 'q' to quit or close the window to continue.")
        
        # Run the app - this should show the window
        if sys.platform == "darwin":  # macOS
            canvas.show()
            app.run()
        else:
            app.run()
        
    except ImportError as e:
        print(f"VisPy not available or missing dependencies for GUI: {e}")
    except Exception as e:
        print(f"Error creating VisPy example: {e}")
        import traceback
        traceback.print_exc()


def test_vispy_colormap_access():
    """Test direct vispy colormap access."""
    print("Testing vispy colormap access...")
    
    try:
        # Test vispy access
        lipari_vispy = qmricolors.get_colormap('lipari', backend='vispy')
        navia_vispy = qmricolors.get_colormap('navia', backend='vispy')
        print(f"VisPy - Lipari: {lipari_vispy}")
        print(f"VisPy - Navia: {navia_vispy}")
        
        print(f"Available colormaps: {qmricolors.AVAILABLE_CMAPS}")
        
    except ImportError as e:
        print(f"VisPy not available: {e}")
    except Exception as e:
        print(f"Error accessing VisPy colormaps: {e}")


if __name__ == "__main__":
    print("qMRI Colors - VisPy Example")
    print("============================")
    
    # Test colormap access
    test_vispy_colormap_access()
    
    # Create vispy example
    print("\nStarting VisPy example (requires GUI)...")
    vispy_example()
    
    print("\nVisPy example completed!")