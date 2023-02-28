---
title: Invasive Organism Information
description: >
  This group is being implemented to make specific changes to Darwin Core and its vocabularies with the intention of improving it for use in research and management concerning biological invasions. To facilitate the management and reduce the impact of invasive species monitoring and impact assessment should be conducted regularly. However, these assessments are difficult to automate because the source data lack common formats and standards. Improved interoperability would allow the creation of repeatable workflows for rapid processing. A similar situation exists for the assessment of conservation statuses for Red Lists. Again, the lack of machine readable resources and inadequate standards prevents automation of the process. Ideally, such assessments could be run regularly or as soon as new data becomes available.
background:
  img: https://images.unsplash.com/photo-1510554093911-4c279430ae5d
  by: David Clode
  href: https://unsplash.com/photos/eCPYx-GBx_I
toc: true
---

## Convenor

- [Quentin Groom](mailto:quentin.groom@plantentuinmeise.be) - Meise Botanic Garden

## Core members

- Steve Baskauf (technical advice on vocabulary specification)
- Peter Desmet (technical advice, interoperability and workflows)
- Melodie McGeoch (invasive species expertise)
- Shyama Pagad (invasive species expertise)
- Ramona Walls (BCO and other ontologies)
- John Wilson (invasive species expertise)
- Dmitry S. Schigel - GBIF
- Paula Zermoglio - Darwin Core

Ex-officio members from the [Biodiversity Data Quality IG](/community/bdq/):

- Arthur Chapman
- Antonio Saraiva

## News

The Task Group has published its proposals in the journal Biodiversity Information Science and Standards. These proposals are now open for public comment. When this period is over they will be presented to the Executive Committee for final approval.

> Groom Q, Desmet P, Reyserhove L, Adriaens T, Oldoni D, Vanderhoeven S, Baskauf SJ, Chapman A, McGeoch M, Walls R, Wieczorek J, Wilson JR.U, Zermoglio PFF, Simpson A (2019) Improving Darwin Core for research and management of alien species. Biodiversity Information Science and Standards 3: e38084. <https://doi.org/10.3897/biss.3.38084>

## Motivation

Many reasons are driving our need to understand the dynamics of living systems. These reasons include the problems of invasive species and emerging wildlife disease, but also population shifts driven by climate and other environmental changes. Determining risks, impacts and providing early warnings of change make particular requirements on the quality of biodiversity observation data. For example, it is necessary to know where taxa occur and where they are native. We need to know the anthropogenic dispersal vectors and routes, and we need to know how well established they are in their locations.

The [GBIF Task Group on Data fitness for use in research on Alien and Invasive species](http://www.gbif.org/resource/82958) made five priority recommendations, one of which was the enhancement, development and adoption of relevant data standards and a second was the improvement of data and information essential to alien and invasive species research. This TDWG task group will help to address these priorities from the perspective of biodiversity standards, particularly for observations and checklists of alien species, but also ancillary data on all biota.

This task is timely because it will build on the work of the Vocabulary Maintenance Specification Task Group by establishing standard controlled vocabularies for fields. Also, because it follow on from the GBIF Task Group mentioned above.

## Goals outputs and outcomes

- To propose a controlled vocabulary for dwc:establishmentMeans conforming to the Vocabulary Maintenance Specification.
- To propose a controlled vocabulary for dwc:occurrenceStatus conforming to the Vocabulary Maintenance Specification.
- To propose a new term and vocabulary for Darwin Core to express whether a taxon has either been introduced by human activity or occurs naturally in a location.
- To propose a new term and vocabulary for Darwin Core to indicate the degree to which an organism has established a sustainable population in a locality.
- At least three demonstration datasets where these terms and vocabularies are implemented. These datasets can be developed in parallel with agreement of the terms and vocabularies as they can be used to test the concepts.
- A report on the proposed new terms and vocabularies with guidance on how they should be used. This report depends on agreement of the above terms and vocabularies.

## Strategy

- The outputs will be produced by the convener and core members in consultation with any other interested parties.
- Information on the group’s deliverables will be maintained on GitHub.
- Meetings will be conducted online, with communications via email. Physical meetings will be held at the TDWG Annual Conference in Ottawa.
- We will present an outline of the proposal at the TDWG 2017 meeting in October 2017. We will use that meeting as an opportunity to resolve any issues.

## Becoming involved

This group needs skills and knowledge related to invasive species research, but also Darwin Core and machine readable vocabularies. It will also be useful to have members with experience of using Darwin Core data, such as publishing to GBIF. These changes will be used by the whole biological community so an appreciation of the needs of other communities is important.

## History and context

This Task Group will build on the work of the GBIF Task Group on Data fitness for use in Research on Alien and Invasive species and the Data standardisation and harmonisation working group of the Alien Challenge COST Action in Europe. Due to these groups much of the groundwork for this proposal has been achieved.

## Resources

Links to the resources used and promoted by the group - Wiki, tutorials, presentations, mailing list, repository.

Proposal pages on GitHub:

- <https://github.com/qgroom/ias-dwc-proposal>
- <https://github.com/qgroom/ias-dwc-proposal/blob/master/Darwin%20Core%20proposals%20to%20support%20alien%20species%20research%20(1).pdf>

## Relevant papers

- Blackburn TM, Pyšek P, Bacher S, Carlton JT, Duncan RP, Jarošík V, Wilson JRU, & Richardson DM (2011). A proposed unified framework for biological invasions. Trends in ecology & evolution, 26(7): 333-339. <https://doi.org/10.1016/j.tree.2011.03.023>
- Groom Q, Adriaens T, Desmet P, Simpson A, De Wever A, Bazos I, Cardoso AC, et al. "Seven recommendations to make your alien species data more useful." Frontiers in Applied Mathematics and Statistics 3 (2017): 13. <https://doi.org/10.3389/fams.2017.00013>
- Hulme PE, Bacher S, Kenis M, Klotz S, Kühn I, Minchin D, ... & Pyšek P (2008) Grasping at the routes of biological invasions: a framework for integrating pathways into policy, Journal of Applied Ecology, 45: 403–414. <https://doi.org/10.1111/j.1365-2664.2007.01442.x>
- Latombe G, Pyšek P, Jeschke JM, Blackburn TM, Bacher S, Capinha C, Costello MJ, Fernández M, Gregory RD, Hobern D, Hui C, Jetz W, Kumschick S, McGrannachan C, Pergl J, Roy HE, Scalera R, Squires ZE, McGeoch MA, Groom QJ, Pagad S, Petrosyan V, Ruiz G & Wilson J (2016) Data fitness for use in research on alien and invasive species. Copenhagen: GBIF Secretariat. Available online at: <http://www.gbif.org/resource/82958>
- Robinson TB, Alexander ME, Simon CL, Griffiths CL, Peters K, Sibanda S, Miza S, Groenewald B, Majiedt P & Sink KJ (2016) Lost in translation? Standardising the terminology used in marine invasion biology and updating South African alien species lists. African Journal of Marine Science, <https://doi.org/10.2989/1814232X.1812016.1163292>
- Wilson JRU, Caplat P, Dickie I, Hui C, Maxwell BD, Nuñez MA, Pauchard A, Rejmánek M, Richardson DM, Robertson MP, Spear D, Webber BL, van Wilgen BW & Zenni RD (2014) A standardized set of metrics to assess and monitor tree invasions. Biological Invasions, 16, 535–551. <https://doi.org/10.1007/s10530-013-0605-x>
