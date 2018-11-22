import {Schema} from "prosemirror-model"
import {Step, Transform} from "prosemirror-transform"

export const create_doc = (doc_data, schema_spec) => {
    const schema = new Schema(schema_spec)
    return schema.nodeFromJSON(doc_data)
}

export const transform_doc = (steps_data, doc) => {
    const schema = doc.type.schema
    const steps = steps_data.map(s => Step.fromJSON(schema, s))
    const transform = new Transform(doc)
    steps.forEach(step => transform.step(step))
    return transform.doc
}
