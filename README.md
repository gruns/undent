<div align="center">
  <img src="logo.svg" width="300px" height="200px" alt="Undent">
</div>


# Undent

Undent turns multiline strings in source code (which are indented, have
inserted newlines, etc) into their intended, beautiful, human-readable
strings.

To do this, `undent()`

  1. [Dedents](https://docs.python.org/3/library/textwrap.html#textwrap.dedent)
     the string so common indentation added for source code formatting
     isn't unintentionally preserved.

  2. Strips preceeding and trailing whitespace, while preserving
     post-dedent indentation, so whitespace added for source code
     formatting isn't unintentionally preserved.

  3. Unwraps paragraphs so newlines inserted for source code formatting
     aren't unintentionally preserved in the output, e.g. newlines
     inserted to avoid lines wider than PEP 8's 80 characters per line.

     Or, optionally line wrap output paragraphs to your intended width,
     e.g. 72 character per line.


### Usage

Just import `undent()` and give it a string.

```python
>>> from undent import undent
>>> undent('''
    indented!
  not intended!''')

'''  indented!
not intended!'''
```

that's it! `undent()` returns a beautiful, human-readable string.

`undent(s, wrap=False, strip=True)` takes two, optional arguments.

#### wrap

(default: `False`) `wrap` is the maximum length of wrapped lines, in
characters, or `False` to unwrap lines. If `wrap` is an integer, as long
as there are no individual words in the input string longer than `wrap`,
no output line will be wider than `wrap` characters. Examples:

```python
undent('Once upon a time, there was a little girl named Goldilocks.', wrap=30)
```

returns

```
Once upon a time, there was a
little girl named Goldilocks.
```

Conversely,

```python
undent('''Once upon a time, there was a
little girl named Goldilocks.''', wrap=False)
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


### Example Behavior

> 1. [Dedents](https://docs.python.org/3/library/textwrap.html#textwrap.dedent)
>    the string so indentation added for source code formatting isn't
>    preserved.

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

> 2. Strips preceeding and trailing whitespace, while preserving
>    post-dedent indentation, so whitespace added for source code
>    formatting isn't unintentionally preserved.

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

> 3. Unwraps paragraphs so newlines inserted for source code formatting
>    aren't unintentionally preserved in the output, e.g. newlines
>    inserted to avoid lines wider than PEP 8's 80 characters per line.

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

> Or, optionally line wrap output paragraphs to your intended width,
> e.g. 72 character per line.

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
            ''', 72))
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