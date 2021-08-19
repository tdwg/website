---
title: People in Biodiversity Data
summary: 
cover_image: https://images.unsplash.com/photo-1580407196238-dac33f57c410
cover_image_by: Wolfgang Hasselman
cover_image_ref: https://unsplash.com/photos/6JZJyHXQ-p0https://unsplash.com/photos/6JZJyHXQ-p0
tags: task group
github: https://github.com/tdwg/attribution/tree/master/people/dwc
status: published
---


# People in Biodiversity Data

Task Group Charter
(Under TDWG Attribution Interest Group)

Submitted: January 13, 2020

Last Updated: May 18, 2020

# Conveners

[David Shorthouse](mailto:david.shorthouse@canada.ca) (Agriculture and Agri-Food Canada, Canada)  
[Quentin Groom](mailto:quentin.groom@plantentuinmeise.be) (Meise Botanic Garden, Belgium)  
[Elspeth M. Haston](mailto:E.Haston@rbge.org.uk) (Royal Botanic Garden Edinburgh, United Kingdom)     
[Anne Thessen](mailto:annethessen@gmail.com) (Oregon State University, USA)

# Member List
  
[Anton Güntsch](mailto:a.guentsch@bgbm.org) (Freie Universität Berlin, Germany)  
[Chloé Besombes](mailto:chloe.besombes@mnhn.fr) (National Museum of Natural History, Paris, France)  
[Dominik Röpert](mailto:d.roepert@bgbm.org) (Botanic Garden and Botanical Museum Berlin)  
[Frederik Berger](mailto:frederik.berger@mfn.berlin) (Museum of Natural Science, Berlin, Germany)  
[Iris Sampaio](mailto:irisfs@gmail.com) (University of the Azores / Senckenberg am Meer)  
[Jiri Frank](mailto:jiri_frank@nm.cz) (National Museum, Prague, Czech Republic)  
[Sharif Islam](mailto:sharif.islam@naturalis.nl) (Naturalis, Netherlands)  
[Jonathan Krieger](mailto:j.krieger@kew.org) (Royal Botanic Gardens, Kew, UK)  
[Nicky Nicolson](mailto:n.nicolson@kew.org) (Royal Botanic Gardens, Kew, UK)  
[Nicole Kearney](mailto:nkearney@museum.vic.gov.au) (Biodiversity Heritage Library, Australia)  
[Paul Braun](mailto:Paul.Braun@mnhn.lu) (National Museum of Natural History, Luxembourg)  
[Robert Cubey](mailto:r.cubey@rbge.org.uk) (Royal Botanic Garden Edinburgh, UK)  
[Ronald Canepa](mailto:rcanepa@acis.ufl.edu) (iDigBio, University of Florida, USA)  
[Rod Page](mailto:Roderic.Page@glasgow.ac.uk) (Glasgow University)  
[Sarah Phillips](mailto:Sarah.Phillips@kew.org) (Royal Botanic Gardens, Kew, UK)  
[Simon Chagnoux](mailto:simon.chagnoux@mnhn.fr) (National Museum of Natural History, Paris, France)  
[Deborah L Paul](mailto:dlpaul@illinois.edu) (Illinois Natural History Survey, Champaign-Urbana, Illinois, USA)  
[Mathias Dillen](mailto:mathias.dillen@plantentuinmeise.be) (Meise Botanic Garden, Belgium)

# Current Activities

Two terms have been created under the GBIF namespace for use in the exchange of identifiers for people in occurrence data. These are **recordedByID** and **identifiedByID** and are available in the core Darwin Core Occurrence extension of GBIF's Integrated Publishing Toolkit. They are defined as follows:

