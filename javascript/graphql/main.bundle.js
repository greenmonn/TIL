"use strict";

var _graphql = require("graphql");

var schema = new _graphql.GraphQLSchema({
  query: new _graphql.GraphQLObjectType({
    name: 'RootQueryType',
    fields: {
      hello: {
        type: _graphql.GraphQLString,
        resolve: function resolve() {
          return 'world';
        }
      }
    }
  })
});
var query = '{ hello }';
var queryNotInSchema = '{ blahblah }';
(0, _graphql.graphql)(schema, query).then(function (result) {
  console.log(result);
});
(0, _graphql.graphql)(schema, queryNotInSchema).then(function (result) {
  console.log(result);
});
