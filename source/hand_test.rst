.. toctree::
   :caption: HELLO Nicolas

#########
HAND TEST
#########

SubPart1
########

********
CHAPTER1
********

SubChapter1
***********

what
    Definition lists associate a term with a definition.

how
    The term is a one-line phrase, and the definition is one
    or more paragraphs or body elements, indented relative to
    the term.

POUIC
=====

:what: Field lists map field names to field bodies, like
       database records.  They are often part of an extension
       syntax.

:how: The field marker is a colon, the field name, and a
      colon.

      The field body may contain one or more body elements,
      indented relative to the field marker.

Hello
-----

Literal blocks are either indented or line-prefix-quoted blocks,
and indicated with a double-colon ("::") at the end of the
preceding paragraph (right here -->)::

    if literal_block:
        text = 'is left as-is'
        spaces_and_linebreaks = 'are preserved'
        markup_processing = None

Hi
~~~

>>> print 'Python-specific usage examples; begun with ">>>"'
Python-specific usage examples; begun with ">>>"
>>> print '(cut and pasted from interactive Python sessions)'
(cut and pasted from interactive Python sessions)

  - idjqidjqoidjqw

    - dqwdjqoidjqwoidjqwoi

KKKKKK
------

jjjjj
~~~~~

********
CHAPTER2
********

SubChapter1
***********

CHLIKA
======

+------------------------+------------+----------+
| Header row, column 1   | Header 2   | Header 3 |
+========================+============+==========+
| body row 1, column 1   | column 2   | column 3 |
+------------------------+------------+----------+
| body row 2             | Cells may span        |
+------------------------+-----------------------+

====================  ==========  ==========
Header row, column 1  Header 2    Header 3
====================  ==========  ==========
body row 1, column 1  column 2    column 3
body row 2            Cells may span columns
====================  ======================

END
---

\- hello - hello
hello - hello
tout est
mis
dans une
meme ligne

saut // de
ligne

.. [1] A footnote contains body elements, consistently
   indented by at least 3 spaces.

END
---

    Hello1
        hello2
            hello3
                - hello41
                    dwdwd
                - hello42
                - hello43
                    dwwdwdw
            hello3 derechef
commentaire relou place ici
        hello2 derechef

END
---

Another top-level paragraph.

        This paragraph belongs to a second-level block quote.

    This paragraph belongs to a first-level block quote.  The
    second-level block quote above is inside this first-level
    block quote.

END
---

:emphasis:`emphasis`

:strong:`I'm strong !!`

:literal:`literally a chicken`

:subscript:`subscript text, what is it?`

:superscript:`Supermen do superscripts !`

:title-reference:`my little poney`

END
---

- This is the first line of a bullet list
  item's paragraph.  All lines must align
  relative to the first line.

      This indented paragraph is interpreted
      as a block quote.

  Another paragraph belonging to the first list item.

 Because it is not sufficiently indented,
 this paragraph does not belong to the list
 item (it's a block quote following the list).

:Hello: This field has a short field name, so aligning the field
        body with the first line is feasible.

:Number-of-African-swallows-required-to-carry-a-coconut: It would
    be very difficult to align the field body with the left edge
    of the first line.  It may even be preferable not to begin the
    body on the same line as the marker.