---
title: TAPIR Task Group Charter
summary: a Task Group of the Technical Architecture Group (TAG)
cover_image: https://c1.staticflickr.com/7/6158/6263150201_a4c9705ff9_b.jpg
cover_image_by: Biodiversity Heritage Library
cover_image_ref: https://www.flickr.com/photos/biodivlibrary/6263150201
tags: Task Group, Charter
github: https://github.com/tdwg/tapir
---

## Convener

Renato De Giovanni (renato [at] cria [dot] org [dot] br)

## Purpose

The TAPIR task group will draft, document and maintain the TAPIR (TDWG Access Protocol for Information Retrieval) Standard for TDWG.

TAPIR specifies a standardised, stateless, HTTP transmittable, XML-based request and response protocol for accessing structured data that may be stored on any number of distributed databases of varied physical and logical structure. TAPIR combines and extends the features of the BioCASe and DiGIR protocols to create a new and more generic means of communication between client applications and data providers using the Internet. The TAPIR task group will ensure the applicability and effectiveness of the protocol through association with the development of the PyWrapper v2 reference implementation.

TAPIR was developed for use with biodiversity and natural science collection data but is a generic tool applicable to other domains. The TAPIR task group will maintain awareness of the potential for interoperability with other subject domains and the protocols that are used or are under development in those domains, and will consider the benefits or problems of convergence with them. The TAPIR task group will liaise with other TDWG groups and allied working groups to ensure compatibility of approach and avoid duplication of effort particularly with related biodiversity standards initiatives.

## Background

The rapid expansion of the Internet and use of the World Wide Web has been accompanied by the desire to create new information services capable of drawing data from large numbers of data providers, regardless of their data management systems or geographic location. There are many practical problems involved in marshalling data from many sources, the great variation in data stores, data structure and data quality being particularly challenging.

XML has become a widely used method to define structured content and share information over the Internet. Formal description of XML documents, including structure, content and semantics, can be done using XML Schema. XML schemas are effective for describing domain-specific data, usually referred to as content schemas, like DarwinCore and ABCD. XML schemas are also useful for the development of accompanying protocols for transmitting requests and responses between services. There have been two major initiatives in the development of biodiversity information networks based on these technologies. In North America, The Species Analyst Network developed the DarwinCore schema and the DiGIR protocol. In Europe, the TDWG ABCD schema and BioCASe protocol have been used to establish the BioCASE network. The DiGIR and BioCASe protocols have many similarities but they are not interchangeable and this is clearly not desirable for global interoperability.

The importance of developing a unified protocol that could handle different content schemas was discussed at the GBIF Data Access and Database Interoperability sub-committee meeting held in Oaxaca in 2004. This discussion lead to GBIF commissioning a study that was published by Döring and De Giovanni in September 2004[1]. This study included a proposal for an integrated protocol. The proposal evolved from a number of preliminary proposals that had considered alternative technologies including SOAP/WSDL, WFS and XQuery. These alternatives and the reasons why they were not adopted at that time are discussed in the GBIF study. A reference implementation based on the initial proposal was delivered in August 2005 as a new version (v2) of the PyWrapper software.

Work continued, with a further meeting held in Madrid in November 2005, where major refinements of the protocol were agreed. A "feature freeze" in January 2006 enabled documentation to be initiated.

The establishment of the TAPIR task group is intended to ensure that the proposed standard and its reference implementations are maintained, developed, documented and respond to future needs and changes.

## Scope

The scope of the task group is currently limited to the development of the TAPIR standard and its reference implementation. It is recognised that there are issues of common interest with other biodiversity informatics initiatives including TDWG content schema subgroups (ABCD, TCS, NCD, SDD and DarwinCore) and external parties such as the Dublin Core Metadata Initiative and the Open Geospatial Consortium. The TAPIR subgroup will liaise with members of other relevant subgroups and projects to ensure a communality of approach and avoidance of duplication. The relationship of the developing TAPIR standard with geospatial data transfer standards and protocols used in other subject domains will also be kept under frequent review.

TAPIR has been refined into a generic product that has the potential to enable interoperability with domains other than biological observations and specimen collections, including geological, ecological, climate, gene sequence and geospatial data. The development of a generic tool has lead to increasing convergence with similar tools and standards used in a wider context, for instance, the OGC Web Feature Service (WFS) standard (where biodiversity data can be regarded as a geospatial feature). The TAPIR task group will monitor the degree of this convergence and consider compatibility issues including the possible adaptation or adoption of these standards.

The TAPIR task group will maintain an overview of the PyWrapper software as a reference implementation of the TAPIR standard. The task group will produce sufficient documentation and guidelines to enable the use of the TAPIR protocol by other software developers and data providers and to explain its principal features to non-technical users (e.g. data holders whose databases have been connected to GBIF via a wrapper implementing TAPIR).

## Core Members

- Donald Hobern (dhobern [at] gbif [dot] org) 
- Javier de la Torre (jatorre [at] mncn [dot] csic [dot] es) 
- Markus Döring (m [dot] doering [at] bgbm [dot] org) 
- Renato De Giovanni (renato [at] cria [dot] org [dot] br) 
- Charles Copp (eim [at] globalnet [dot] co [dot] uk) 

## Clients

- Individuals and organisations involved in providing biodiversity information services based on distributed networks of data holders
- Developers of interoperability and data content standards
- Biodiversity information managers
- Potential users in other subject domains where an HTTP-based request-response protocol may be applicable for information delivery
- Outcomes and Outputs
- The TAPIR Schema
- TAPIR online resources (website, wiki)
- PyWrapper v2
- TAPIR Technical documentation
- TAPIR Overview and Users Guide
 
## Strategy

Our guiding objectives are to create a protocol for biodiversity information sharing that is:

1. effective to use and clear to understand;
1. not bound to any particular operating system or software;
1. flexible and extensible to meet changing needs;
1. compatible with developing standards in the wider arena of Internet-based data exchange, particularly geospatial technologies and standards;
1. maintainable;
1. well documented and
1. freely and readily available.

The work process will include the following activities:

1. Maintaining appropriate Web resources to present information and encourage debate;
1. Document and circulate the TAPIR schema (xsd) for wider review and comment;
1. Oversee the reference implementation of TAPIR within the PyWrapper v2 software;
1. Incorporate revisions and publish the full draft of the TAPIR Standard with accompanying explanatory documents and full technical specification;
1. Present the documented protocol to the TDWG annual conference;
1. Propose TAPIR for adoption as a full TDWG standard;
1. Monitor and refine the standard as necessary and consider convergence with standards in other subject domains;

## References

[1] GBIF Data Access and Database Interoperability: A Unified protocol for search and retrieval of distributed data. GBIF September 2004, Markus Döring and Renato De Giovanni see: http://www.cria.org.br/protocols/newprotocol.pdf

Resources:

- TAPIR Repository: http://github.com/tdwg/tapir/
- TAPIR Schema Repository: http://rs.tdwg.org/tapir/
- TAPIR Mailing List: http://lists.tdwg.org/mailman/listinfo/tdwg-tag

## Version History

August 29, 2006 - Document created - by Markus Döring

April 24, 2009 - Minor updates - by Renato De Giovanni
