---
title: GBWG - Environmental Samples and eDNA
summary: This group has been established to develop a data standard and usage guidelines for sharing environmental sample and environmental DNA data.
cover_image: https://images.unsplash.com/photo-1606698235008-0b44ca6f7594
cover_image_by: David Clode
cover_image_ref: https://unsplash.com/photos/EyEdZ2aKRfA 
tags: task group
github: https://github.com/tdwg/gbwg/
---


# Environmental Samples and eDNA
** A Task Group of the Genomic Biodiversity Interest/Working Group (GBWG) **


________________


## Summary

This group has been established to develop a data standard and usage guidelines for sharing environmental sample and environmental DNA data. Although GBIF, GGBN and GSC are providing solutions for different kinds of DNA related data, the existing data standards need a substantial review and extension to fit current needs. This task group will work closely together with the Material Sample Task Group to review terms associated with physical samples. These data become more and more important for conservation, climate change, human health, ecology, monitoring and many other research approaches. The number of environmental sample and DNA collections has increased enormously in different communities. It is time to provide tools and guidance for researchers, industry, and collections on how to record and share such data.

## Convener

- Gabi Droege | GGBN/Botanic Garden and Botanical Museum Berlin | g.droege@bgbm.org | @gdadade

## Core members

* [Kristy Deiner](mailto:alpinedna@gmail.com)
* [Chris Hunter](mailto:chris@gigasciencejournal.com)
* [Stefania Marcheggiani](stefania.marcheggiani@iss.it)

## Motivation

The need and willingness to publish research and collection data of environmental samples and sequence data derived from environmental DNA has increased rapidly in the last few years. The routine monitoring of small organisms or organism parts is becoming increasingly  important in times of climatic and anthropogenic changes. Although GBIF, GGBN and GSC are providing solutions for different kinds of DNA related data, the existing data standards need a substantial review and extension to fit current needs.

Challenges:

* number and complexity of relationships between and within samples
* number and complexity of relationships between and within sequences derived from samples
* diversity of use cases
* changes to taxonomy or identification associated to a given sequence
* amount of data associated to a single environmental sample
* potential complex history of preservation changes 
* star schema and occurrence model limitations

Gaps we would like to address in this group:

High priority:

* relationships between and within samples and between sequences, including parent-child relationships (e.g. extend recommended vocabulary in relatedResourceClass)
* description of the sample and its preservation history (together with the Material Sample TG)
* how to enable search for different types of samples (controlled/recommended vocabulary)
* how to relate different analysis results to same eDNA

Medium priority:

* providing metadata and their source about sequences and lab data in general (extraction, sequencing pipeline, primers, sequences)
* how to enable search for different sequences in different types of samples

In this task group we aim at consolidating the GGBN Data Standard, MIxS as well as the latest GBIF guide to publish DNA derived data in order to develop a data standard and best practice usage guide for sharing environmental sample and eDNA data. In particular, the goal is to develop application schemas that can be used by aggregators such as GBIF, OBIS and GGBN.

In this context it will be important to fulfill the needs of both the collection and research communities.

## Scope

* Organismal environmental (e.g. surface, water, ice, soil and air samples) and host-associated samples (e.g. gut, fecal, cheek, blood, wood)
* Agrobiodiversity and in-vitro samples
* Environmental DNA samples
* Community/bulk samples
* both recent and ancient material
* sequence data and data derived from PCR detection such as qPCR
* Gathering event data, relationships between samples, lab data (extraction, sequencing pipeline, primers, sequences)

## Goals outputs and outcomes
* Definitions of glossary terms, such as “what is an environmental sample”
* Consider which granularity or resolution of data would be of interest
* Data standard for sharing environmental sample and eDNA data
* Application schemes for using the data standard with current ABCD and DwC models
* If needed alternative application schemes
* Example use cases for application of best practices
* Publication of proposed data standard, application schemes and best practice guidelines

## Strategy
* Build on and consolidate previous work from within GGBN, GBIF and GSC
* Consult with related initiatives, working groups and networks (e.g. biobank networks, permit working group, data aggregators, material sample working group)
* Consult with researchers and collections who work with environmental samples
* Regular reports to the GBWG Interest Group and Executive Committee

## Timeline

| Milestones and Deliverables| Due Month | Description | Remarks |
| M1 | 4 | Use cases and priorities defined |  |
| D1 | 6 | Definition of glossary terms done |  |
| M2 | 10 | Agreement on terms describing gathering event, description and storage of sample, relationships between samples | In parts dependent on other Task Groups: i) [MaterialSample](/community/osr/material-sample/), ii) Permits and Loans | 
| D2 | 12 | Scenarios for granularity/resolution of data defined |  | 
| M3 | 16 | Agreement on lab data terms |  | 
| M4 | 18 | Agreement on how to deal with different levels of identifications (host vs. organisms found in sample)|  |
| D3 | 20 | Application scheme for current ABCD and DwC models done |  | 
| D4 | 24 | Data standard, application schemes and best practice guide ready for submission |  | 
	 
## Becoming involved

Interested parties are invited to watch and contribute to the [GitHub repository](https://github.com/tdwg/gbwg/) and participate in our calls. Please contact the convenor for more information. Also please subscribe to our [open mailing](http://lists.tdwg.org/mailman/listinfo/tdwg-gbwg) list to be informed about upcoming meetings and news.

## History/context

This Task Group will build on the work of GSC, GGBN and GBIF. Storage and study of human-associated samples has a long history. Organizations such as ISBER and ESBB came up with data standards too. GGBN is already partnering with both to enable exchange of knowledge. Many environmental specimen banks traditionally store samples for chemical, rather than molecular analysis. This Task Group will get in touch with those communities as well.