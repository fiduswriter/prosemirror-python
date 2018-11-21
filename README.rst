=====
Prosemirror-python
=====

This is an unofficial and not production ready package. Contributions and improvements are welcome.

This package does not attempt at importing all of Prosemirror in Python. It is merely trying to use those parts of
prosemirror-model and prosemirror-transform that are needed for serverside operations.


**This package has not yet been tested!**

How to use
-----------

1. Install with `pip install prosemirror`

2. In your python code, import the two included functions with:


    from prosemirror import create_doc, transform_doc

Then create a Document object:

    doc = create_doc(doc_data, schema_spec)


Thereafter create an updated Document object with the given steps applied:

    updated_doc = transform_doc(steps_data, doc)

To get the JSON version of a Document object, simply use the builtin toJSON method:

    updated_doc.toJSON()

