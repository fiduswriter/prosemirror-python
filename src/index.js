import {Schema} from "prosemirror-model"
import {Step} from "prosemirror-transform"
import OrderedMap from "orderedmap"

export const create_doc = (doc_data, spec_data) => {
    const schemaSpec = {
        marks: new OrderedMap(spec_data.marks.content),
        nodes: new OrderedMap(spec_data.nodes.content)
    }
    const schema = new Schema(schemaSpec)
    return schema.nodeFromJSON(doc_data)
}

export function transform_doc(steps_data, doc) => {
    let schema = doc.type.schema
    let step, s, i
    for (i=0; i < steps_data.length; i++) {
        s = steps_data[i]
        step = Step.fromJSON(schema, s)
        {doc} = step.apply(doc)
    }
    return doc
}

// For testing purposes: Let JS take care of JSON handling

export const create_doc_json = (doc_data_json, spec_data_json) => {
    const doc_data = JSON.parse(doc_data_json)
    const spec_data = JSON.parse(spec_data_json)
    const schemaSpec = {
        marks: new OrderedMap(spec_data.marks.content),
        nodes: new OrderedMap(spec_data.nodes.content)
    }
    const schema = new Schema(schemaSpec)
    return schema.nodeFromJSON(doc_data)
}

export const transform_doc_json = (steps_data_json, doc) => {
    const steps_data = JSON.parse(steps_data_json)
    const steps = steps_data.map(
        s => ({doc} = Step.fromJSON(doc.type.schema, s).apply(doc))
    )
    return doc
}
