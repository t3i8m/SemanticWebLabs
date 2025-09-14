from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD

g = Graph()

SCHEMA = Namespace("https://schema.org/")
EX = Namespace("http://semanticweb2025.group5/vinted/")  

g.bind("schema", SCHEMA)
g.bind("ex", EX)
g.bind("rdfs", RDFS)
g.bind("xsd", XSD)

g.add((SCHEMA.Product, RDF.type, RDFS.Class))
g.add((SCHEMA.Brand, RDF.type, RDFS.Class))
g.add((EX.Category, RDF.type, RDFS.Class))

g.add((EX.Women,RDF.type, RDFS.Class))
g.add((EX.Women,RDFS.subClassOf, EX.Category))

g.add((EX.Men,RDF.type, RDFS.Class))
g.add((EX.Men,RDFS.subClassOf, EX.Category))

g.add((EX.Kids,RDF.type, RDFS.Class))
g.add((EX.Kids,RDFS.subClassOf, EX.Category))

g.add((EX.Home,RDF.type, RDFS.Class))
g.add((EX.Home,RDFS.subClassOf, EX.Category))

g.add((EX.Entertainment, RDF.type, RDFS.Class))
g.add((EX.Entertainment, RDFS.subClassOf, EX.Category))

g.add((EX.Clothing, RDF.type, RDFS.Class))
g.add((EX.Clothing, RDFS.subClassOf, EX.Women))

g.add((EX.Shoes,RDF.type, RDFS.Class))
g.add((EX.Shoes,RDFS.subClassOf, EX.Women))

g.add((EX.Bags,RDF.type, RDFS.Class))
g.add((EX.Bags,RDFS.subClassOf, EX.Women))

g.add((EX.Grooming, RDF.type, RDFS.Class))
g.add((EX.Grooming, RDFS.subClassOf, EX.Men))

g.add((EX.Accessories, RDF.type, RDFS.Class))
g.add((EX.Accessories, RDFS.subClassOf, EX.Men))

g.add((EX.SmallKitchenAppliances, RDF.type, RDFS.Class))
g.add((EX.SmallKitchenAppliances, RDFS.subClassOf, EX.Home))

g.add((EX.CookwareBakeware, RDF.type, RDFS.Class))
g.add((EX.CookwareBakeware, RDFS.subClassOf, EX.Home))

g.add((EX.PetCare, RDF.type, RDFS.Class))
g.add((EX.PetCare, RDFS.subClassOf, EX.Home))

g.add((EX.Books, RDF.type, RDFS.Class))
g.add((EX.Books, RDFS.subClassOf, EX.Entertainment))

g.add((EX.Video, RDF.type, RDFS.Class))
g.add((EX.Video, RDFS.subClassOf, EX.Entertainment))

g.add((EX.Music, RDF.type, RDFS.Class))
g.add((EX.Music, RDFS.subClassOf, EX.Entertainment))

g.add((SCHEMA.brand, RDF.type, RDF.Property))
g.add((SCHEMA.brand, RDFS.domain, SCHEMA.Product))
g.add((SCHEMA.brand, RDFS.range,  SCHEMA.Brand))

g.add((SCHEMA.category, RDF.type, RDF.Property))
g.add((SCHEMA.category, RDFS.domain, SCHEMA.Product))
g.add((SCHEMA.category, RDFS.range,  EX.Category))

g.add((EX.collaborationBrand, RDF.type, RDF.Property))
g.add((EX.collaborationBrand, RDFS.subPropertyOf, SCHEMA.brand))
g.add((EX.collaborationBrand, RDFS.domain, SCHEMA.Product))
g.add((EX.collaborationBrand, RDFS.range,  SCHEMA.Brand))

g.add((EX.primaryCategory, RDF.type, RDF.Property))
g.add((EX.primaryCategory, RDFS.subPropertyOf, SCHEMA.category))
g.add((EX.primaryCategory, RDFS.domain, SCHEMA.Product))
g.add((EX.primaryCategory, RDFS.range,  EX.Category))

g.add((EX.secondaryCategory, RDF.type, RDF.Property))
g.add((EX.secondaryCategory, RDFS.subPropertyOf, SCHEMA.category))
g.add((EX.secondaryCategory, RDFS.domain, SCHEMA.Product))
g.add((EX.secondaryCategory, RDFS.range,  EX.Category))

g.add((SCHEMA.name, RDF.type, RDF.Property))
g.add((SCHEMA.name, RDFS.domain, SCHEMA.Product))
g.add((SCHEMA.name, RDFS.range,  XSD.string))

g.add((SCHEMA.color, RDF.type, RDF.Property))
g.add((SCHEMA.color, RDFS.domain, SCHEMA.Product))
g.add((SCHEMA.color, RDFS.range,  XSD.string))

g.add((SCHEMA.itemCondition, RDF.type, RDF.Property))
g.add((SCHEMA.itemCondition, RDFS.domain, SCHEMA.Product))
g.add((SCHEMA.itemCondition, RDFS.range,  XSD.string))

g.add((SCHEMA.size, RDF.type, RDF.Property))
g.add((SCHEMA.size, RDFS.domain, SCHEMA.Product))
g.add((SCHEMA.size, RDFS.range,  XSD.string))

g.serialize(destination="vinted_schema.ttl", format="turtle")
print("Saved to vinted_schema.ttl")