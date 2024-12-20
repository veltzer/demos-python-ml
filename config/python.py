config_requires = []
dev_requires = []
install_requires = [
    "scikit-learn",
    # "sklearn",
    "pyarrow",
    "pandas",
    "numpy",
    "matplotlib",
    # deep learining
    "tensorflow",
    "keras",
]
build_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires = [
]
requires = config_requires + install_requires + build_requires + test_requires
