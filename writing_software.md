## Distributing a Python Package using PyPI

Once you've done the hard work of writing codes, tests and documentation, uploading to the Python Package Index (PyPI) for distribution is relatively straight forwards:
see the steps listed [here](https://packaging.python.org/tutorials/packaging-projects/). In summary:

1. Bump up the version number on your repo (and any asociated documentation).
2. Create a release on Github
3. Update the packages needed: `python3 -m pip install --upgrade build pip twine`
4. Build the distribution: `python3 -m build`
5. Upload to PyPI: `python3 -m twine upload dist/\*`
6. Test with a clean pip install in a new conda environment
