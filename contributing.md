Coding Standards for Set game

This document outlines coding standards for use when collaborating on Set game.

This is a living document, and we encourage pull request and issues to improve on or contest the expressed ideas.


GENERAL OVERVIEW:

We use Python and Javascript (Node.js). If you plan to develop in another language please flag this and discuss.
Tests are required. Unit tests, as well as functional and integration tests. Aiming for test coverage of 80% and above is desirable.
Tests must be automated via a continuous integration platform that is triggered when code is pushed to the canonical repository.
Documentation is required for all code. Documentation is just as important as tests.
Document functions, classes, modules and packages with docstrings.

Provide a great README.md file with examples of how to use the code.
(Only use documentation builders like Sphinx for large projects; prefer README.md files for brevity and accessibility of documentation.)

Use ' and not " as the quote character by default
Space lines as needed for clarity and parsability.

Use clear and concise naming practices--

Use spaces and never tabs.
Javascript, HTML and CSS: 2 space indentation.
Python: 4 space indentation.
Strictly enforce a 79 character line limit.
Use common language conventions for naming functions, classes and variables (camelcase vs. snake-case when appropriate, capitalization when appropriate, etc.).
Code should be submitted via pull requests, which another person should merge.

Our work is done in Python and Javascript (Node.js). There can be good reasons for writing a particular library or app in another language, but if you think this is the case, please raise this issue directly before starting any work.


PYTHON:

Follow the Python Style Guide (PSG) as formulated in PEP-8: http://www.python.org/dev/peps/pep-0008/
The critical points are:

Use spaces; never use tabs
4 space indentation
79 character line limit
Variables, functions and methods should be lower_case_with_underscores
Classes are TitleCase
And other preferences:

Use ' and not " as the quote character by default
When writing a method, consider if it is really a method (needs self) or if it would be better as a utility function
When writing a @classmethod, consider if it really needs the class (needs cls) or it would be better as a utility function or factory class

Names to avoid:
Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use 'l', use 'L' instead.

Choose function names that are clear and verby (relevant to to what the function does), and choose variable names that are clear and concise of what they are representing.

Lists/Dictionaries/Sets/Tuples should be in this format:
[
    'item_1',
    'item_2',
    'item_3',
]
** NOTE: Trailing comma.

Comments:
Inline comments should be two spaces away from code start with # followed by a single space, then the comment, and should end with a period.
Standard comments should go directly above the code you are commenting on, start with a #, followed by a single space, then the comment, and should end with a period.

Space lines as needed for clarity and parsability of your code.

Docstrings:
single line docstrings example: 
    """ Brief clear comment here."""
multi line comment example: 
    """ Longer comment here. Longer comment here. Longer comment here. 
    Longer comment here. Longer comment here. Longer comment here.
    Longer comment here.
    """


Javascript

Using ES6

Use spaces; never use tabs
2 space indentation
79 character line limit
Variables, functions and methods should be camelCase
Classes are TitleCase


TESTING:

[TBD]


DOCUMENTATION:

Prefer to make really good README.md files, rather than implementing a full documentation framework.


BRANCH MANAGEMENT:
We generally follow Git Flow, with some modifications, and some flexibility per project. The following should hold true for pretty much all projects:

Have a master branch
Never commit directly to master
Always work from a feature/{} or a fix/{} branch that is checked out from master
Always reference issues from Git messages using #{issue_id}, and the various other related conventions used by most Git hosts.
Properly describe changes in commit messages: "Fixes database migration script failure on Python 2.7", not "Fix."
Continuous integration and deployment


URLs:

In general do not use trailing slash on urls (but ensure you redirect 301 from trailing slash to non-trailing slash)
e.g.: /work not /work/, /work/9 not /work/9/


FOR REFERENCE:
https://www.python.org/dev/peps/pep-0008/
http://docs.ckan.org/en/latest/contributing/python.html
