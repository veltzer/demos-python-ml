import config.project

package_name = config.project.project_name

dev_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
install_requires = [
    "sklearn",
    "pandas",
    "numpy",
    "matplotlib",
]

python_requires = ">=3.10"

test_os = ["ubuntu-22.04"]
test_python = ["3.10"]
