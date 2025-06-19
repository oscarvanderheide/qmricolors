#!/usr/bin/env python3
"""
General example for qMRI Colors package.

This script demonstrates basic usage of the qMRI Colors package.
For specific examples, see:
- matplotlib_example.py: matplotlib-specific examples
- vispy_example.py: VisPy-specific examples
"""

import sys
import os

# Add the parent directory to the path so we can import qmricolors
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Import qmricolors - this automatically registers the colormaps
import qmricolors


def test_colormap_access():
    """Test direct colormap access."""
    print("Testing colormap access...")
    
    # Test matplotlib access
    lipari_mpl = qmricolors.get_colormap('lipari', backend='matplotlib')
    navia_mpl = qmricolors.get_colormap('navia', backend='matplotlib')
    print(f"Matplotlib - Lipari: {lipari_mpl}")
    print(f"Matplotlib - Navia: {navia_mpl}")
    
    # Test vispy access
    try:
        lipari_vispy = qmricolors.get_colormap('lipari', backend='vispy')
        navia_vispy = qmricolors.get_colormap('navia', backend='vispy')
        print(f"VisPy - Lipari: {lipari_vispy}")
        print(f"VisPy - Navia: {navia_vispy}")
    except ImportError:
        print("VisPy not available for testing")
    
    print(f"Available colormaps: {qmricolors.AVAILABLE_CMAPS}")


if __name__ == "__main__":
    print("qMRI Colors - General Example")
    print("=============================")
    
    # Test colormap access
    test_colormap_access()
    
    print("\nFor detailed examples, run:")
    print("- python qmricolors/examples/matplotlib_example.py")
    print("- python qmricolors/examples/vispy_example.py")
    
    print("\nGeneral example completed!")