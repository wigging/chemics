# Run this script to remove folders and files produced from PyPI build, conda
# build, and pytest. Returns the project folder to a pre-build state.

echo "Removing PyPI build folders and files..."
rm -rf build/
rm -rf dist/
rm -rf mytestpackage.egg-info/

echo "Removing Conda build folders and files..."
rm -rf noarch/
rm -rf osx-64/

echo "Removing pytest cache folder..."
rm -rf .cache/

echo "Cleanup complete."

