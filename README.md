|Method|Endpoint|Description|Roles|
|POST|/api/v1/incidents|users can be able to create new incidents|users|
|POST|/api/v1/users|users can create new accounts|users|
|GET|/api/v1/users|admin can get all users|admin|
|GET|/api/v1/incidents|get all incidents|admin|
|GET|/api/v1/incidents/<int: id>|get specific incident|admin|
|GET|/api/v1/incidents/<int: id>|get specific incident|users|
|GET|/api/v1/users/<int: id>|get specific user by id|admin|
|GET|/api/v1/users/<string: username>|get specific user by username|admin|
|GET|/api/v1/users/<int: id>|get specific user by email|admin|
|PUT|/api/v1/incidents/<int: id>|edit specific incident| users|
|PUT|/api/v1/incidents/<int: id>|change status of specific incident|