**recordedByID** | <!-- -->
--- | ---
Definition | An unordered list (concatenated and separated) of IDs representing names of people, groups, or organizations responsible for recording the original Occurrence. No semantics should be assumed, including for example an ordering of identifiers to indicate a primary collector or any institutional affiliation. The recommended best practice is to separate the values with a vertical bar (`|`).
Examples | `https://orcid.org/0000-0001-6215-3617 | https://orcid.org/0000-0003-1691-239X` `https://orcid.org/0000-0001-6215-3617 | https://www.wikidata.org/entity/Q28913658`
Qualname | <http://rs.gbif.org/terms/1.0/recordedByID>


**identifiedByID** | <!-- -->
--- | ---
Definition | An unordered list (concatenated and separated) of IDs representing names of people, groups, or organizations who assigned the Taxon to the subject. No semantics should be assumed, including for example an ordering of identifiers to citation priority or any institutional affiliation. The recommended best practice is to separate the values with a vertical bar (`|`).
Examples | `https://orcid.org/0000-0001-6215-3617 | https://orcid.org/0000-0003-1691-239X` `https://orcid.org/0000-0001-6215-3617 | https://www.wikidata.org/entity/Q28913658`
Qualname | <http://rs.gbif.org/terms/1.0/identifiedByID>

