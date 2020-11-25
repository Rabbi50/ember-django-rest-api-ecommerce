import DS from 'ember-data';
const { Model, attr} = DS;

export default Model.extend({
    name: attr(),
    description: attr(),
    price: attr(),
    features: attr(),
    colors: attr()

});