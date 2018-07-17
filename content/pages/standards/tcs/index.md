---
title: Taxonomic Concept Transfer Schema (TCS)
summary: 
cover_image: https://images.unsplash.com/photo-1502912143929-50c8a1ce1f69
cover_image_by: Fancycrave @fancycrave
cover_image_ref: https://unsplash.com/photos/4A8ZSlAOUqs
tags: technical specification, 2005 standard, 2005
github: https://github.com/tdwg/tcs
---

# Taxonomic Concept Transfer Schema (TCS)

* **Download**: [Download](https://github.com/tdwg/tcs/tree/master/TCS101)
* **Status**: TDWG current (2005) Standard
* **Category**: Technical specification
* **Permanent URL**: http://www.tdwg.org/standards/117
* **TDWG task group**: Taxonomic Names and Concepts interest group
* **Date submitted**: 2006-11-24
* **Date published**: 2005-09-16
* **Last modified**: 2007-06-11

## Abstract

The availability, exchange and interpretation of taxonomic information (such as species check lists, distribution and identification data) is of critical importance to taxonomists, ecologists and other biologists and legislators, amongst others. This information is provided by a number of global and local taxonomic database services. These databases hold records, often based on valid scientific names for species, according to their own models of what constitutes a taxonomic 'entity' or concept (i.e. a species or higher level taxon). Databases typically model a single view of taxonomy, whilst making some attempt to relate their concepts to synonymous names or concepts.

The rules and history of taxonomic nomenclature mean that scientific names do not unambiguously identify taxonomic concepts as represented according to different models of taxonomy. Therefore the same name will apply to different taxon concepts according to different taxonomic viewpoints (conversely, very similar concepts according to alternative taxonomies may sometimes be given different names). The problems inherent in using names as identifiers are recognized and might be addressed by representing richer taxon concepts, based on a name plus a reference to the definition of the concept or at least by capturing the usage of that name according to some original taxonomic source.

The need for a common mechanism for the providers of taxonomic information to exchange information with other providers and users of varying expertise in taxonomy was recognized at TDWG Lisbon 2003. Such a mechanism must adequately represent the data as modelled by the owners of the data, whist facilitating integration with data provided according to different models of taxonomy.

The development of an abstract model for a taxonomic concept, which can capture the various models represented and understood by the various data providers, is central to this project. This model is presented as an XML schema document that is proposed as a standard to allow exchange of data between different data models. It aims to capture data as understood by the data owners without distortion, and facilitate the query of different data resources according to the common schema model.

The TCS schema was conceived to allow the representation of taxonomic concepts as defined in published taxonomic classifications, revisions and databases.

As such, it specifies the structure for XML documents to be used for the transfer of defined concepts. Valid transfer documents may either explicitly detail the defining components of taxon concepts, transfer GUIDs referring to defined taxon concepts (if and when these are available) or a mixture of the two.

The TCS schema is not designed to facilitate the exchange or documentation of information about Taxon Concepts where this information is not part of a taxonomic revision creating new concepts. The amount and variety of (additional) information that can be potentially assigned to concepts is outside the scope of a taxonomic concept transfer schema, but we would encourage the development of domain specfic models that use or extend this schema. XML supports this flexibility by allowing the use of different name spaces.

For example, whilst a TCS taxon concept definition may include details of specimen circumscription (i.e. list specimens that are asserted to define the taxon concept) datasets that merely include observations identifying specimens as being examples of a taxon concept would reference a defined taxon concept, not constitute a new or modified concept. That is, TCS documents are for transferring the definitions of taxon concepts, not for detailing observations of these defined concepts.

Examples of observational datasets that could refer to defined taxon concepts might include:

* ecological field records, which record abundance data on a variety taxa
* descriptive datasets that include descriptions of representative specimens or taxa
* specimen records for biological collections

The observations recorded in these would not constitute definitions of the concepts, but document instances of the concept. (However, observation datasets might themeselves be included as part of a taxon concept definition, e.g. as specimen or character circumscriptions - if this is what the 'creator' of the concept intended).

Once concept definitions are globally available and have been assigned GUIDs, referencing them in observation datasets etc. is simplified. In the absence of GUIDs some form of user key could be recorded that would identify a preexisting concept. This might consist of the scientific name and concept author (AccordingTo).

Where there is no appropriate, prexisting globally defined concept to reference, datasets could provide TCS definitions of the concept being described/observed/identified in TCS format. These would minimally consist of a name, but optimally include reference to the origin of the concept definition (The AccordingTo element in TCS). Thus field data that records presence of Aus bus, Aus cus and Aus dus, as identified in the field guide of (Kubrick, 2001) should include this information in the data description/mark-up. It then will be possible to resolve these incompletely defined concepts with other concept records represented in TCS format.

## Preferred citation

> Taxonomic Names and Concepts interest group. 2006. Taxonomic Concept Transfer Schema (TCS), version 1.01. Biodiversity Information Standards (TDWG) http://www.tdwg.org/standards/117
