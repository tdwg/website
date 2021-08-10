---
title: TDWG Access Protocol for Information Retrieval (TAPIR)
summary: TAPIR is a computer protocol designed for discovery, search and retrieval of distributed data over the Internet. TAPIR consists of a [specification](http://tdwg.github.io/tapir/docs/) that determines how client applications seeking information should communicate with server applications hosting data. TAPIR is an approved TDWG standard.
cover_image: https://c1.staticflickr.com/7/6158/6263150201_a4c9705ff9_b.jpg
cover_image_by: Biodiversity Heritage Library
cover_image_ref: https://www.flickr.com/photos/biodivlibrary/6263150201
tags: technical specification, current standard, 2010
github: https://github.com/tdwg/tapir
website: http://tdwg.github.io/tapir/docs/
website_title: TAPIR specification
---

## Header section

Title
: TDWG Access Protocol for Information Retrieval (TAPIR)

Permanent IRI (for citations and links)
: <http://www.tdwg.org/standards/449>

Publisher
: [Biodiversity Information Standards (TDWG)](https://www.tdwg.org/)

Ratified
: 2009-09-09

Status
: [Current standard](https://www.tdwg.org/standards/status-and-categories/)

Category
: [Technical specification](https://www.tdwg.org/standards/status-and-categories/#categories%20of%20tdwg%20standards_1)

Abstract
: TAPIR is a computer protocol designed for discovery, search and retrieval of distributed data over the Internet. TAPIR consists of a specification that determines how client applications seeking information should communicate with server applications hosting data. TAPIR is an approved TDWG standard.

Bibliographic citation
: > TAPIR Task Group. 2009. TDWG Access Protocol for Information Retrieval (TAPIR). Biodiversity Information Standards (TDWG) http://www.tdwg.org/standards/449

## Motivation

[DiGIR](http://www.digir.net/) and [BioCASe](http://www.biocase.org/products/protocols/) are alternative protocols developed to access historical data from geographically distributed biological collections. While DiGIR and BioCASe have been successful in their own domains, incompatibilities between them make the exchange of biodiversity data more complex than it should be. TAPIR, the TDWG Access Protocol for Information Retrieval, is an international project to solve this problem and to add new functionality.

## How TAPIR works

A TAPIR network comprises distributed data providers with different database systems and different data structures, but all of them having the same kind of content. Consider a group of natural history museums that want to make their biological specimen data available from a single Web search page. Each organization has its own database in a different computer environment. For example, some may use a commercial collection management software, others may use an open source software environment, or even just a simple spreadsheet. Their common requirement is for all searches via a single Web page to access all databases and produce a combined and integrated response to the searcher.

Since all databases contain the same kind of content, it is therefore possible to define what is called a data abstraction layer. DarwinCore is an example of a data abstraction layer for biodiversity data. DarwinCore specifies the details of a specimen or observation of a specimen, such as the name of the organism, where, when and by whom it was collected. TAPIR works with one or more of these data abstraction layers to make it appear to the searcher that all the separate databases are like one big integrated database.

The data providers usually don't need to change their databases nor to periodically export their data. Instead, they will typically install a 'wrapper' software application and then configure it in a way that each concept from the data abstraction layer corresponds to a particular field in their own databases.

This wrapper receives the remote TAPIR search request, translates it into the local language and data structure, applies it to the database, and then sends back a TAPIR search response to the searcher.

TAPIR is flexible enough to be used in a wide range of applications. Other examples include harvesting data to build a central database, sharing data using different Web formats (e.g. RSS, RDF or KML) or building Web interfaces to help browse or search any database.

## TAPIR's key features

- integrates well with the Web infrastructure because it is based on established international Web standards like HTTP, XML and XML Schema.
- is independent of the data being exchanged and therefore can be used to access a wide range of data.
- can return data in many different formats - search responses are flexible and customizable.
- includes five operations to cover all necessary aspects for searching and retrieving data in a network: access to metadata (descriptive data) and capabilities of the provider, preliminary data discovery and data mining, searching, and monitoring the data provider service.
- allows all operations to be invoked through simple Web addresses.
- supports complex requests.
- has existing TAPIR wrapper applications including PyWrapper, TapirLink and TapirDotNET. 

## Resources

- [TAPIR 1.0 Normative Specification](http://tdwg.github.io/tapir/docs/tdwg_tapir_specification_2010-05-05.html)
- [W3C XML Schema for document validation (normative)](http://tdwg.github.io/tapir/schema/tapir.xsd)
- [Concept alias definitions for common TDWG standards](http://tdwg.github.io/tapir/cns/alias.txt)
- [TAPIR output models and query templates](http://tdwg.github.io/tapir/cs/)
- [TAPIR Network Builders' Guide](http://tdwg.github.io/tapir/docs/TAPIRNetworkBuildersGuide_2010-05-05.html)

## Software

- **TapirLink**: the original PHP TapirLink software is being host on SourceForge: <http://sourceforge.net/projects/digir/files/TapirLink/> and <http://sourceforge.net/p/digir/svn/HEAD/tree/tapirlink/>
- **PyWrapper**: A python provider software, based on the BioCASE predecessor:
<http://sourceforge.net/p/digir/svn/HEAD/tree/pywrapper/>
- **TAPIR Tester**: <http://sourceforge.net/p/digir/svn/HEAD/tree/tapirtester/>
- **TAPIR Builder**: <http://sourceforge.net/p/digir/svn/HEAD/tree/tapirbuilder/>


## Parts of the standard

This standard is comprised of 6 documents. 

Documents:

**Title:** TDWG Access Protocol for Information Retrieval (TAPIR) Protocol Specification \
**Permanent IRI:** [http://rs.tdwg.org/tapir/doc/specification/](http://tdwg.github.io/tapir/docs/tdwg_tapir_specification_2010-05-05.html) \
**Created:** 2010-05-05 \
**Last modified:** 2010-05-05 \
**Contributors:** \
Renato De Giovanni (lead author) - Centro de Referência em Informação Ambiental \
Charles Copp (lead author) - Environmental Information Management  \
Markus Döring (author) - Botanic Garden and Botanical Museum Berlin-Dahlem  \
Anton Güntsch (author) - Botanic Garden and Botanical Museum Berlin-Dahlem  \
Dave Vieglais (author) - KU Natural History Museum \
Donald Hobern (author) - Global Biodiversity Information Facility \
Javier de la Torre (author) - Botanic Garden and Botanical Museum Berlin-Dahlem  \
John Wieczorek (author) - Museum of Vertebrate Zoology at Berkeley \
Robert Gales (author) - KU Natural History Museum \
Roger Hyam (author) - TDWG \
Stanley Blum (author) - California Academy of Sciences \
Perry Steven (author) - KU Natural History Museum \
Piers Higgs (review manager) \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** This document specifies the TAPIR protocol and the structure and syntax of TAPIR messages.   \
**Citation:** TAPIR Task Group. 2010. TDWG Access Protocol for Information Retrieval (TAPIR) Protocol Specification. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/tapir/doc/specification/

**Title:** TDWG Access Protocol for Information Retrieval (TAPIR) XML Schema  \
**Permanent IRI:** [http://rs.tdwg.org/tapir/doc/xmlschema/](http://tdwg.github.io/tapir/schema/tapir.xsd) \
**Created:** 2009-02-05 \
**Last modified:** 2009-02-05 \
**Contributors:** \
Renato De Giovanni (lead author) - Centro de Referência em Informação Ambiental \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** TAPIR XML Schema. TAPIR is an acronym for TDWG Access Protocol for Information Retrieval. It is a unified and extended protocol based on DiGIR and BioCASe. TAPIR specifies a standardised, stateless, HTTP transmittable, XML-based request and response protocol for accessing structured data that may be stored on any number of distributed databases of varied physical and logical structure.   \
**Citation:** TAPIR Task Group. 2009. TDWG Access Protocol for Information Retrieval (TAPIR) XML Schema. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/tapir/doc/xmlschema/

**Title:** TDWG Access Protocol for Information Retrieval (TAPIR) Concept Aliases \
**Permanent IRI:** [http://rs.tdwg.org/tapir/doc/conceptaliases/](http://tdwg.github.io/tapir/cns/alias.txt) \
**Created:** 2015-06-01 \
**Last modified:** 2015-06-01 \
**Contributors:** \
Renato De Giovanni (lead author) - Centro de Referência em Informação Ambiental \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** Globally unique aliases for concepts. The aliases listed here are only unique within their concept source.  \
**Citation:** TAPIR Task Group. 2015. TDWG Access Protocol for Information Retrieval (TAPIR) Concept Aliases. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/tapir/doc/conceptaliases/

**Title:** TDWG Access Protocol for Information Retrieval (TAPIR) Network Builders' Guide \
**Permanent IRI:** [http://rs.tdwg.org/tapir/doc/guide/](http://tdwg.github.io/tapir/docs/TAPIRNetworkBuildersGuide_2010-05-05.html) \
**Created:** 2015-06-03 \
**Last modified:** 2015-06-03 \
**Contributors:** \
Charles Copp (lead author) - Environmental Information Management  \
Renato De Giovanni (lead author) - Centro de Referência em Informação Ambiental \
Lee Belbin (reviewer) - TDWG Infrastructure Project \
Markus Döring (reviewer) - Botanic Garden and Botanical Museum Berlin-Dahlem  \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** This document provides guidelines for building networks based on the TAPIR protocol.   \
**Citation:** TAPIR Task Group. 2015. TDWG Access Protocol for Information Retrieval (TAPIR) Network Builders' Guide. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/tapir/doc/guide/

**Title:** TDWG Access Protocol for Information Retrieval (TAPIR) Output Models and Query Templates \
**Permanent IRI:** [http://rs.tdwg.org/tapir/doc/models/](http://tdwg.github.io/tapir/cs/) \
**Created:** 2015-11-25 \
**Last modified:** 2015-11-25 \
**Contributors:** \
Renato De Giovanni (lead author) - Centro de Referência em Informação Ambiental \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** This page is an index to TAPIR XML models and query templates. \
**Citation:** TAPIR Task Group. 2015. TDWG Access Protocol for Information Retrieval (TAPIR) Output Models and Query Templates. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/tapir/doc/models/

