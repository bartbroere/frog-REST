# frog-REST
Expose the FROG NLP model with a simple REST API

Simple Docker container for quickly finding named entities (organisations and persons for now)
in Dutch text using [Frog NLP](https://languagemachines.github.io/frog/).

Runs on port 5000

``docker run -p 5000:5000 -d bartbroere/frog-rest``

```
POST http://localhost:5000/process
POST http://localhost:5000/persons
POST http://localhost:5000/organisations
with the parameter document for each of these calls
```