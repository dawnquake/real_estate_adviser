from SPARQLWrapper import SPARQLWrapper, JSON



def query_postcode_hmlc_transactions(postcode_with_space: str):

    """
    https://landregistry.data.gov.uk/app/qonsole
    """

    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX lrcommon: <http://landregistry.data.gov.uk/def/common/>
    PREFIX lrppi: <http://landregistry.data.gov.uk/def/ppi/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT ?paon ?saon ?street ?town ?county ?postcode ?amount ?date ?category
    WHERE
    {
        VALUES ?postcode {"POSTCODE_TO_REPLACE"^^xsd:string}

        ?addr lrcommon:postcode ?postcode.

        ?transx lrppi:propertyAddress ?addr ;
                lrppi:pricePaid ?amount ;
                lrppi:transactionDate ?date ;
                lrppi:transactionCategory/skos:prefLabel ?category.

        OPTIONAL {?addr lrcommon:county ?county}
        OPTIONAL {?addr lrcommon:paon ?paon}
        OPTIONAL {?addr lrcommon:saon ?saon}
        OPTIONAL {?addr lrcommon:street ?street}
        OPTIONAL {?addr lrcommon:town ?town}
    }
    ORDER BY ?amount
    """

    query = query.replace("POSTCODE_TO_REPLACE", postcode_with_space)

    # Define the SPARQL endpoint
    sparql = SPARQLWrapper("https://landregistry.data.gov.uk/landregistry/query")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)  # Set the return format to JSON

    # Execute the query
    try:
        response = sparql.query().convert()  # Perform the query and get the results as JSON
        results = response["results"]["bindings"]
    except:
        results = "Sorry, HM Land Registry is currently busy at the moment"

    return results

