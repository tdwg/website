---
title: Realm and Biome
description: >
  A task group of the Darwin Core maintenance group working on vocabularies to describe the ecological context of a sampling or observing event.
background:
  img: https://images.unsplash.com/photo-1580380853761-76b20197ef99
  by: USGS
  href: https://unsplash.com/photos/rXj2M7xtdB8
github: https://github.com/tdwg/dwc-realm-biome-tg
toc: true
---


# Realm and Biome Charter </br >
A Task Group of the Darwin Core Maintenance Group


## Convenor

  - Cecilie Svenningsen – Global Biodiversity Information Facility (GBIF) Secretariat 

## Core Members

  - Kate Ingenloff – Global Biodiversity Information Facility (GBIF) Secretariat
  - John Wieczorek – providing support for the process of Vocabulary enhancements as the Darwin Core convenor. 
  - Pier Luigi Buttigieg – Alfred Wegener Institute \- Board member of the GSC, Chief editor of the Environment Ontology (ENVO), Chair of IOC-UNESCO’s Ocean Data and Information System 

## Motivation 

Species occurrence data, in its most basic form, provides essential details about the species observed, including names, dates, and geographic location of observations. While geographic information captures the location, metadata about the ecological context of the observation site can offer invaluable insights for users in their downstream analysis. 

Three terms are currently available to capture habitat information associated with species occurrences: Darwin Core’s [habitat](https://dwc.tdwg.org/terms/#dwc:habitat) and [targetHabitatScope](http://rs.tdwg.org/eco/terms/targetHabitatScope) and [excludedHabitatScope](http://rs.tdwg.org/eco/terms/excludedHabitatScope) in [Humboldt extension for ecological inventories](https://eco.tdwg.org/). Two additional terms, [env_broad_scale](https://w3id.org/mixs/0000012) and [env_local_scale](https://w3id.org/mixs/0000013), in the DNA-derived data GBIF extension (adapted from the Minimum Information about any (x) Sequence (MIxS) standard), capture system-level environmental information implementing the Environment Ontology ([ENVO](http://purl.obolibrary.org/obo/ENVO_00000428)) as a controlled vocabulary. However, none of the existing cores or extensions includes a term that provides a means to report the broader categories of realm and [biome](https://github.com/tdwg/dwc/issues/38) to describe sampling sites. It is also currently not possible to report which [environmental material](https://github.com/tdwg/dwc/issues/40) surrounds the sample at the time of sampling, except in the context of a DNA-derived sample for which the term [env_medium](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#env_medium) from the [DNA-derived data extension](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2024-04-17.xml) can be applied. Adding the terms *biome*, *realm*, and *environmentalMaterial* to DwC will give data publishers and data users methods of broadly considering the biogeography of available data from a climatic (biome) and a geographic (realm) perspective and the medium in which a sample was collected (*environmentalMaterial*). 

This task group aims to integrate the terms *realm*, *biome*, and *environmentalMaterial* with controlled vocabularies into the Darwin Core standard in the Event class. Enriching the environmental context of biodiversity data by including these terms with associated controlled vocabularies can enhance data curation and provide biodiversity data users with deeper analytical capabilities. 

## Goals Outputs and Outcomes

The main goal of the task group will be to propose another new term, *realm*, to the Darwin Core standard and evaluate the proposal of two other terms, *biome* and *environmentalMaterial*, including the possibility of implementing controlled vocabularies for all terms. The primary deliverables will be: 

  - A review of the appropriateness of ENVO, IUCN, or other sources for deriving a controlled vocabulary for proposed terms *realm* and *biome*.
    - Potentially include use cases to examine which resource best covers user needs 
  - An assessment of how the inclusion of the terms relates to other TDWG standards, including the Latimer Core standard, which currently includes the terms [ltc:biogeographicRealm](https://ltc.tdwg.org/terms/#ltc_biogeographicRealm), [ltc:biome](https://ltc.tdwg.org/terms/#ltc_biome) and [ltc:material](https://ltc.tdwg.org/terms/#ObjectGroup_material). 
  - A proposal to extend the Darwin Core standard to include *realm* and potentially *biome* and *environmentalMaterial* as terms with associated controlled vocabularies. This includes 
    - a formal definition of the term *realm* following the Darwin Core Term proposal template. 
    - a formal definition of the term *biome* following the Darwin Core Term proposal template. 
    - a formal definition of the term *environmentalMaterial* following the Darwin Core Term proposal template. 
    - formal definitions of the controlled vocabularies and their concepts following the Vocabulary Maintenance Standard. 
    - updates to the relevant GBIF schemas ([Event](https://rs.gbif.org/core/dwc_event_2024-02-19.xml), [Occurrence](https://rs.gbif.org/core/dwc_occurrence_2024-02-23.xml), [DNA-derived data](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2024-04-17.xml)) used to publish Darwin Core Archives. 

## Strategy

The task group deliverables will be maintained in a [GitHub repository](https://github.com/tdwg/dwc-realm-biome-tg) and communication will be conducted via [email](https://lists.tdwg.org/postorius/lists/dwc-realm-biome.lists.tdwg.org/). The task group will work closely with the Darwin Core Maintenance Group and the Genomics Standards Consortium to coordinate changes that may affect both standards.  

## Becoming Involved

Motivated individuals with the following skills and knowledge are encouraged to join the task group: 
  - Data holders with information on realms, biomes, and environmental material (for use in the development of any potential use cases) 
  - Data users who can help scope the need for specific values in the proposed terms - Specialists with an ecology background 
  - Individuals with knowledge of potential resources that can support the development of a controlled vocabulary for the terms 

Individuals interested in contributing to the task group should contact the convenor and are invited to participate in the [GitHub repository](https://github.com/tdwg/dwc-realm-biome-tg) for the task group. 

Please join the [mailing list](https://lists.tdwg.org/postorius/lists/dwc-realm-biome.lists.tdwg.org/) to receive news about the task group work. 

## History/Context

Proposals to include the [biome](https://github.com/tdwg/dwc/issues/38) and [environmentalMaterial](https://github.com/tdwg/dwc/issues/40) terms in the Darwin Core Standard have been open on the DwC GitHub repository since 2014, with the conclusion that a task group is needed to resolve the remaining issues. 

[ENVO](http://purl.obolibrary.org/obo/ENVO_00000428) was initially proposed as an ontology for a *biome* term. More recently, however, the [IUCN Global Ecosystem Typology](https://global-ecosystems.org/explore) superseded that recommendation and the suggestion that the addition of two new terms, *biome* and *realm*, be considered. 

## Summary

The motivation is to improve the Darwin Core standard to increase the accessibility of metadata related to survey sites. In support of this goal, this task group is established to define three potential new Darwin Core terms, *realm*, *biome*, and *environmentalMaterial*, and controlled vocabularies for each of these. 

## Resources
  - GitHub issue for the [proposed *biome* term](https://github.com/tdwg/dwc/issues/38) 
  - GitHub issue for the [proposed *environmentalMaterial* term](https://github.com/tdwg/dwc/issues/40) 
  - [Humboldt extension for ecological inventories](https://rs.gbif.org/extension/eco/Humboldt_2024-04-16.xml) 
  - [DNA-derived data extension](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2024-04-17.xml) 
  - [IUCN Global Ecosystem Typology](https://global-ecosystems.org/explore) 
  - [ENVO proposed source](http://purl.obolibrary.org/obo/ENVO_00000428) for the biome term

