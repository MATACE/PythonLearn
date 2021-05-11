if [ "$1"x = "r"x ]
then
    python main.py
elif [ "$1"x = "c"x ]
then
    python clear.py
elif [ "$1"x = "b"x ]
then
    python setup.py sdist
elif [ "$1"x = "rm"x ]
then
    rm -rf dist package_demo.egg-info
fi