---
title: Best practices for development of vocabularies of values ("Vocabularies")
summary: The Vocabularies Task Group (TG4) of the Biodiversity Data Quality Interest Group is exploring the approaches and technologies TDWG might use to manage vocabularies of data terms and values.
cover_image: 
cover_image_by: 
cover_image_ref: 
tags: task group
github: https://github.com/tdwg/bdq/tree/master/tg4
---

The detailed goals and expected outcomes for the Vocabularies Task Group (TG4), as well as the steps to produce them are described here.

## Convenor
[Paula Zermoglio](pzermoglio@gmail.com)

## Motivation

Biodiversity data are increasingly being shared from myriad sources. While the Darwin Core standard defines a set of terms under which data are organized and shared, it does not refer to the actual values used to describe the content of each field. More often than not, distinct sources utilize diverse criteria to populate the fields. While this has allowed data publication broadly, when it comes to data usage, it becomes apparent that such heterogeneity hinders discoverability and use of the data. One way to reduce this variability and improve data use is to provide standardized vocabularies for the community to use. Vocabularies exist for some terms, but are constrained to specific groups or disciplines. Furthermore, there is no best practice defined for the creation of biodiversity data vocabularies for the values captured under Darwin Core terms (hereafter vocabularies-of-values), and no recommended environment in which to do so. This TG aims to create such a framework under the TDWG umbrella, with the ultimate objective of building a corpus of vocabularies of standard values for terms. We identify four target audiences who could potentially benefit from the outcomes of this TG: 1) Data producers (i.e., data collectors) who could capture data using the controlled vocabularies through pick lists and could impart valuable information more efficiently; 2) Data custodians (e.g., staff in museum collections) who could manage, provide and use data more efficiently; 3) Data aggregators who could use the vocabularies to provide infrastructure for data filtering; 4) Data users for whom more effective filtering would represent improvement in data fitness for use.
Currently, other initiatives concerning biodiversity data vocabularies-of-values are scattered, and no other TDWG task group is addressing the issue of the structure of such standards. As this TG is directly related with data quality and use, the Data Quality Interest Group seems the appropriate environment for this work.


## Goals, outputs and outcomes

**1. Preparation of a Scoping Document.** The document will include the following topics:
    - Determining what types of vocabularies would be needed for TDWG – consistent with the various ISO Standards on Vocabularies (i.e., do we require vocabularies, dictionaries of terms, controlled vocabularies, thesauri, ontologies, etc.), and whether vocabularies should be mono-lingual or multi-lingual.
    - Determining a strategy for organizing the construction of vocabularies, considering: A) structuring of work within TDWG, with the following options: 1) the creation of a separate Interest group; 2) the creation of several Task Groups within the Data Quality Interest Group, or associated to other TDWG Interest Groups; B) Domain specific needs and practices.
  
**2. Development of a common repository for TDWG vocabularies-of-values.** GitHub will be the first option but other alternatives will be explored to provide a user-friendly platform for gathering and developing vocabularies. Exploration of alternative platform is expected.

**3. Development of a current best practice for the building of TDWG vocabularies.** Such format will be based primarily on the TDWG Standards Documentation Specification.

**4. Building of at least one exemplary vocabulary** under the standard format developed in item 3.

**5. Collection and assessment of already existing vocabularies** across the community that can be used as are, or that can be modified for TDWG purposes. The list of such vocabularies will be made available through the common repository.

**6. Identification of domain-specific groups** that may be involved in the preparation of vocabularies and creation of a list of contacts that will be available through the GitHub repository.

**7. In-depth evaluation of the current state** of data that is shared through aggregators in relation to the use of controlled values for each Darwin Core term. A report will be built.

**8. Preparation of a list of vocabularies needed** for terms of the Darwin Core standard based on the previous report.

## Strategy

### General

