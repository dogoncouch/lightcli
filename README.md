# lightcli
A lightweight terminal interaction library for Python.

# Installing
See the latest instructions on the [releases page](https://github.com/dogoncouch/lightcli/releases).

# Functions
    import lightcli
    
    choice = lightcli.get_input([options=<options>], [prompt=<prompt>], [qopt={True|False}])


Prompts for and returns input. `` options `` is the list of acceptable answers (a list of strings). `` prompt `` is the text shown when asking for input (a string). `` qopt `` toggles a 'q to quit' option (True/False: default is False).

    multiline = lightcli.long_input([prompt=<prompt>])

Gets a multi-line string as input. Entering an EOF (ctrl-D in \*nix, ctrl-Z in Windows) on a blank line ends the input.

# Copyright
MIT License

Copyright (c) 2017 Dan Persons (dpersonsdev@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

