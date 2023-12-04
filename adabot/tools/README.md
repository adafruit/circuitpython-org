
# Adabot Tools and Scripts


#### library_functions.py

Functions and typing protocols used for working with bundle libraries.
Pairs with functionality in `iterate_libraries.py` to create functions
for working with the Adafruit CircuitPython Bundle.


#### iterate_libraries.py

Function for looping through the libraries in the bundle.  There is a
function for iterating through a cloned bundle ("local") and another
for iterating through the bundle libraries on GitHun ("remote"). These
functions allow for a single function (see `library_functions.py`) to
act upon all libraries/repositories.


#### git_functionality.py

Provides basic git functionality such as syncing libraries and pushing
changes to the remote when working with a cloned library.  In particular,
it defines decorators that can be used with functions described by
`library_functions.LocalLibFunc`.


#### ci_status.py

Provides functionality for checking the GitHub Actions status of bundle
libraries.  Note that a GitHub token with the proper scope must be given
(the one needed for working with adabot should be enough).


#### docs_status.py

Provides functionality for checking the ReadTheDocs build status of
bundle libraries.  Note that both a Github and ReadTheDocs token must be
given (the GitHub token used by adabot should be enough, but a token
from adabot's account on ReadTheDocs will be needed).


#### find_text.py

Script to check for text across CircuitPython repos.

Type:
`python3 find_text.py -h`
to figure out how to use it.


#### runner.py

Script to run specific CircuitPython library validators one at a time.

Must be run from top-level directory (i.e. one up from this one).

Run with:
`python3 runner.py`
and then type in the number you want to run.


#### file_compare.py

Functionality to compare a file across all Adafruit CircuitPython repos
and output the text of the files along with which and how many repos use that
exact file text.
