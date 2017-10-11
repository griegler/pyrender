# PyRender

This project contains a Cython version of [librender by Andreas Geiger and Chaohui Wang 2014](http://www.cvlibs.net/software/librender/).
The code enables the efficient rendering of depth maps from 3D triangle meshes.

To use the code, first compile the Cython code via 

```bash
python setup.py build-ext --inplace
```

You can then use the rendering function

```python
import pyrender
...
# vertices: a 3xN double numpy array
# faces: a 3xN double array (indices of vertices array)
# cam_intr: (fx, fy, px, py) double vector
# img_size: (width, height) int vector
depth, mask, img = pyrender.render(vertices, faces, cam_intr, img_size)
```

Make sure `pyrender` is in your `$PYTHONPATH`.
