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

```
from prosemirror import create_doc, transform_doc
```

First use `doc = create_doc(doc_data, schema_spec)` to create a Document object.

Then use `updated_doc = transform_doc(steps_data, doc)` to create a new Document object with the given steps applied.

Use `updated_doc.toJSON()` to get the JSON version of the updated document.
