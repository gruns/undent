# -*- coding: utf-8 -*-

#
# Undent - Intelligently dedent strings for output
#
# Ansgar Grunseid
# grunseid.com
# grunseid@gmail.com
#
# License: MIT
#

import os
from textwrap import dedent, fill

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


DEFAULT_WRAP_WIDTH = 70  # same as textwrap's default


def getIndentation(line):
    return line[0:len(line) - len(line.lstrip())]


def splitIntoParagraphs(s):
    """
    Split <s> into paragraphs and the number of newlines before each
    paragraph, so whitespace between paragraphs can be preserved. Ex:

      splitIntoParagraphs('''a

      b


      c''')

    return [(0, 'a'), (1, 'b'), (2, 'c')].
    """
    paragraphs = []

    paragraphLines = []
    numNewlinesBeforeParagraph = 0
    for line in s.splitlines():
        if not line.strip() and paragraphLines:  # end of current paragraph
            paragraph = os.linesep.join(paragraphLines)
            paragraphs.append((numNewlinesBeforeParagraph, paragraph))
            paragraphLines = []
            numNewlinesBeforeParagraph = 1
        elif not line.strip():  # another empty line before the next paragraph
            numNewlinesBeforeParagraph += 1
        elif (paragraphLines and # new paragraph with different indentation
                  getIndentation(line) != getIndentation(paragraphLines[-1])):
            paragraph = os.linesep.join(paragraphLines)
            paragraphs.append((numNewlinesBeforeParagraph, paragraph))
            paragraphLines = [line]
            numNewlinesBeforeParagraph = 0
        else:  # a new line in the current paragraph
            paragraphLines.append(line)

    if numNewlinesBeforeParagraph or paragraphLines:
        paragraph = os.linesep.join(paragraphLines)
        paragraphs.append((numNewlinesBeforeParagraph, paragraph))

    return paragraphs


def combineParagraphs(paragraphs):
    expanded = [(os.linesep * numNewlines) + p for numNewlines, p in paragraphs]
    return os.linesep.join(expanded)


def unwrap(paragraph):
    toks = [
        line.rstrip() if i == 0 else line.strip()
        for i, line in enumerate(lines)]
    unwrapped = ' '.join(toks).rstrip()
    return unwrapped


def lstripEmptyLines(s):
    """
    Only strip empty lines to preserve initial indentation. Ex

      lstripEmptyLines('''
      
      
        foo
      blah''')
    
    returns '  foo\nblah'.
    """
    lines = []
    for line in s.splitlines():
        if lines or line.strip():
            lines.append(line)

    s = os.linesep.join(lines)
    return s


def undent(s, wrap=False, strip=True):
    s = dedent(s)

    if strip:
        s = lstripEmptyLines(s)  # preserve indentation; only strip empty lines
        s = s.rstrip()

    if wrap is False:  # unwrap
        paragraphs = [
            (newlines, unwrap(p)) for newlines, p in splitIntoParagraphs(s)]
        s = combineParagraphs(paragraphs)
    elif wrap:
        width = DEFAULT_WRAP_WIDTH if wrap is True else wrap
        paragraphs = [
            (newlines, fill(p, width)) for newlines, p in splitIntoParagraphs(s)]
        s = combineParagraphs(paragraphs)

    return s
