---
title: Sustainable DarwinCore MIxS Interoperability
summary: The Task Group has been convened to consolidate previous work that aimed to prevent siloed (meta)data standards development in the omics and broader biodiversity communities. The TG will leverage procedural and technical advancements in TDWG and the GSC to develop a sustainably interoperable MIxS-driven extension of DwC. The result will ensure that data produced in either MIxS- or DwC-compliant form can be automatically brokered between user communities, bringing the communities closer together.
cover_image: https://images.unsplash.com/photo-1606698235008-0b44ca6f7594
cover_image_by: David Clode
cover_image_ref: https://unsplash.com/photos/EyEdZ2aKRfA 
tags: task group
github:
---

## Convenors

Pier Luigi Buttigieg, Raïssa Meyer

## Core members  

Name | Institution 
--- | --- 
Chris Mungall |
John Wieczorek |
Pier Luigi Buttigieg |
Ramona Walls |
Raïssa Meyer |
Tim Robertson | GBIF
Thomas Stjernegaard Jeppesen | GBIF
Ward Appeltans | OBIS 
Pieter Provoost | OBIS
Saara Suominen | OBIS
Anton Van de Putte | 
Yi Ming Gan | 
Maxime Sweetlove | 

## Motivation

The task group is needed to build semantically precise and sustained interoperability between TDWG’s Darwin Core (DwC) [1] standard, and the Minimum Information about any (x) Sequence (MIxS) [2,3] checklist from the Genomic Standards Consortium (GSC) [4]. 

These two, de facto, (meta)data standards have co-existed for a number of years, but adoption of one or the other is still leading to the siloing of information and a resulting lack of sustained interoperability between systems such as those of the INSDC [5] and OBIS [6] or GBIF [7]. Meanwhile, some of these stakeholders are creating bespoke / local interpretations of DwC/MIxS mappings, which may further silo the digital holdings of the omic biodiversity community.

Here, we aim to consolidate previous work on this issue [8–11] into a stable, operational, and more authoritative cross-embedding of these de facto standards. This is becoming an urgent need by international efforts moving into the domain of omically-enabled biodiversity research and operations. 