Members of this group are developing an extension to Darwin Core entitled, [Agent Actions](https://github.com/tdwg/attribution/tree/master/people/dwc). This extension accommodates the [theoretical work](http://doi.org/10.5334/dsj-2019-054) produced in collaboration with the Research Data Alliance.


# Motivation

* Unique identifiers for people are needed to connect entities in biodiversity research. These entities include publications, specimens, molecular sequences, taxonomic names and concepts, projects, code, workflows, and observations
* We can use organizations and/or projects like ISNI, ORCID, and Wikidata that are stable and their resolution services are expected to be maintained in perpetuity
* ORCID IDs are rapidly being adopted in scholarly publication for person identification. Wikidata is linking taxonomic names to people identifiers and iNaturalist allows ORCID IDs to identify observers. Specimen data are lagging behind, even though there is a clear need
* Researchers and collection managers desire a credit system that acknowledges their efforts in depositing and curating specimens
* Citizen scientists desire a way to track the impact of their efforts
* Collections management systems often model people as Agents but few accommodate external identifiers, none have a mechanism to unambiguously share attribution data
* Research is underway in how to best extract, reconcile, and resolve people names in occurrence data and publications and we understand that this will encourage focused coordination and will reduce duplication of effort in digitization programs (Nicolson & Tucker, 2019; Nicolson et al. 2018)
* We have a published model developed under both the Research Data Alliance and Biodiversity Information Standards that may be used as guiding principles in sharing attribution data (Thessen et. al. 2019)
History and Background

Many of the participants of the Task Group have worked on people identifiers and person data. We consider that it is time for these initiatives to be brought together under a task group to create common standards, common approaches and best practices.

In March 2019 under the aegis of the Mobilise COST Action a workshop was run on the subject of “Authority Management of People Names” [https://osf.io/qwegk/](https://osf.io/qwegk/). This workshop developed a number of actions and these were progressed at a pre-conference workshop at the Biodiversity Next Conference in October 2019. At the workshop the participants worked on visualization, disambiguation, engagement and dissemination of people identifiers for collections [https://osf.io/9t3f2/](https://osf.io/9t3f2/).

# Goals

1. Determine whether Darwin Core must be amended & subsequently ratified to accommodate more granular representations of our information held in terms like recordedBy, identifiedBy, georeferencedBy, measurementDeterminedBy
2. Establish a draft Darwin Core extension for attribution with feedback from users
   1. Establish a vocabulary of actions whose URIs are tied to [VIVO](https://wiki.duraspace.org/display/VIVODOC110x/Ontology+Reference) [^1] (coordinated with Anne Thessen)
   2. Develop definitions in multiple languages for terms in the action vocabulary
   3. Reconcile the extension with existing extensions and how they record agents and their actions
   4. Pilot the implementation of the extension with 2-3 museums and herbaria that serve data through the Integrated Publishing Toolkit (IPT)
   5. Serve the extension from GBIF’s registry of extensions
3. Advocate and proselytize on the use of globally unique identifiers for agents and their actions in collections and other related initiatives. For example, in collection management systems.
4. Develop a 3-4 page rationale with costs and benefits for seeking formal TDWG/GBIF membership with ORCID and/or ISNI [International Standard Name Identifier] (ISNI and ORCID work together but don’t cover the same groups of people; ORCID for living, ISNI for dead). Audience: GBIF heads of delegations, governing board
5. Make a best practice guide to the disambiguation of people’s names written on specimens.
6. Identify areas of overlap with other Interest Groups in TDWG
   1. Make recommendations to improve workflows eg Data Quality Interest Group

# Methods

The Task Group will use online means to communicate and document its work. Members have already had various ad hoc online meetings and these will continue. The Group also uses the Open Science Framework to store documents and will use tools such as Google Docs to work collaboratively. The Task Group will seek opportunities to meet face-to-face. Obvious venues are at the annual meetings of TDWG and SPNHC, but members may also have chances to meet at the RDA conferences and at regional meetings. If funding or other resources are needed, we will look for support from various projects, including DiSSCo, ALA and iDigBio. We will also reach out to developers of collection management systems to make them aware of our work.

Ultimately, the Task Group will submit its proposals to TDWG’s journal BISS and follow the TDWG Vocabulary Maintenance Standard to get these proposals adopted.

# Summary

People are an important element in the biodiversity knowledge graph. If we are able to identify people uniquely we will be able to connect entities in the graph, such as specimens, literature, sequence and taxon names. We propose to create a task group that will resolve outstanding problems with standards related to people’s names. This task group will also promote the use of people identifiers with scientists and infrastructures to ensure widespread adoption and usage in research. We will conduct this work globally and seek input from all the relevant actors in this field. Considerable work has already been done towards the goals of this task group, however we feel it is important to form an official group to gain legitimacy, facilitate wider adoption and connect with stakeholders outside our networks.

# Resources

[RDA/TDWG Attribution Metadata Working Group: Final Recommendations](https://www.rd-alliance.org/group/rda-tdwg-metadata-standards-attribution-physical-and-digital-collections-stewardship/outcomes)

# Literature

Groom, Q.J., C. O’Reilly, and T. Humphrey. 2014. Herbarium specimens reveal the exchange network of British and Irish botanists, 1856–1932. New Journal of Botany 4: 95–103. <https://doi.org/10.1179/2042349714Y.0000000041>

Lindon, H. L., Gardiner, L. M., Brady, A., & Vorontsova, M. S. (2015). Fewer than three percent of land plant species named by women: Author gender over 260 years. Taxon, 64(2), 209-215.

Penn, M.G., S. Cafferty, and M. Carine. 2017. Mapping the history of botanical collectors: spatial patterns, diversity, and uniqueness through time. Systematics and Biodiversity 16: 1–13. <https://doi.org/10.1080/14772000.2017.1355854>

Nicolson, N., A. Paton, S. Phillips, and A. Tucker. 2018. Specimens as Research Objects: Reconciliation Across Distributed Repositories to Enable Metadata Propagation. 2018 IEEE 14th International Conference on e-Science (e-Science). <https://doi.org/10.1109/eScience.2018.00028>

Nicolson, N., and A. Tucker. 2017. Identifying Novel Features from Specimen Data for the Prediction of Valuable Collection Trips. Lecture Notes in Computer Science 235–246. <https://doi.org/10.1007/978-3-319-68765-0_20>

Thessen, A.E., Woodburn, M., Koureas, D., Paul, D., Conlon, M., Shorthouse, D.P. and Ramdeen, S., 2019. Proper Attribution for Curation and Maintenance of Research Collections: Metadata Recommendations of the RDA/TDWG Working Group. Data Science Journal, 18(1), p.54. <http://doi.org/10.5334/dsj-2019-054>

[^1]: VIVO is member-supported, open source software and an ontology for representing scholarship.
