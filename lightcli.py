#_MIT License
#_
#_Copyright (c) 2017 Dan Persons (dpersonsdev@gmail.com)
#_
#_Permission is hereby granted, free of charge, to any person obtaining a copy
#_of this software and associated documentation files (the "Software"), to deal
#_in the Software without restriction, including without limitation the rights
#_to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#_copies of the Software, and to permit persons to whom the Software is
#_furnished to do so, subject to the following conditions:
#_
#_The above copyright notice and this permission notice shall be included in all
#_copies or substantial portions of the Software.
#_
#_THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#_IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#_FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#_AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#_LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#_OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#_SOFTWARE.

# lightcli
# A lightweight terminal interaction library for Python.

__version__ = '0.2-alpha'



def get_input(options=[], prompt='Press ENTER to continue.', qopt=False):
    """Ask for input, and check its sanity. (q to quit)"""

    choice = None
    while not choice:
        try:
            choice = str(input(prompt + ' ' + str(options) + \
                    ' (q to quit) '))
        except SyntaxError:
            if options == []:
                pass
        if choice:
            if choice in options:
                return choice
            elif qopt == True and choice == 'q':
                choice = None
                is_sure = input('Are you sure you want to quit? ')
                if is_sure in ('Y', 'y', 'yes'):
                    exit('\nThanks for playing. Goodbye.\n')
            elif options == []:
                return 0
            else:
                print('Answer must be one of ' + str(options) +
                        '. Your answer?')
                if options:
                    choice = None
        elif options == []:
            return 0
        else:
            print('Answer must be one of ' + str(options) + 
                    '. Your answer?')
