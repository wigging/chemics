echo -e "\033[1mMove Sphinx html files to docs folder.\033[0m"

if [ ! -d "docs" ]; then
    echo "create docs folder"
    mkdir docs/
fi

shopt -s nullglob dotglob

files=(docs/*)

if [ ${#files[@]} -gt 0 ]; then
    echo "remove previous files in docs folder"
    rm -R docs/*
fi

if [ ! -d "sphinx/_build/html" ]; then
    echo "no files in sphinx/build/html"
    echo "run Sphinx to generate html"
    exit 1
fi

echo "copy html files to docs folder"
cp -R sphinx/_build/html/* docs/

echo "done"