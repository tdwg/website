---
title: Environmental Samples and eDNA
description: >
  This group has been established to develop a data standard and usage guidelines for sharing environmental sample and environmental DNA data.
background:
  img: https://images.unsplash.com/photo-1508624217470-5ef0f947d8be
  by: Andrzej Kryszpiniuk
  href: https://unsplash.com/photos/4wFqHZ1ONnM
github: https://github.com/tdwg/gbwg/
toc: true
---

## Convener

- [Miwa Takahashi](mailto:miwa.takahashi@csiro.au) – Commonwealth Scientific and Industrial Research Organisation (CSIRO), Perth, Australia

## Core members

* [Kristy Deiner](mailto:alpinedna@gmail.com)
* [Chris Hunter](mailto:chris@gigasciencejournal.com)
* [Stefania Marcheggiani](mailto:stefania.marcheggiani@iss.it)
* [Joana Paupério](mailto:joanap@ebi.ac.uk)
* [Peter Woollard](mailto:woollard@ebi.ac.uk)
* [Luke Thompson](mailto:luke.thompson@noaa.gov) 
* [Katherine Silliman](mailto:ks567@msstate.edu) 
* [Steve Formel](mailto:steve@formeldataservices.com)
* [Camila Babo](mailto:camila.babo@cibio.up.pt)
* [Tobias Frøslev](mailto:tfroeslev@gbif.org)
* [Saara Suominen](mailto:s.suominen@unesco.org)

## Motivation

