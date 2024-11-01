---
title: Sensitive Species Extension
description: >
  A Task Group of the Darwin Core Maintenance Group
background:
  img: https://images.unsplash.com/photo-1658737320601-b10bcd2ca06d
  by: Tomás Evaristo
  href: https://unsplash.com/photos/a-close-up-of-a-sea-animal-MB1Ml14y90U
github: https://github.com/tdwg/sensitive-species-extension
toc: true
---

## Task Group Charter

**A Task Group of the Darwin Core Maintenance Group**


## Convenor

- [Cameron Slatyer](mailto:Cam.Slatyer@csiro.au) - _Atlas of Living Australia_

## Core Members

- Andrew Rodrigues - _GBIF, Global initiatives and implementation of DWC_
- Piers Higgs - _Gaia Resources, technical expertise_
- Tania Laity - _Atlas of Living Australia, data management and species expertise_
- John Wieczorek - _VertNet, Darwin Core Maintenance Interest Group_

## Motivation

The growth of biodiversity data aggregators and citizen science projects over the past two decades has led to an exponential expansion in the application of big data to conservation assessment and biodiversity research. Subsequently, expectations that biodiversity data should be made available have risen, as has the recognition of the challenges of both releasing and not releasing sensitive species data.

As biodiversity data has been democratised, the motivations of individuals, researchers, and organisations in restricting access to certain types of data have remained constant. Data producers and custodians may have a more conservative view of access than data consumers. Factors to be taken into consideration include type and level of threat, vulnerability, type of information, and public availability. Additionally, there is a growing recognition of the need to enable Indigenous peoples and local communities to assert data sovereignty over traditional knowledge and biodiversity data gathered by, about or within areas managed by them.

## History/Context

Two of the most recent attempts to deal with the overlapping issues in this space have been [Arthur Chapman's 2020 Current Best Practices for Generalizing Sensitive Species Occurrence Data](https://docs.gbif.org/sensitive-species-best-practices/master/en/), and development of a standardised [national framework for the Sharing of Restricted access species data in Australia](https://rasd.org.au/pdf-html/index.html).

Chapman proposed an extension to Darwin Core to capture information about how and why records for sensitive species have been generalised. GBIF have recently undertaken an analysis of how the current sensitive data fields in DWC are being applied and used and found that there is a lack of consistency and correct application.


## Goals Outputs and Outcomes

* An assessment of how the Sensitive Species extension relates to other TDWG standards
* Detailed documentation on sensitive species terms included in the extension
* Standard specification for submission to TDWG Executive by December 2025


## Strategy 

Create a GitHub repository for the task group to assure adoption of best practices for the development of TDWG standards and successful submission of final deliverables to the TDWG leadership and community for review. The repository configuration and function will follow existing TDWG practices.

- Call out for members and set up Task Group
- Review recommendations from the GBIF Sensitive Species Report 2023
- Review recommendations / principles form the Australian National Framework
- Review Chapman’s proposed extension considering the above and the discussion at the workshop at TDWG 2023
- Finalise a vocabulary for extension fields (where relevant) through community deliberation and consensus within the task group, the parent Species Information Interest Group, the DWC Maintenance Group and the wider TDWG community.
- The development of extensions will follow the process and expected deliverable of the TDWG Vocabulary Maintenance Specification (VMS, [https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md)). If a new standard is indicated, development will follow the TDWG Standards Documentation Standard (SDS, [https://github.com/tdwg/vocab/blob/master/sds/documentationspecification.md](https://github.com/tdwg/vocab/blob/master/sds/documentationspecification.md)) and will be reviewed as required by the [TDWG By-laws](https://www.tdwg.org/about/process/) for the ratification of standards.
- Throughout the process we will work closely with the Darwin Core Maintenance Interest Group and the Species Information Interest Group, some members of whom are also members of this Task Group, and who have experience with the development and incorporation of extensions.
- We will also engage experts to aid with the revision of term definitions as necessary.
- We will work closely with GBIF staff to coordinate wider implementation and use of Sensitive Species extension.
- All development will be done and progress tracked in the Sensitive Species GitHub repository from TDWG GitHub organization.


## Becoming Involved

* individuals having an interest in this work should contact the convener and are invited to watch and contribute via the Sensitive Species Extension GitHub Repository (https://github.com/tdwg/sensitive-species-extension).
* Please join the mailing list to contact the group https://lists.tdwg.org/mailman/listinfo/dwc-sensitive-species


## Summary

This Task Group will explore concepts and methods of sensitive species data generalisation to fully integrate this type of data into existing data exchange schemas. The extension attributes proposed by [Chapman (2020)](https://docs.gbif.org/sensitive-species-best-practices/master/en/) will be reviewed, revised as necessary and integrated into an extension to Darwin Core. The outcome of this Task Group will be  to provide a framework and clear semantics for generalising and sharing sensitive species data.


## Resources

* [Chapman AD (2020) Current Best Practices for Generalizing Sensitive Species Occurrence Data. Copenhagen: GBIF Secretariat. https://doi.org/10.15468/doc-5jp4-5g10.](https://docs.gbif.org/sensitive-species-best-practices/master/en/).
* [National Framework for the Sharing of Restricted Access Species Data in Australia 2023, Atlas of Living Australia, Publication Series No. 6, Canberra, Australia. https://doi.org/10.54102/ala.94894.](https://rasd.org.au/pdf-html/index.html)
* TDWG 2023 Workshop Abstract- [WKSH03 Handling restricted access data in an open data landscape](https://www.tdwg.org/conferences/2023/session-list/#wksh03).
