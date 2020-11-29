import DS from 'ember-data';
const { Model, attr } = DS;

export default Model.extend({
    name: attr(),
    email: attr(),
    address: attr(),
    totalPrice: attr(),
    items: [],
});
