---
title: TDWG Access Protocol for Information Retrieval (TAPIR)
summary: 
cover_image: https://c1.staticflickr.com/7/6158/6263150201_a4c9705ff9_b.jpg
cover_image_by: Biodiversity Heritage Library
cover_image_ref: https://www.flickr.com/photos/biodivlibrary/6263150201
tags: technical specification, current standard, 2009
github: https://github.com/tdwg/tapir
---

_Renato De Giovanni_
August 28, 2007

## Definition

TAPIR is a computer protocol designed for discovery, search and retrieval of distributed data over the Internet. TAPIR consists of a [specification](http://tdwg.github.io/tapir/docs/) that determines how client applications seeking information should communicate with server applications hosting data. TAPIR is an approved TDWG standard.

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
 - [TAPIR Executive Summary](http://www.tdwg.org/activities/tapir/executive-summary/)
 - [TAPIR 1.0 Normative Specification](http://tdwg.github.io/tapir/docs/tdwg_tapir_specification_2010-05-05.html)
 - [W3C XML Schema for document validation (normative)](http://tdwg.github.io/tapir/schema/tapir.xsd)
 - [Concept alias definitions for common TDWG standards](http://tdwg.github.io/tapir/cns/alias.txt)
 - [TAPIR output models and query templates](http://tdwg.github.io/tapir/cs/)
 - [TAPIR Charter](http://www.tdwg.org/activities/tapir/charter/)
 - [TAPIR Network Builders' Guide](http://tdwg.github.io/tapir/docs/TAPIRNetworkBuildersGuide_2010-05-05.html)


### TapirLink
The original PHP TapirLink software is being host on SourceForge: 
 - http://sourceforge.net/projects/digir/files/TapirLink/
 - http://sourceforge.net/p/digir/svn/HEAD/tree/tapirlink/
 

### PyWrapper 
A python provider software, based on the BioCASE predecessor:
http://sourceforge.net/p/digir/svn/HEAD/tree/pywrapper/


### TAPIR Tester
http://sourceforge.net/p/digir/svn/HEAD/tree/tapirtester/

### TAPIR Builder
http://sourceforge.net/p/digir/svn/HEAD/tree/tapirbuilder/

 

## Preferred citation

> De Giovanni Renato, Döring Markus, Güntsch Anton, Vieglais Dave, Hobern Donald, de la Torre Javier, Wieczorek John, Gales Robert, Hyam Roger, Blum Stanley, Perry Steven. 2010. TDWG Access Protocol for Information Retrieval (TAPIR), Version 1.0. Biodiversity Information Standards (TDWG) http://www.tdwg.org/standards/449