A key motivation for this group is to ensure the “digital health” efforts leveraging the immense interest in using omic technologies to observe life in the oceans under the UN Decade of Ocean Science for Sustainable Development (2021-2030; <https://oceandecade.org/>). Stakeholders rallying around this global call either use both standards, or wish to collaborate across them as part of the Decade’s digital strategy (See the Data section in the [Implementation Plan](https://www.oceandecade.org/assets/uploads/documents/Ocean-Decade-Implementation-Plan-Version-2-0-min_1596634145.pdf)). The organisations who are the custodians of these standards need to agree on a functional and stable interoperation solution. Otherwise there will be increasing confusion and digital overhead in using omics biodiversity data to deepen our understanding of the marine ecosystem, increase our knowledge about drivers and consequences of change, and to inform policy decisions. 


## Goals outputs and outcomes

### Phase 1

- Building on previous work, create and complete a MIxS-driven extension of DwC, synchronised with GSC MIxS release cycles and mapped through IRIs
    - Explore both item-level IRI binding and extensible mapping through SSSOM-like approaches
- Qualify all mappings between MIxS fields and their counterparts in DwC
    - Qualifications will explain if discrepancies in, e.g., syntax are to be expected and suggest how these can be resolved
- Explore sustainable technology to preserve extensions and alternative mappings in a systematic way [12]
- Draft a Memorandum of Understanding (MoU) between TDWG and the GSC on how this mapping shall be maintained and developed to protect and deepen interoperability

### Phase 2

- For selected fields, propose controlled vocabularies in DwC to promote improved consistency and DwC-MIxS alignment
- For selected fields, propose term lists from a curated list of ontologies for semantic control

### Phase 3

- Socialise the extension and call for community feedback
- Test technical interoperability in a demonstration exercise (e.g. simulating an INSDC database using MIxS interoperating with an OBIS or GBIF simulation)

## Strategy

- Build on and consolidate previous work from within TDWG ([MIxS Sample extension](http://rs.gbif.org/sandbox/extension/mixs_sample.xml))
- Employ a series of online “extendathons” to address the goals stated above
- Continually report to both the GSC Compliance and Interoperability Group (CIG), GBWG, and the TDWG Executive Committee to ensure high-level endorsement
- Consult with users who work across omics and biodiversity to ensure the work of this Task Group is implementable and adds value globally


## Becoming involved

Interested parties are invited to watch and contribute to the GitHub repository (will be set up when the Task Group is endorsed [13]).

## History/context

- Over more than three Decades TDWG has developed capacity and expertise in handling and working with biodiversity data and metadata.
- Over the past 15 years, the GSC has been gathering experts and major sequence data facilities to develop meaningful metadata for sequence data. 
- Over the past decade, multi-omics approaches are becoming a mainstream feature in biodiversity research, observation, and monitoring. 
- Major infrastructures in both fields have adopted the developed standards and request compliant input data. However, the relevant standards are not the same across organisations. 
- For example, the INSDC resources accept MIxS-compliant metadata, while OBIS and GBIF have developed systems leveraging DwC. 
- In recent years, both TDWG and the GSC - which began as grassroots, primarily academic enterprises - are formalising their standards development procedures and enhancing their technological capacities, supporting more defined routes to sustainably interoperable with one another.
- The increased capacities of both the GSC and TDWG gives us an opportunity to reinvigorate previous efforts to align MIxS and DwC. Such efforts include:
    - a Hackathon-Workshop [9] on Darwin Core and MIxS Standards Alignment (February 2012)
- This gives us the opportunity to rigorously and persistently link GSC and TDWG standards, to prevent user communities of one or the other drifting apart. 

## Resources

1. 	Darwin Core. [cited 23 Nov 2020]. Available: <https://dwc.tdwg.org>
2. 	MIxS. [cited 23 Nov 2020]. Available: <https://gensc.org/mixs/>
3. 	Yilmaz P, Kottmann R, Field D, Knight R, Cole JR, Amaral-Zettler L, et al. Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications. Nat Biotechnol. 2011;29: 415–420.
4. 	Genomic Standards Consortium. [cited 23 Nov 2020]. Available: <https://gensc.org>
5. 	International Nucleotide Sequence Database Collaboration. [cited 23 Nov 2020]. Available: <http://www.insdc.org>
6. 	Ocean Biodiversity Information System. [cited 23 Nov 2020]. Available: <https://obis.org>
7. 	GBIF. [cited 23 Nov 2020]. Available: <https://www.gbif.org/>
8. 	[No title]. [cited 23 Nov 2020]. Available: <https://www.google.com/url?q=http://rs.gbif.org/sandbox/extension/mixs_sample.xml&sa=D&ust=1606134852828000&usg=AOvVaw2Uc21jolJo9dFujBI1u3D4>
9. 	Tuama ÉÓ, Deck J, Dröge G, Döring M, Field D, Kottmann R, et al. Meeting Report: Hackathon-Workshop on Darwin Core and MIxS Standards Alignment (February 2012). Stand Genomic Sci. 2012;7: 166.
10. <http://rs.gbif.org/sandbox/extension/dna_derived_data.xml>
11. Andersson AF, Bissett A, Finstad AG, Fossøy F, Grosjean M, Hope M, et al. Publishing DNA-derived data through biodiversity data platforms [Community review draft]. [cited 23 Nov 2020]. Available: <https://doi.org/10.35035/doc-vf1a-nr22>
12. microbiomedata. microbiomedata/metadata_converter. [cited 23 Nov 2020]. Available: <https://github.com/microbiomedata/metadata_converter>
13. GitHub repository: To be decided shortly

