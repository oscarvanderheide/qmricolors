"""
qMRI Colors - Custom colormaps for quantitative MRI visualization.

This package provides lipari and navia colormaps for both matplotlib and vispy.
Simply import this package to automatically register the colormaps.

Usage:
    import qmricolors

    # Use in matplotlib
    import matplotlib.pyplot as plt
    plt.imshow(data, cmap='lipari')

    # Use in vispy
    from vispy.color import get_colormap
    cmap = get_colormap('navia')
"""

from .matplotlib_cmaps import (
    register_matplotlib_colormaps,
    get_matplotlib_colormap,
    MATPLOTLIB_CMAPS,
)
from .vispy_cmaps import (
    register_vispy_colormaps,
    get_vispy_colormap,
    list_vispy_colormaps,
    VISPY_CMAPS,
)

__version__ = "0.1.2"
__all__ = [
    "register_matplotlib_colormaps",
    "register_vispy_colormaps",
    "get_matplotlib_colormap",
    "get_vispy_colormap",
    "list_vispy_colormaps",
    "MATPLOTLIB_CMAPS",
    "VISPY_CMAPS",
    "AVAILABLE_CMAPS",
]

# Available colormap names
AVAILABLE_CMAPS = ["lipari", "navia"]


def register_all_colormaps():
    """Register all qMRI colormaps with both matplotlib and vispy."""
    matplotlib_cmaps = register_matplotlib_colormaps()
    vispy_cmaps = register_vispy_colormaps()
    return {"matplotlib": matplotlib_cmaps, "vispy": vispy_cmaps}


def get_colormap(name, backend="matplotlib"):
    """
    Get a colormap by name for the specified backend.

    Parameters
    ----------
    name : str
        Name of the colormap ('lipari' or 'navia')
    backend : str, optional
        Backend to use ('matplotlib' or 'vispy'), default 'matplotlib'

    Returns
    -------
    colormap
        The requested colormap object
    """
    if backend == "matplotlib":
        return get_matplotlib_colormap(name)
    elif backend == "vispy":
        return get_vispy_colormap(name)
    else:
        raise ValueError(f"Unknown backend: {backend}. Use 'matplotlib' or 'vispy'.")


# Automatically register colormaps when the package is imported
try:
    _registered_cmaps = register_all_colormaps()
    # print(f"qMRI Colors: Registered {len(AVAILABLE_CMAPS)} colormaps: {', '.join(AVAILABLE_CMAPS)}")
except Exception as e:
    print(f"qMRI Colors: Warning - Could not register all colormaps: {e}")
    _registered_cmaps = None
