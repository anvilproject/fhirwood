# fhirwood
FHIRwood provides some basic classes that can be used to consume or generate some key FHIR data types such as Coding, CodeableConcept and Range.

These were initially developed to simplify the tests for CMG FHIR ingest scripts, for which one of the resources required a lengthy set of components (an array of coding/value members). The goal here is to simplify parsing and evaluation of some common FHIR data types as well as to assist in generation of JSON output using python objects rather than rewriting JSON objects with minor differences. 

These objects should be able to be instantiated using reasonably named parameters as well as raw JSON "blocks". They must be flexible enough to support the variety of forms seen from real FHIR data. A key aspect is to easily perform comparisons, which must work even if the component actually represents an array, such as Identifiers and Codings.

