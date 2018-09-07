import {
    graphql,
    GraphQLSchema,
    GraphQLObjectType,
    GraphQLString,
} from 'graphql';

const schema = new GraphQLSchema({
    query: new GraphQLObjectType({
        name: 'RootQueryType',
        fields: {
            hello: {
                type: GraphQLString,
                resolve() {
                    return 'world';
                }
            }
        }
    })
});

const query = '{ hello }';

const queryNotInSchema = '{ blahblah }';

graphql(schema, query).then(result => {
    console.log(result)
});

graphql(schema, queryNotInSchema).then(result => {
    console.log(result)
});