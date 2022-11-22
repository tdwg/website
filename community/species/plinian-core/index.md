---
title: Plinian Core
summary: This group works towards developing a data specification, the Plinian Core, that can be used to describe different aspects of biological species information. By "biological species information" all kinds of properties or traits related to taxa, including biological and non-biological traits are within scope. Thus, for instance, terms pertaining to descriptions, legal aspects, conservation, management, demography, nomenclature, and related resources are incorporated. The Plinian Core’s aim is to facilitate the exchange of information about species and higher taxa, covering biological and non-biological aspects pertaining to all taxonomic groups.
cover_image: https://images.unsplash.com/photo-1605315222417-f2ddd393a2e9
cover_image_by: David Clode
cover_image_ref: https://unsplash.com/photos/Fk99LvrIqws
tags: task group
github: https://github.com/tdwg/PlinianCore
---

## Convener  

[Francisco Pando](pando@rjb.csic.es) - Real Jardín Botánico, CSIC. Madrid

## Core members  

Name | Role
--- | ---
María Mora | Biodiversity informatics expertise
William Ulate | Biodiversity informatics expertise
Manuel Vargas | Biodiversity informatics expertise
Camila Plata | Biodiversity informatics expertise
José Cuadra | Biodiversity informatics expertise

## Motivation

Species level information is one of the most demanded services or products from the taxonomic experts. 
We see species pages everywhere: from on-line floras and faunas to CITES manuals for custom agents, to guides for naturalists. As such, aiming to produce a data specification to facilitate data integration and interoperability among species pages is a mean with great potential to increase efficiency and cooperative work.

### What is in scope?

* Species level catalogs of any kind of biological objects or data.
* Terminology associated with biological collection data.
* Striving for compatibility with other biodiversity-related standards.
* Facilitating the addition of components and attributes of biological data.

### What is not in scope?

* Data interchange protocols.
* Non-biodiversity-related data.
* Occurrence level data.
 
Plinian Core design required to be easy to use, self-contained, able to support data integration from multiple databases, and the ability to handle different levels of granularity.

## Goals outputs and outcomes