- The convener and the core members of the group will produce the reports and documentation outputs in collaboration with any other interested parties.
- Discussion and general work will be performed via periodic meetings that will be held remotely and in person in appropriate venues (e.g., TDWG 2018, 2019, DQIG meetings).
- All activities will be tracked in the common repository in GitHub (item 2), which will be created either as an independent repository or under the existing Interest Group repository (https://github.com/tdwg/bdq), as a first activity. All materials produced will be available in that repository as well.
### Specifics
- The scoping document, the current best practice for building vocabularies-of-values, the exemplary vocabulary and the list of vocabularies needed (items 1, 3, 4 and 8) will be created by the members of the TG, using either GitHub directly or other platforms such as Google Documents for early stages.
- The scoping document, the current best practice and the exemplary vocabulary (items 1, 3 and 4) will be presented at TDWG/SPNCH 2018 Meeting. This will be a special opportunity to integrate the initiative with the broader community and to identify and engage with individuals and domain-specific groups that might be interested in the construction of the vocabularies.
- We will explore the possibility of creating a user-friendly repository (item 2) for building and storing TDWG vocabularies. We will also evaluate the cost-benefits and provide a report/proposal for the construction of a platform.
- The gathering of existing vocabularies (item 5) will be based on a preliminary list made by the convener and already available at https://docs.google.com/spreadsheets/d/1SDbtZxEzg0t10OSNDPJN0XSye6mMOTTCIBH3xh-HUYA/edit#gid=0. A more extensive search will be conducted and key stakeholders (e.g., aggregators, database management systems, data providers from natural history collections) will be personally contacted via email and invited to share vocabularies in use.
- As before, domain-specific groups will be identified and contacted via email and personally in appropriate meetings (e.g., TDWG/SPNCH 2018) (item 6).
- If further in-person interaction is needed among the members of the TG and/or with other members of the community or domain-specific groups, we will seek funding opportunities through different agencies outside TDWG.
- Evaluation of the current state of data (item 7) will be carried out mainly by the convener based on previous research conducted on data from GBIF, iDigBio and VertNet, already available through a data directory in the Darwin Core Questions & Answers GitHub site (https://github.com/tdwg/dwc-qa/tree/master/data).

### Timeline (tentative)

![timeline](https://drive.google.com/uc?export=download&id=0B4sIKK7qrRVITFhGb3I0Qld5Q28)

## Becoming involved

Achieving the goals of this TG will require the interaction of people from several areas within the community. Main areas of knowledge needed are: standards in general and Darwin Core in particular, vocabularies, domain-specific needs both from the data provider and data user perspectives. Therefore, it will be useful to have members from all these different areas of expertise. 
Each of the proposed goals of this TG are distinct enough to allow members of the community to participate in one or more of them without requiring full knowledge of all the topics addressed. We hope this will promote broader participation.

## Resources

- Standards Documentation Specification, (particularly section 4.5.4 of  <https://github.com/tdwg/vocab/blob/master/documentation-specification.md>).
- Preliminary collection and assessment of already existing vocabularies across the community (<https://docs.google.com/spreadsheets/d/1SDbtZxEzg0t10OSNDPJN0XSye6mMOTTCIBH3xh-HUYA/edit#gid=0>).
- ANSI/NISO Z39.19-2005 (R2010) — Guidelines for the construction, format, and management of monolingual controlled vocabularies, National Information Standards Organization (US). (<http://www.niso.org/apps/group_public/download.php/12591/z39-19-2005r2010.pdf>).
- ISO Standard for thesauri, ISO25964, (<https://en.wikipedia.org/wiki/ISO_25964>).
- ISO 25964-1:2011 Information and documentation -- Thesauri and interoperability with other vocabularies -- Part 1: Thesauri for information retrieval (<https://www.iso.org/standard/53657.html>).
- ISO 25964-2:2013 Information and documentation -- Thesauri and interoperability with other vocabularies -- Part 2: Interoperability with other vocabularies (<https://www.iso.org/standard/53658.html>).
- TDWG Vocabulary Maintenance Specification Task Group (<https://github.com/tdwg/vocab>).
- Distinct Value lists (<https://github.com/tdwg/dwc-qa/tree/master/data>).
- TDWG Data Quality mailing list (<http://lists.tdwg.org/mailman/listinfo/tdwg-bdq>).
- Ontobee (<http://www.ontobee.org/>).
- Research Data Alliance (RDA) Vocabulary Services Interest Group Charter Proposal. (<https://www.rd-alliance.org/group/vocabulary-services-interest-group/case-statement/vocabulary-services-interest-groups.html>).
