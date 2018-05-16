# Run this script to remove folders and files produced from PyPI build, conda
# build, and pytest. Returns the project folder to a pre-build state.

echo "Remove PyPI build folders and files..."
rm -rf build/
rm -rf chemics.egg-info/
rm -rf dist/

echo "Remove Conda build folders and files..."
rm -rf recipe/chemics/

echo "Remove pytest cache folder..."
rm -rf .pytest_cache/

echo "Cleanup complete."
