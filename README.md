<table>
    <tr>
        <td>Method</td>
        <td>Endpoint</td>
        <td>Description</td>
        <td>Roles</td>
    </tr>
    <tr>
      
        <td>POST</td>
        <td>/api/v1/users</td>
        <td>create user account</td>
        <td>users</td>
    </tr>
    <tr>
     <td>GET</td>
        <td>/api/v1/users</td>
        <td>get all users</td>
        <td>admin</td>
    </tr>

    <tr>
     <td>GET</td>
        <td>/api/v1/users/<string: email></td>
        <td>get a specific user by email</td>
        <td>admin</td>
    </tr>
    <tr>
     <td>GET</td>
        <td>/api/v1/users/<string: username></td>
        <td>get a specific user by username</td>
        <td>admin</td>
    </tr>

     <tr>
     <td>GET</td>
        <td>/api/v1/users/<int: id></td>
        <td>get a specific user by id</td>
        <td>admin</td>
    </tr>

    <tr>
     <td>POST</td>
        <td>/api/v1/incidents</td>
        <td>create new incident</td>
        <td>users</td>
    </tr>
     <tr>
     <td>POST</td>
        <td>/api/v1/incidents</td>
        <td>create new incident</td>
        <td>users</td>
    </tr>

    <tr>
     <td>GET</td>
        <td>/api/v1/incidents</td>
        <td>get all incident</td>
        <td>admin</td>
    </tr>
    <tr>
     <td>GET</td>
        <td>/api/v1/incidents/<int: id></td>
        <td>get specific incident by id</td>
        <td>users</td>
    </tr>
    <tr>
     <td>PATCH</td>
        <td>/api/v1/incidents/<int: id></td>
        <td>change status of a specific incident by id</td>
        <td>admin</td>
    </tr>
    <tr>
     <td>PATCH</td>
        <td>/api/v1/incidents/<int: id></td>
        <td>edit a specific incident by id</td>
        <td>users</td>
    </tr>
    <tr>
     <td>DELETE</td>
        <td>/api/v1/incidents/<int: id></td>
        <td>delete a specific incident by id</td>
        <td>users</td>
    </tr>

</table>
