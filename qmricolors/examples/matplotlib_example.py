#!/usr/bin/env python3
"""
Matplotlib example for qMRI Colors package.

This script demonstrates how to use the custom colormaps with matplotlib.
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
    plt.show()


def test_matplotlib_colormap_access():
    """Test direct matplotlib colormap access."""
    print("Testing matplotlib colormap access...")
    
    # Test matplotlib access
    lipari_mpl = qmricolors.get_colormap('lipari', backend='matplotlib')
    navia_mpl = qmricolors.get_colormap('navia', backend='matplotlib')
    print(f"Matplotlib - Lipari: {lipari_mpl}")
    print(f"Matplotlib - Navia: {navia_mpl}")
    
    print(f"Available colormaps: {qmricolors.AVAILABLE_CMAPS}")


if __name__ == "__main__":
    print("qMRI Colors - Matplotlib Example")
    print("=================================")
    
    # Test colormap access
    test_matplotlib_colormap_access()
    
    # Create matplotlib example
    matplotlib_example()
    
    print("\nMatplotlib example completed!")