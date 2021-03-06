=====
Prosemirror-python
=====

This is an unofficial and not production ready package. Contributions and improvements are welcome.

This package does not attempt at importing all of Prosemirror in Python. It is merely trying to use those parts of
prosemirror-model and prosemirror-transform that are needed for serverside operations.


**This package has not yet been extensively tested!**

How to use it
-----------

1. Install with `pip install prosemirror`

2. In your python code, import the two included functions with:


    from prosemirror import create_doc, transform_doc

3. Then create a Document object:

    doc = create_doc(doc_data, spec_data) # spec_data = JSON.parse(JSON.stringify(view.state.schema.spec))


4. Thereafter create an updated Document object with the given steps applied:

    updated_doc = transform_doc(steps_data, doc)

5. To get the JSON version of a Document object, simply use the builtin toJSON method:

    updated_doc.toJSON()


Speed
-----------

It is not setting any speed records so far. These tests were conducted with Python 2 with the test files in the repo (applying three steps to an existing doc):

    prosemirror-python: 0.024s
    
    nodejs: 0.00013s
    
    jsonpatch (Python): 0.00024s

So it is around 200 times slower than nodejs and 100 times slower than using jsonpatch. It is possible that it could be sped up in various ways, for example by using pypy and a vm or alike. Please let me know if you figure something out!

License questions
-----------

**Q - What license is this under?**

A - AGPL-3, check the LICENSE file.


**Q - I have spent the past month building a webbased text editing app. I am in stealth
mode as my editor is really unique and I'll be the next IT Billionaire once I
release it. Now I would like to use this library, but the AGPL requires me to share
changes I make with others! It's not fair that you are standing between me and my fortune!**

A - Right. If it is worth that much to you, you can try to pay me so that I'll put it under
a more liberal license. Secondly, you could suggest taking over maintainership of this
library and promise extra features to get me to change my mind. Thirdly - you could just
start from scratch as long as it's not much code, but then we both lose out of any fixes
either one of us makes.

We all need to live of something, I give a lot of code away for free
and the only requirement there is is that you contribute any changes you make back. Not
that expensive, if you think about it.
