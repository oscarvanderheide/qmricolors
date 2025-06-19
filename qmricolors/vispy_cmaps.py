"""
VisPy colormap registration for qMRI colormaps.
"""
import csv
import numpy as np
from pathlib import Path
from vispy.color import Colormap
from vispy.color.colormap import _colormaps


def _load_colormap_data(filename):
    """Load colormap data from CSV file."""
    data_dir = Path(__file__).parent
    filepath = data_dir / filename
    
    colors = []
    with open(filepath, 'r') as f:
        for line in f:
            # Skip empty lines
            line = line.strip()
            if not line:
                continue
            # Split the space-separated RGB values
            rgb_values = line.split()
            if len(rgb_values) == 3:
                colors.append([float(rgb_values[0]), float(rgb_values[1]), float(rgb_values[2])])
    
    return np.array(colors)


def _create_vispy_colormap(name, colors):
    """Create a VisPy colormap from RGB color data."""
    # VisPy expects colors as numpy array with shape (N, 3) or (N, 4)
    if colors.shape[1] == 3:
        # Add alpha channel if not present
        alpha = np.ones((colors.shape[0], 1))
        colors = np.hstack([colors, alpha])
    
    cmap = Colormap(colors)
    # Set the name manually after creation
    cmap.name = name
    return cmap


def register_vispy_colormaps():
    """Register qMRI colormaps with VisPy."""
    # Load colormap data
    lipari_colors = _load_colormap_data('lipari.csv')
    navia_colors = _load_colormap_data('navia.csv')
    
    # Create colormaps
    lipari_cmap = _create_vispy_colormap('lipari', lipari_colors)
    navia_cmap = _create_vispy_colormap('navia', navia_colors)
    
    # Register colormaps with VisPy
    _colormaps['lipari'] = lipari_cmap
    _colormaps['navia'] = navia_cmap
    
    return {'lipari': lipari_cmap, 'navia': navia_cmap}


def get_vispy_colormap(name):
    """Get a registered VisPy colormap by name."""
    if name in _colormaps:
        return _colormaps[name]
    else:
        # If not registered, register all and try again
        register_vispy_colormaps()
        return _colormaps.get(name, None)


def list_vispy_colormaps():
    """List all available VisPy colormaps including qMRI ones."""
    # Make sure our colormaps are registered
    register_vispy_colormaps()
    return list(_colormaps.keys())


# Available colormap names
VISPY_CMAPS = ['lipari', 'navia']