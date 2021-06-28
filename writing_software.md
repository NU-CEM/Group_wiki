## Which language should I programme in?

For computational materials science I'd recommend using either Python or Julia. For those new to programming I'd recommend Python. Why? It's very widely used (lots of existing packages and extensive documentation), it's open source (you won't get tied into expensive licenses) and it's a readable language with a friendly learning curve (you can usually do quite a lot, quite quickly with not too much pain).

## What should my programming environment look like?

There are a few options. Some people like to develop code using an interactive notebook such as the [Jupyter Notebook](). Some like to develop in a basic text editor such as [Sublime](). Some like to use a more fully featured programming environment like [Pycharm](). Personally, I tend to use all three, depending on the size of the project and the writing stage I'm at - for early code development I nearly always use a Jupyter Notebook for quick feedback on my innumerable silly mistakes.

However you decide to write code I *highly recommend* you use a package manager such as [conda](). Python software packages are built like a tower of cards. Each package is built on (imports) other Python packages. These underlying packages will slowly morph and change over time. It's important to keep track of the exact version numbers used, and you may require different versions of the same code on your system at any given time (for example package_A may require package_X v1, whilst package_B might require package_X v2). In the perfect world, we'd all maintain our packages for perfect compatability but this isn't the perfect world - it's a potentially very messy world so learn how to keep things nice, tidy and reproducibble with Conda environments.

## I'm all setup. How do I..err...learn how to code....

I recommend three things
1. For the very basics (python types, for loops, functions etc...), complete one of the many Python tutorials out there
2. To put this into practice and *actually* learn, find a suitable project question and start trying to code. For example, you may want to read in some experimental data and plot it. Or you may want to write a solver for heat diffusion from some weird shaped object. If you are one of my students, feel free to ask me for project suggestions. Ideally it should be something useful, as that will keep you going when you hit a brick wall.
3. Find some code you like, and study it. I have a few people who I know code nicely (including Ben Morgan and Adam Jackson). I can read their code for inspiration, adapting little tips and tricks they use for my own work. 

## I've got a code that works!

Great! That's the first step complete. 

## Documentation

## Testing

## Packaging and sharing

## Distributing a Python Package using PyPI

Once you've done the hard work of writing codes, tests and documentation, uploading to the Python Package Index (PyPI) for distribution is relatively straight forwards:
see the steps listed [here](https://packaging.python.org/tutorials/packaging-projects/). In summary:

1. Bump up the version number on your repo (and any asociated documentation).
2. Create a release on Github
3. Update the packages needed: `python3 -m pip install --upgrade build pip twine`
4. Build the distribution: `python3 -m build`
5. Upload to PyPI: `python3 -m twine upload dist/\*`
6. Test with a clean pip install in a new conda environment