The need and willingness to publish research data, species occurrence records, and sequence data derived from environmental DNA (eDNA) has increased rapidly in the last few years. The routine monitoring of small organisms is becoming increasingly important in times of climatic and anthropogenic changes. Although GBIF, GGBN and GSC are providing solutions for different kinds of DNA-related data, the existing data standards need a substantial review and extension to fit current needs. To address these challenges, the FAIR eDNA (FAIRe) guidelines and checklist were developed and released in January 2025 ([https://fair-edna.github.io/index.html](https://fair-edna.github.io/index.html)). The FAIRe metadata checklist integrates terms from established standards such as DwC, the DNA-derived data extension to DwC, and MIxS, while introducing new terms to accommodate the specific requirements of eDNA data and workflow. Our goal is to review and refine the FAIRe checklist and incorporate relevant terms into the DwC suite, designed for adoption by major eDNA data platforms, including GBIF and OBIS. This will enhance FAIR data practices within eDNA communities, and facilitate the integration of eDNA-derived occurrence records with other biodiversity and environmental datasets. 

**Challenges**:

* number and complexity of relationships between and within samples
* number and complexity of relationships between and within sequences derived from samples
* diversity of use cases
* changes to taxonomy or identification associated to a given sequence
* amount of data associated to a single environmental sample
* potential complex history of preservation changes
* star schema and occurrence model limitations

**Gaps we would like to address in this group:**

High priority:

* providing metadata checklist to fully describe the source of eDNA derived sequences, species occurrences and lab data in general (e.g., sampling methods, extraction, sequencing and bioinformatics pipeline, primers, sequences, species annotation)
* relationships between and within samples and between sequences, including parent-child relationships (e.g. extend recommended vocabulary in relatedResourceClass) and sample-control associations (e.g., linking specific extraction negative control to batches of eDNA samples). 
* description of the sample and its preservation history (together with the Material Sample TG)
* how to relate different analysis results to same eDNA
* Integrating the FAIRe checklist terms into the DwC suite to address the above priority list. 

Medium priority:

* how to enable search for different sequences in different types of samples

In this task group we aim at consolidating the GGBN Data Standard, MIxS, the latest GBIF guide to publish DNA derived data, and the FAIRe checklist in order to develop a data standard and best practice usage guide for sharing environmental sample and eDNA data. In particular, the goal is to develop application schemas that can be used by repositories and data aggregators such as GBIF, OBIS, GGBN and INSDC.

To ensure the standard fulfills the needs of both the collection and research communities, we emphasise collaboration and co-developments with them throughout the process.

## Scope

* Organismal environmental (e.g. surface, water, ice, soil and air samples) and host-associated samples (e.g. gut, fecal, cheek, blood, wood)
* Agrobiodiversity and in-vitro samples
* Environmental DNA samples
* Community/bulk samples
* both recent and ancient material
* sequence data and species occurrence records derived from PCR detection such as qPCR
* species occurrence record with a “degree of uncertainty” (e.g., percentage identify match for species assignment) 
* Gathering event data, relationships between samples, lab data (extraction, sequencing pipeline, primers, sequences)
* Collaboration with other standard organisations (i.e., GSC) and stakeholders in the eDNA research and commercial sectors (i.e., service providers) to ensure alignment with their needs and ongoing efforts

## Goals, outputs, and outcomes

* Consider which granularity or resolution of data would be of interest
* Data standard for sharing eDNA data
* Application schemes for using the data standard with current ABCD and DwC models, or alternative application schemes (i.e., DwC-DP) if needed
* Example use cases for application of best practices
* Publication of proposed data standard, application schemes, and best practice guidelines

## Strategy

* Build on and consolidate previous work from within GBIF, GSC, eDNAqua-Plan, FAIRe initiatives, and GGBN
* Consult with related initiatives, working groups, and networks (e.g. biobank networks, permit working group, data aggregators, material sample working group)
* Consult with researchers and commercial sectors working with eDNA
* Joint, fortnightly meetings with members of the TG and the GSC eDNA project
* Regular reports to the GBWG Interest Group and Executive Committee

## Timeline

| Milestones and Deliverables | Due Month | Description | Remarks |
| :---- | :---- | :---- | :---- |
| M1 | Apr 2025 | Use cases and priorities defined |   |
| D1 | July 2025 | Definition of glossary terms done |   |
| M2 | Aug 2025 | Agreement on terms describing gathering event, description and storage of sample, relationships between samples | In parts dependent on other Task Groups: i) [MaterialSample](https://www.tdwg.org/community/osr/material-sample/), ii) Permits and Loans |
| D2 | Oct 2025 | Scenarios for granularity/resolution of data defined |   |
| M3 | July 2025 | Agreement on lab data terms |   |
| M4 | Oct 2025 | Agreement on how to deal with different levels of identifications (host vs. organisms found in sample) |   |
| D3 | Feb 2026 | Application scheme for current ABCD and DwC models (or alternative application schemes if needed) |   |
| D4 | Apr 2026 | Data standard, application schemes and best practice guide ready for submission |   |
	 
## Becoming involved

Interested parties are invited to watch and contribute to the [GitHub repository](https://github.com/tdwg/gbwg/) and participate in our calls. Please contact the convenor for more information. Also please subscribe to our [open mailing](http://lists.tdwg.org/mailman/listinfo/tdwg-gbwg) list to be informed about upcoming meetings and news.

## History and context

This Task Group will build on the work of GSC, GGBN and GBIF. Storage and study of human-associated samples has a long history. Organizations such as ISBER and ESBB came up with data standards too. GGBN is already partnering with both to enable exchange of knowledge. Many environmental specimen banks traditionally store samples for chemical, rather than molecular analysis. The FAIR eDNA (FAIRe) initiative has developed the FAIR guidelines and checklist specific to eDNA workflows and data. Members of the eDNA Task Group co-lead the MIxS-eDNA project under the GSC. We will get in touch with those communities to coordinate efforts. 

## Summary

This group has been established to develop a data standard and usage guidelines for sharing environmental DNA protocols and data. Although GBIF, GGBN and GSC are providing solutions for different kinds of DNA related data, the existing data standards need a substantial review and extension to fit current needs. This task group will work closely together with the Material Sample Task Group to review terms associated with physical samples. These data become more and more important for conservation, climate change, human health, ecology, monitoring and many other research approaches. The number of environmental sample and DNA collections has increased enormously in different communities. It is time to provide tools and guidance for researchers, industry, and collections on how to record and share such data.
