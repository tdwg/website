---
title: Natural Collections Descriptions (NCD)
summary: 
cover_image: 
cover_image_by: 
cover_image_ref: 
tags: technical specification, draft standard
github: https://github.com/tdwg/ncd
---

**Status note:**  _NCD is a draft standard that was develop more than a decade ago and submitted for ratification in 2008. Personnel changes in several critical roles caused the ratification process to stall, so the specification has remained as a draft since then. The [NCD Interest Group](https://github.com/tdwg/ncd) was reestablished in 2016 and has begun to re-work the draft specification with the ultimate aim of getting it ratified as a TDWG standard._

_The last version of the draft standard, [NCD-v090](https://github.com/tdwg/ncd/tree/master/NCD-v090_TDWG) consists of two parts, a normative document, which specifies classes, attributes, and their definitions, and a second part, which explains the rationale for the design and composition. The text below was taken from the Summary of the non-normative part._

-----

**Authors:** Neil Thomson (Natural History Museum, London), Roger Hyam (Royal Botanic Garden Edinburgh), Constance Rinaldo (Harvard University), Carol Butler (Smithsonian Institution), Doug Holland (Missouri Botanical Gardens), Barbara Mathé (American Museum of Natural History), Günter Waibel (RLG Programs, OCLC), Wouter Addink (ETI Bioinformatics), Ruud Altenburg (ETI), Markus Döring (Berlin Botanic Garden)

## Summary

Natural Collections Description (NCD) is a data standard for describing collections of natural history materials at the collection level; one NCD record [some elements may repeat] describes one entire collection.

Collection descriptions are electronic records that document the holdings of an organisation as groups of items, which complement the more traditional item-level records such as are produced for a single specimen or a library book. NCD is tailored to natural history. It lies between general resource discovery standards such as Dublin Core (DC) and rich collection description standards such as the Encoded Archival Description (EAD). It is possible to extract a Dublin Core record from an NCD record for use with general resource discovery systems, or to use an NCD record as the seed for a richer collection description, like an EAD record.

The NCD standard covers all types of natural history collections, such as specimens, original artwork, archives, observations, library materials, datasets, photographs or mixed collections such as those that result from expeditions and voyages of discovery.
NCD primarily holds information about collections of objects, but can also be used to describe organisations (collections of collections) and networks (collections of organisations). There are many existing sources of information about biodiversity organisations, but they are scattered and in different formats.

This document accompanies the normative part of the NCD standard. The standard consists of the series of class and property definitions and is presented in a separate document. These definitions are identified by unique TDWG Uniform Resource Identifiers (URI). It assumes that copies of the definitions will be hosted at the specified URIs given in the normative form document. 

The standard also contains recommendations on the use of Dublin Core and vCard properties. This avoids duplicating established vocabularies and facilitates interpretation of NCD documents by non NCD aware applications.

It is expected that NCD will develop further as experience is gained in the projects that are making use of it, particularly in the addition of terms to the pick-lists. It has reached a sufficiently mature state that applications may be based on it. Following approval from the TDWG appraisers it will be designated as NCD version 1.0 and made widely known to the biodiversity informatics community.

The NCD standard is the culmination of work on collections descriptions carried out for the European Union Framework VI programme SYNTHESYS and the work performed by the Anglo-American group Resources Available in Natural Sciences (RAVNS), which operates under the auspices of RLG Programs, OCLC.

The normative documentation includes an example record and, for those that are developing applications based on NCD a column provides suggested cardinality – that is, for fields that should be considered mandatory (M) or may have more than one value – that is, repeatable (R) or indicate text in the local language (L).

To ensure that the barriers to usage are as low as possible, only four properties of the Collection class are considered to be mandatory:
1. Author of the record
2. Date of record creation
3. Collection name
4. Collection description

An NCD Toolkit has been developed by ETI Bioinformatics in Amsterdam with the aid of funding from GBIF and is available for download at https://sourceforge.net/projects/ncdtoolkit/. Version 1.0 of the NCD Toolkit is based on NCD v0.8. It is a cross-platform database which enables natural history organisations to record data about their own collections.
