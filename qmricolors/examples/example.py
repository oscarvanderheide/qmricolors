#!/usr/bin/env python3
"""
Example usage of qMRI Colors package.

This script demonstrates how to use the custom colormaps with both matplotlib and vispy.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Add the parent directory to the path so we can import qmricolors
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Import qmricolors - this automatically registers the colormaps
import qmricolors

def matplotlib_example():
    """Demonstrate matplotlib usage."""
    print("Creating matplotlib example...")
    
    # Create some sample data
    x = np.linspace(0, 10, 100)
    y = np.linspace(0, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)
    
    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot with lipari colormap
    im1 = ax1.imshow(Z, cmap='lipari', aspect='auto')
    ax1.set_title('Lipari Colormap')
    plt.colorbar(im1, ax=ax1)
    
    # Plot with navia colormap
    im2 = ax2.imshow(Z, cmap='navia', aspect='auto')
    ax2.set_title('Navia Colormap')
    plt.colorbar(im2, ax=ax2)
    
    plt.tight_layout()
    plt.savefig('matplotlib_example.png', dpi=150, bbox_inches='tight')
    plt.show()


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


def test_colormap_access():
    """Test direct colormap access."""
    print("\nTesting colormap access...")
    
    # Test matplotlib access
    lipari_mpl = qmricolors.get_colormap('lipari', backend='matplotlib')
    navia_mpl = qmricolors.get_colormap('navia', backend='matplotlib')
    print(f"Matplotlib - Lipari: {lipari_mpl}")
    print(f"Matplotlib - Navia: {navia_mpl}")
    
    # Test vispy access
    lipari_vispy = qmricolors.get_colormap('lipari', backend='vispy')
    navia_vispy = qmricolors.get_colormap('navia', backend='vispy')
    print(f"VisPy - Lipari: {lipari_vispy}")
    print(f"VisPy - Navia: {navia_vispy}")
    
    print(f"Available colormaps: {qmricolors.AVAILABLE_CMAPS}")


if __name__ == "__main__":
    print("qMRI Colors Example")
    print("===================")
    
    # Test colormap access
    test_colormap_access()
    
    # Create matplotlib example
    # matplotlib_example()
    
    # Create vispy example (optional)
    print("\nWould you like to test the VisPy example? (requires GUI)")
    vispy_example()  # Uncomment to test VisPy
    
    print("\nExample completed!")