# qMRI Colors

A Python package providing custom colormaps (lipari and navia) for quantitative MRI visualization in both matplotlib and vispy.

## Installation

Install the package using uv (recommended) or pip:

```bash
# Using uv
uv add qmricolors

# Using pip
pip install qmricolors
```

For development:
```bash
git clone <repository-url>
cd qmricolors
uv sync
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

- **lipari**: A blue-to-white colormap suitable for quantitative MRI visualization
- **navia**: A red-to-white colormap suitable for quantitative MRI visualization

## Customizing Colormaps

To use your own colormap data, replace the CSV files in the package:

1. `qmricolors/lipari.csv`
2. `qmricolors/navia.csv`

The CSV format should have columns `r`, `g`, `b` with values between 0 and 1:

```csv
r,g,b
0.0,0.0,0.2
0.0,0.1,0.4
0.0,0.2,0.6
...
```

## Example

Run the included example script to see the colormaps in action:

```bash
python example.py
```

## Dependencies

- matplotlib >= 3.10.3
- vispy >= 0.15.2
- numpy >= 1.21.0

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]