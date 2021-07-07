### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?  
RESTful routes follow the REST constraints for creating web services (Application Protocol Interfaces) to provide resources. REST stands for Representation State Transfer. RESTful routes follow the conventions which map the route's path to HTTP methods GET, POST, PUT, PATCH, and DELETE.

- What is a resource?  
A resource is the data transferred through RESTful APIs between client and server.

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
JSON APIs do not respond with HTML. They respond with JSON.

- What does idempotent mean? Which HTTP verbs are idempotent?  
Idempotent means the request can be performed repeatedly and each call will have the same result. GET, PUT, and DELETE are all idempotent. POST is not since repeated calls will each produce a new resource.

- What is the difference between PUT and PATCH?  
A PUT request updates (replaces) an entire resources while a PATCH request updates only a part of a resource.

- What is one way encryption?  
One way encryption means that the process of encrypting can't be reversed. For example, you can't find the original password given the hashed password.

- What is the purpose of a `salt` when hashing a password?  
A salt is a piece of random data added to a password before hashing it. The purpose is to make it more difficult to identify common passwords from a list of hashed passwords. The same password will also result in different hashed passwords when a salt is included.

- What is the purpose of the Bcrypt module?  
Bcrypt provides methods to generate hashed passwords and to authenticate given a hashed password.

- What is the difference between authorization and authentication?  
Authentication is validating that users are who they say they are. This can include asking the user for a password. Authorization is providing access to particular resources.
