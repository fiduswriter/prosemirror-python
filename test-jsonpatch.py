#!/usr/bin/env python

import json
from jsonpatch import apply_patch

doc_data = json.loads('{"type":"article","attrs":{"papersize":"A4","citationstyle":"apa","documentstyle":"elephant","language":"en-US","tracked":false},"content":[{"type":"title","content":[{"type":"text","marks":[{"type":"insertion","attrs":{"user":1,"username":"johanneswilm","date":25710790,"approved":true}}],"text":"testing"}]},{"type":"subtitle","attrs":{"hidden":true}},{"type":"authors","attrs":{"hidden":true}},{"type":"abstract","attrs":{"hidden":true},"content":[{"type":"paragraph","attrs":{"track":[]}}]},{"type":"keywords","attrs":{"hidden":true}},{"type":"body","content":[{"type":"paragraph","attrs":{"track":[]},"content":[{"type":"text","marks":[{"type":"insertion","attrs":{"user":1,"username":"johanneswilm","date":25710790,"approved":true}}],"text":"the body"}]}]}]}')

diff_data = json.loads('[{"op":"replace","path":"/content/5/content/0/content/0/text","value":"the b"},{"op":"add","path":"/content/5/content/0/content/1","value":{"type":"text","marks":[{"type":"insertion","attrs":{"user":1,"username":"johanneswilm","date":25716230,"approved":true}}],"text":"X"}},{"op":"add","path":"/content/5/content/0/content/2","value":{"type":"text","marks":[{"type":"insertion","attrs":{"user":1,"username":"johanneswilm","date":25710790,"approved":true}}],"text":"ody"}}]')

import time
a = range(100)
start = time.time()

for i in a:
    apply_patch(
        doc_data,
        diff_data,
        False
    )

stop = time.time()

print((stop - start)/100)