* An assessment on how Plinian Core relates to other TDWG standards. Done: [https://doi.org/10.3897/biss.2.25869](https://doi.org/10.3897/biss.2.25869)
* A detailed documentation on the different terms included in Plinian Core. Done: [https://github.com/tdwg/PlinianCore/wiki](https://github.com/tdwg/PlinianCore/wiki)
* At least three implementations of species information systems based on Plinian Core. Done (See below, section “Relevant projects and initiatives”)
* A SPARQL Endpoint and underlying ontology implemented and working. Done: [https://crossnature.eu/visor/](https://crossnature.eu/visor/)
* A standard specification complying with the TDWG SDS. The TG plans to make a formal submission of the documentation to the TDWG Executive by November 27th, 2020. In progress

## Becoming involved

This group welcomes participation from all interested parties on implementing species catalogs, species pages or other usages or profiles of the standard. Also individuals who have a vested interest in maintaining the stability and interoperability of Plinian Core. 
If you are interested in participating in the group, please contact the convener or a core member.

## History/context

* Plinian Core started in 2004 as a dialog between Maria Mora (INBio, Costa Rica) and Francisco Pando (GBIF-Spain) around the idea of developing a common system to gather, manage and publish "species-level information. The basis and use cases for these ideas were INBIO's "species pages" (UBIS) and the “CD-ROM of Flora Iberica".
* More concrete ideas were developed during the GBIF-organized meeting "Building SpeciesBanks: How Shall We Shape the Future?” (Amsterdam, 2005).
* In 2005-2006, an intense collaboration between INBio and GBIF.ES was maintained, from which the first version of the standard expressed as xsd is created, and receives its current name: Plinian Core.
* 2007-2009 University of Granada (Spain) and the Colombian Biodiversity Information System (SiB -Colombia) adheres to the initiative.
* INBio develops the first "implementable" version of the PliC: that is dubbed "Flat Plinian".
* A portal of "species and specimens" is developed on the architecture of the GBIF data portal (Tapir), by INBio, in the context of IABIN (the Inter-American Biodiversity Information Network), and with the collaboration of GBIF.ES
* 2011 Collaboration with Encyclopedia of Life started. Strategic decision to separate a conceptual model (later called "Abstract Model) from implementations adopted. CONABIO (Mexico) becomes an active partner in the development of PliC
* 2012 Plinian Core activities start aligning with TDWG and procedures; globalization of the developments. 
* 2012-Partnership for the development of Plinian Core in this new phase incorporated the University of Granada (UG, Spain), the Colombian Biodiversity information System (SiB-Colombia, Colombia), the National Commission for the Knowledge and Use of Biodiversity (Conabio, Mexico) and the University of São Paulo (USP, Brazil), and workshops and working sessions were organized, some sponsored by the involved participants, some by GBIF.
* As a result of the process started in 2012, a new version, Plinian Core v3.1 was defined. This provides more flexibility to fully represent the information of a species in a variety of scenarios. New elements to deal with aspects such as IPR, related resources, references, etc. were introduced, and elements already included were better-defined and documented.
* The “Species Information Interest Group”was approved by the TDWG Executive in 2013. Plinian Core is identified as a priority task within that IG.
* 2014-2018 First full implementations of Plinian core are put in Production (see section “Relevant projects and initiatives”)
* 2017 -2019 Advancing implementation of Plinian Core in the Living Atlases in coordination with the LA community for the BIE module of Living Atlases.  (see: Vargas & al., 2018)

## Resources

* Gerbracht J (2018) A Content Management System and underlying models for avian taxonomic monographs. Biodiversity Information Science and Standards 2: e25693. [https://doi.org/10.3897/biss.2.25693](https://doi.org/10.3897/biss.2.25693)
* Pando F (2017) How species interactions are managed in Plinian Core: Status and questions. Proceedings of TDWG 1: e20556. [https://doi.org/10.3897/tdwgproceedings.1.20556](https://doi.org/10.3897/tdwgproceedings.1.20556)
* Pando F (2018) Comparison of species information TDWG standards from the point of view of the Plinian Core specification. Biodiversity Information Science and Standards 2: e25869. [https://doi.org/10.3897/biss.2.25869](https://doi.org/10.3897/biss.2.25869)
* Plinian Core pages at TDWG’s GitHub: specification, documentation, issues and developments: [https://github.com/tdwg/PlinianCore](https://github.com/tdwg/PlinianCore)
* Vargas M, Mora M, Ulate W, Cuadra J (2018) The Living Atlases Community in Action: Sharing Species Pages through the Atlas of Living Costa Rica. Biodiversity Information Science and Standards 2: e25990. [https://doi.org/10.3897/biss.2.25990](https://doi.org/10.3897/biss.2.25990)
* Vargas M, Mora Cross M, Cuadra J, Ulate Rodríguez W (2019) Sharing Species Pages in the Atlas of Living Costa Rica using Plinian Core. Biodiversity Information Science and Standards 3: e35474.  [https://doi.org/10.3897/biss.3.35474](https://doi.org/10.3897/biss.3.35474)


## Relevant projects and initiatives  

* Atlas de la Biodiversidad de Costa Rica – CRBio
    * See [species pages](http://www.crbio.cr/crbio/?page_id=61&lang=en)
* Spanish Ministry for the Ecological transition, [Species Information System](https://www.miteco.gob.es/es/biodiversidad/servicios/banco-datos-naturaleza/Eidos_acceso.aspx)
    * [SPARQL Endpoint](https://crossnature.eu/visor/)
    * Underlying [ontology](https://datos.iepnb.es/def/sector-publico/medio-ambiente/pliniancore/)
    * [Ontology visualisation](http://www.visualdataweb.de/webvowl/#iri=https://datos.iepnb.es/def/sector-publico/medio-ambiente/pliniancore/3.0.0)
* Vasque Country (Spain) Official [Nature Information System](https://www.ivap.euskadi.eus/contenidos/ds_informes_estudios/plinian_core/eu_def/adjuntos/plinian.pdf)
    * [Specification](https://opendata.euskadi.eus/catalogo/-/txostenak-ikerketak/euskadiko-naturari-buruzko-informazio-sisteman-jasota-dauden-espezieak-deskribatzen-dituen-informazioa/) for creating DwC-Archives based on Plinian Core
* Colombian Biodiversity [Catalog](https://catalogo.biodiversidad.co/)
    * Documentation for [exotic](http://repository.humboldt.org.co/handle/20.500.11761/9691) and [threatened](http://repository.humboldt.org.co/handle/20.500.11761/9690) species
    * [Documentation](http://repository.humboldt.org.co/handle/20.500.11761/9689) about species pages editor
* Enciclovida, Mexican [species catalog](https://enciclovida.mx/)

