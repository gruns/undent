<div align="center">
  <img src="logo.svg" width="300px" height="200px" alt="Undent">
</div>


# Undent

Undent turns source code strings into their intended human-readable
strings.

Strings in source code may be indented, bookended with whitespace, or
contain newlines to adhere to code style guidelines. `undent()`
gracefully removes such code style formatting and returns a string the
original, intended string for human consumption.

To accomplish this, `undent()`

  1. [Dedents](https://docs.python.org/3/library/textwrap.html#textwrap.dedent)
     the multiline string to remove common indentation.

  2. Strips preceeding and trailing whitespace, while preserving
     post-dedent indentation, to remove whitespace added for source code
     formatting.

  3. Unwraps paragraphs to remove newlines inserted for source code
     formatting. E.g. newlines inserted to adhere to PEP 8's 79
     characters per line limit.

     Or, optionally line wrap paragraphs to a custom width, e.g. 72
     character per line.


### Usage

Just import `undent()` and give it a multiline string.

```python
from undent import undent

def createEmail():
    name = 'Billy'
    emailAddr = 'billy@gmail.com'
    email = undent(f'''
        Hi {name}!

        Thank you for registering with email address

          {emailAddr}

        We'd love to hear from you; please email us
        and say hello!''')

   return email
```

Above, `undent()` dedents, formats, and wraps the multiline string into
a beautiful, human-readable string.

```
Hi Billy!

Thank you for registering with email address

  billy@gmail.com.

We'd love to hear from you; please email us and say hello!
```

`undent(s, width=False, strip=True)` takes two, optional arguments.

#### width

(default: `False`) `width` is the maximum length of wrapped lines, in
characters, or `False` to unwrap lines. If `width` is an integer, as
long as there are no individual words in the input string longer than
`width`, no output line will be wider than `width` characters. Examples:

```python
undent('Once upon a time, there was a little girl named Goldilocks.', width=30)
```

returns

```
Once upon a time, there was a
little girl named Goldilocks.
```

Conversely,

```python
undent('''Once upon a time, there was a
little girl named Goldilocks.''', width=False)
```

returns

```
Once upon a time, there was a little girl named Goldilocks.
```

#### strip

(default: `True`) `strip` determines whether or not to remove preceeding
and trailing whitespace. Examples:

```python
undent('''
    Once upon a time, there was a
    little girl named Goldilocks.
    ''', strip=True)
```

returns

```
Once upon a time, there was a little girl named Goldilocks.
````

Alternatively

```python
undent('''

    Once upon a time, there was a
    little girl named Goldilocks.

    ''', strip=False)
```

returns

```


Once upon a time, there was a little girl named Goldilocks.


```


### Examples

#### `undent()` [dedents](https://docs.python.org/3/library/textwrap.html#textwrap.dedent) the string so indentation added for source code formatting isn't preserved.

```python
if True:
    print(undent('''common

    indentation

is removed'''))
```

outputs

```
common

    indentation

is removed
```

#### `undent()` strips preceeding and trailing whitespace, while preserving post-dedent indentation, so whitespace added for source code formatting isn't unintentionally preserved.

```python
if True:
    print(undent('''
        preceeding

            and trailing

        whitespace is removed
    '''))
```

outputs

```
preceeding

    and trailing

whitespace is removed
```

#### `undent()` unwraps paragraphs so newlines inserted for source code formatting aren't unintentionally preserved in the output, e.g. newlines inserted to avoid lines wider than PEP 8's 80 characters per line.

```python
if someIndentation:
    if moreIndentation:
        if evenDeeperIndentation:
            print(undent(f'''
                Once upon a time, there was a little girl named
                Goldilocks. She went for a walk in the forest. Pretty
                soon, she came upon a house. She knocked and, when no
                one answered, she walked right in.
            
                At the table in the kitchen, there were three bowls of
                porridge. Goldilocks was hungry. She tasted the porridge
                from the first bowl.
            '''))
```

outputs

```
Once upon a time, there was a little girl named Goldilocks. She went for a walk in the forest. Pretty soon, she came upon a house. She knocked and, when no one answered, she walked right in.

At the table in the kitchen, there were three bowls of porridge. Goldilocks was hungry. She tasted the porridge from the first bowl.
```

#### Or, optionally line wrap output paragraphs to your intended width, e.g. 72 character per line.

```python
if someIndentation:
    if moreIndentation:
        if evenDeeperIndentation:
            width = 72
            print(undent(f'''
                Once upon a time, there was a little girl named
                Goldilocks. She went for a walk in the forest. Pretty
                soon, she came upon a house. She knocked and, when no
                one answered, she walked right in.
            
                At the table in the kitchen, there were three bowls of
                porridge. Goldilocks was hungry. She tasted the porridge
                from the first bowl.
            ''', width))
```

outputs

```
Once upon a time, there was a little girl named Goldilocks. She went for
a walk in the forest. Pretty soon, she came upon a house. She knocked
and, when no one answered, she walked right in.

At the table in the kitchen, there were three bowls of porridge.
Goldilocks was hungry. She tasted the porridge from the first bowl.
```


### Installation

Installing Undent with pip is easy.

```
$ pip install undent
```