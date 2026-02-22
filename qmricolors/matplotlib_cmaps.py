"""
Matplotlib colormap registration for qMRI colormaps.
"""

from pathlib import Path
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap


def _load_colormap_data(filename):
    """Load colormap data from CSV file."""
    data_dir = Path(__file__).parent
    filepath = data_dir / filename

    colors = []
    with open(filepath, "r") as f:
        for line in f:
            # Skip empty lines
            line = line.strip()
            if not line:
                continue
            # Split the space-separated RGB values
            rgb_values = line.split()
            if len(rgb_values) == 3:
                colors.append(
                    [float(rgb_values[0]), float(rgb_values[1]), float(rgb_values[2])]
                )

    return colors


def _create_matplotlib_colormap(name, colors):
    """Create a matplotlib colormap from RGB color data."""
    cmap = LinearSegmentedColormap.from_list(name, colors, N=256)
    return cmap


def register_matplotlib_colormaps():
    """Register qMRI colormaps with matplotlib."""
    # Load colormap data
    lipari_colors = _load_colormap_data("lipari.csv")
    navia_colors = _load_colormap_data("navia.csv")

    # Create colormaps
    lipari_cmap = _create_matplotlib_colormap("lipari", lipari_colors)
    navia_cmap = _create_matplotlib_colormap("navia", navia_colors)

    # Register colormaps with matplotlib using the new API
    mpl.colormaps.register(lipari_cmap, name="lipari")
    mpl.colormaps.register(navia_cmap, name="navia")

    return {"lipari": lipari_cmap, "navia": navia_cmap}


def get_matplotlib_colormap(name):
    """Get a registered matplotlib colormap by name."""
    try:
        return mpl.colormaps[name]
    except KeyError:
        # If not registered, register all and try again
        register_matplotlib_colormaps()
        return mpl.colormaps[name]


# Available colormap names
MATPLOTLIB_CMAPS = ["lipari", "navia"]

