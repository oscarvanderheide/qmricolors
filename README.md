# qMRI Colors

A Python package providing the recommended colormaps from [Fuderer et al. (2024)](https://pubmed.ncbi.nlm.nih.gov/39415361/) for quantitative MRI visualization. This package makes it easy to use the scientifically-optimized lipari and navia colormaps in both matplotlib and vispy, eliminating the need for manual colormap registration in each project.

The colormaps are based on the research presented in "Colormaps for quantitative magnetic resonance imaging" (Magnetic Resonance in Medicine, 2024) and are sourced from the [colorResources repository](https://github.com/mfuderer/colorResources).

**WARNING** At the moment this package does not comply with the recommendations because it's not adapting to the underlying image, see [https://magneticresonanceimaging.github.io/QMRIColors.jl/dev/clip/](https://magneticresonanceimaging.github.io/QMRIColors.jl/dev/clip/) for an explanation.


## Installation

Install the package directly from GitHub using uv (recommended) or pip:

```bash
# Using uv
uv add git+https://github.com/oscarvanderheide/qmricolors.git

# Using pip
pip install git+https://github.com/oscarvanderheide/qmricolors.git
```

For development:
```bash
git clone git@github.com:oscarvanderheide/qmricolors.git
cd qmricolors
uv sync

# Install in development mode to use examples
uv pip install -e .
```

## Usage

Simply import the package to automatically register the custom colormaps:

```python
import qmricolors
```

### Matplotlib Usage

```python
import matplotlib.pyplot as plt
import numpy as np
import qmricolors

# Create sample data
data = np.random.rand(100, 100)

# Use the custom colormaps
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(data, cmap='lipari')
plt.title('Lipari Colormap')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(data, cmap='navia')
plt.title('Navia Colormap')
plt.colorbar()

plt.show()
```

### VisPy Usage

```python
from vispy import app, scene
from vispy.color import get_colormap
import numpy as np
import qmricolors

# Create sample data
data = np.random.rand(100, 100)

# Get custom colormap
lipari_cmap = get_colormap('lipari')

# Create visualization
canvas = scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()
image = scene.visuals.Image(data, cmap=lipari_cmap, parent=view.scene)
view.camera = scene.PanZoomCamera(aspect=1)
view.camera.set_range()

app.run()
```

**Note**: If the VisPy window doesn't appear, this may be due to GUI backend issues. Try:
1. Installing a GUI backend: `pip install PyQt5` or `pip install PySide2`
2. On macOS, you may need to run Python from the terminal rather than an IDE
3. Use the simple test script: `python test_vispy_simple.py`

### Direct API Usage

```python
import qmricolors

# Get colormap for specific backend
lipari_mpl = qmricolors.get_colormap('lipari', backend='matplotlib')
navia_vispy = qmricolors.get_colormap('navia', backend='vispy')

# List available colormaps
print(qmricolors.AVAILABLE_CMAPS)  # ['lipari', 'navia']

# Register colormaps manually (if needed)
qmricolors.register_all_colormaps()
```

## Available Colormaps

- **lipari**: A scientifically-optimized colormap for quantitative MRI visualization
- **navia**: A scientifically-optimized colormap for quantitative MRI visualization

These colormaps were designed based on perceptual uniformity principles and extensive testing for quantitative medical imaging, as described in [Fuderer et al. (2024)](https://pubmed.ncbi.nlm.nih.gov/39415361/).

## Customizing Colormaps

To use your own colormap data, replace the CSV files in the package:

1. `qmricolors/lipari.csv`
2. `qmricolors/navia.csv`

The CSV format should contain space-separated RGB values (without headers), with values between 0 and 1:

```
0.011370 0.073240 0.148284
0.013965 0.079062 0.155370
0.015899 0.084718 0.162521
0.017234 0.090035 0.169728
...
```

Each line represents one color with three space-separated values for red, green, and blue components.

## Examples

The package includes several example scripts to demonstrate usage:

### General Example
Test basic colormap functionality:
```bash
uv run qmricolors/examples/example.py
```

### Matplotlib Example
See matplotlib-specific plotting examples:
```bash
uv run qmricolors/examples/matplotlib_example.py
```

### VisPy Example
Interactive 3D visualization with VisPy (requires GUI):
```bash
uv run qmricolors/examples/vispy_example.py
```

## Dependencies

- matplotlib >= 3.10.3
- vispy >= 0.15.2
- numpy >= 1.21.0

## References

- Fuderer, M., et al. (2024). Colormaps for quantitative magnetic resonance imaging. *Magnetic Resonance in Medicine*. https://pubmed.ncbi.nlm.nih.gov/39415361/
- Original colormap resources: https://github.com/mfuderer/colorResources

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
