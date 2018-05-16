# Run this script to move Sphinx HTML files to the docs/ folder.

echo -e "\033[1mMove Sphinx html files to docs/ folder.\033[0m"

if [ ! -d "docs" ]; then
    echo "create docs/ folder"
    mkdir docs/
fi

shopt -s nullglob dotglob

files=(docs/*)

if [ ${#files[@]} -gt 0 ]; then
    echo "remove previous files in docs/"
    rm -R docs/*
fi

if [ ! -d "sphinx/_build/html" ]; then
    echo "no files in sphinx/_build/html/"
    echo "need to run Sphinx to generate html"
    exit 1
fi

echo "move html files from sphinx/_build/html/ to docs/"
mv sphinx/_build/html/* docs/

echo "add .nojekyll file in docs/"
touch docs/.nojekyll

echo "Done."