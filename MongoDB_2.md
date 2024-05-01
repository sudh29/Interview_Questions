### In MongoDB, operators are used to perform various operations on data. MongoDB provides a rich set of operators that allow you to query, manipulate, and aggregate data in your collections. Here are some commonly used operators in MongoDB:

## Comparison Operators:

* $eq: Matches values that are equal to a specified value.
* $ne: Matches values that are not equal to a specified value.
* $gt: Matches values that are greater than a specified value.
* $lt: Matches values that are less than a specified value.
* $gte: Matches values that are greater than or equal to a specified value.
* $lte: Matches values that are less than or equal to a specified value.

### Find documents where the 'field' is not equal to 'value'
query = {'field': {'$ne': 'value'}}

result = collection.find(query)

## Logical Operators:

* $and: Joins query clauses with a logical AND.
* $or: Joins query clauses with a logical OR.
* $not: Inverts the effect of a query expression.
* $nor: Joins query clauses with a logical NOR.

### Find documents where both conditions are true
query = {'$and': [{'field1': 'value1'}, {'field2': 'value2'}]}

result = collection.find(query)


## Element Operators:

* $exists: Matches documents that have the specified field.
* $type: Selects documents if a field is of the specified type.

Array Operators:

* $in: Matches any of the values specified in an array.
* $nin: Matches none of the values specified in an array.
* $all: Matches arrays that contain all elements specified in the query.
* $elemMatch: Matches documents that contain an array field with at least one element matching the specified query.

### Find documents where the 'field' matches any value in the given list
query = {'field': {'$in': ['value1', 'value2']}}

result = collection.find(query)

## Evaluation Operators:

* $regex: Provides regular expression matching.
* $text: Performs a text search.
* $where: Matches documents that satisfy a JavaScript expression.

### Find documents where the 'field' exists
query = {'field': {'$exists': True}}
result = collection.find(query)


## Projection Operators:

* $project: Reshapes each document in the result set.
* $slice: Limits the number of elements in an array.
* $elemMatch: Filters the content of an array to return only the first element matching the specified condition.

## Update Operators

### Update a document by setting a value to a field
query = {'_id': ObjectId('document_id')}
update = {'$set': {'field': 'new_value'}}
collection.update_one(query, update)

### Increment the value of a field in a document
query = {'_id': ObjectId('document_id')}
update = {'$inc': {'field': 5}}
collection.update_one(query, update)



