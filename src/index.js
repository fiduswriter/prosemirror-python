import {Schema} from "prosemirror-model"
import {Step, Transform} from "prosemirror-transform"
import OrderedMap from "orderedmap"

export const create_doc = (doc_data, spec_data) => {
    const schemaSpec = {
        marks: new OrderedMap(spec_data.marks.content),
        nodes: new OrderedMap(spec_data.nodes.content)
    }
    const schema = new Schema(schemaSpec)
    const node = schema.nodeFromJSON(doc_data)
    return node
}

export const transform_doc = (steps_data, doc) => {
    const schema = doc.type.schema
    const steps = steps_data.map(s => Step.fromJSON(schema, s))
    const transform = new Transform(doc)
    steps.forEach(step => transform.step(step))
    return transform.doc
}
