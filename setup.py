from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np
import platform

extra_compile_args = []
extra_link_args = ['-lGLEW', '-lglut']

if platform.system() == 'Darwin':
  extra_link_args.append('-framework OpenGL')
  extra_link_args.append('-framework GLU')
else:
  extra_link_args.append('-lGL')
  extra_link_args.append('-lGLU')

setup(
  name="pyrender",
  cmdclass= {'build_ext': build_ext},
  ext_modules=[
    Extension('pyrender',
      ['pyrender.pyx',
       'offscreen.cpp',
      ],
      language='c++',
      include_dirs=[np.get_include(),],
      extra_compile_args=extra_compile_args,
      extra_link_args=extra_link_args
    )
  ]
)


