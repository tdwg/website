---
title: Sustainable DarwinCore MIxS Interoperability
description: >
  The Task Group was convened to consolidate previous work that aimed to prevent siloed (meta)data standards development in the omics and broader biodiversity communities. The TG leverages procedural and technical advancements in TDWG and the GSC to develop a sustainably interoperable MIxS-driven extension of DwC. The results (completed in 2023) ensure that data produced in either MIxS- or DwC-compliant form can be automatically brokered between user communities, bringing the communities closer together.
background:
  img: https://images.unsplash.com/photo-1606698235008-0b44ca6f7594
  by: David Clode
  href: https://unsplash.com/photos/EyEdZ2aKRfA
github: https://github.com/tdwg/gbwg/tree/main/dwc-mixs
toc: true
---

## Conveners

- [Pier Luigi Buttigieg](https://orcid.org/0000-0002-4366-3088)
- [Raïssa Meyer](https://orcid.org/0000-0002-2996-719X)

## Core members

- [Anton Van de Putte](https://orcid.org/0000-0003-1336-5554)
- [Bill Duncan](https://orcid.org/0000-0001-9625-1899)
- [Chris Mungall](https://orcid.org/0000-0002-6601-2165)
- [John Wieczorek](https://orcid.org/0000-0003-1144-0290)
- [Mariya Dimitrova](https://orcid.org/0000-0002-8083-6048)
- [Maxime Sweetlove](https://orcid.org/0000-0003-3770-3714)
- [Pier Luigi Buttigieg](https://orcid.org/0000-0002-4366-3088)
- [Pieter Provoost](https://orcid.org/0000-0002-4236-0384)
- [Ramona Walls](https://orcid.org/0000-0001-8815-0078)
- [Raïssa Meyer](https://orcid.org/0000-0002-2996-719X)
- [Saara Suominen](https://orcid.org/0000-0001-9401-8460)
- [Thomas Stjernegaard Jeppesen](https://orcid.org/0000-0003-1691-239X)
- [Tim Robertson](https://orcid.org/0000-0001-6215-3617)
- [Ward Appeltans](https://orcid.org/0000-0002-3237-4547)
- [Yi Ming Gan](https://orcid.org/0000-0001-7087-2646)

## Motivation

**NOTE: this Task Group has completed its work and is no longer active.**

The task group built semantically precise and sustained interoperability between TDWG’s Darwin Core (DwC) [1] standard, and the Minimum Information about any (x) Sequence (MIxS) [2,3] checklist from the Genomic Standards Consortium (GSC) [4].

These two, de facto, (meta)data standards have co-existed for a number of years, but adoption of one or the other is still leading to the siloing of information and a resulting lack of sustained interoperability between systems such as those of the INSDC [5] and OBIS [6] or GBIF [7]. Meanwhile, some of these stakeholders are creating bespoke / local interpretations of DwC/MIxS mappings, which may further silo the digital holdings of the omic biodiversity community.

Here, we aim to consolidate previous work on this issue [8–11] into a stable, operational, and more authoritative cross-embedding of these de facto standards. This is becoming an urgent need by international efforts moving into the domain of omically-enabled biodiversity research and operations.

A key motivation for this group is to ensure the “digital health” efforts leveraging the immense interest in using omic technologies to observe life in the oceans under the UN Decade of Ocean Science for Sustainable Development (2021-2030; <https://oceandecade.org/>). Stakeholders rallying around this global call either use both standards, or wish to collaborate across them as part of the Decade’s digital strategy (See the Data section in the [Implementation Plan](https://www.oceandecade.org/assets/uploads/documents/Ocean-Decade-Implementation-Plan-Version-2-0-min_1596634145.pdf)). The organisations who are the custodians of these standards need to agree on a functional and stable interoperation solution. Otherwise there will be increasing confusion and digital overhead in using omics biodiversity data to deepen our understanding of the marine ecosystem, increase our knowledge about drivers and consequences of change, and to inform policy decisions.

## Goals, outputs and outcomes

#### Phase 1

- Building on previous work, create and complete a MIxS-driven extension of DwC, synchronised with GSC MIxS release cycles and mapped through IRIs
    - Explore both item-level IRI binding and extensible mapping through SSSOM-like approaches
- Qualify all mappings between MIxS fields and their counterparts in DwC
    - Qualifications will explain if discrepancies in, e.g., syntax are to be expected and suggest how these can be resolved
- Explore sustainable technology to preserve extensions and alternative mappings in a systematic way [10]
- Draft a Memorandum of Understanding (MoU) between TDWG and the GSC on how this mapping shall be maintained and developed to protect and deepen interoperability

#### Phase 2

- For selected fields, propose controlled vocabularies in DwC to promote improved consistency and DwC-MIxS alignment
- For selected fields, propose term lists from a curated list of ontologies for semantic control

#### Phase 3

- Socialise the extension and call for community feedback
- Test technical interoperability in a demonstration exercise (e.g. simulating an INSDC database using MIxS interoperating with an OBIS or GBIF simulation)

## Strategy

- Build on and consolidate previous work from within TDWG ([MIxS Sample extension](http://rs.gbif.org/sandbox/extension/mixs_sample.xml))
- Employ a series of online “extendathons” to address the goals stated above
- Continually report to both the GSC Compliance and Interoperability Group (CIG), GBWG, and the TDWG Executive Committee to ensure high-level endorsement
- Consult with users who work across omics and biodiversity to ensure the work of this Task Group is implementable and adds value globally

## Results

[Memorandum of Understanding (MoU) between TDWG and the GSC](https://www.gensc.org//news/2022/11/04/gsc_tdwg_mou.html)

Meyer R, Appeltans W, Duncan WD, Dimitrova M, Gan Y-M, Stjernegaard Jeppesen T, Mungall C, Paul DL, Provoost P, Robertson T, Schriml L, Suominen S, Walls R, Sweetlove M, Ung V, Van de Putte A, Wallis E, Wieczorek J, Buttigieg PL (2023) **_Aligning Standards Communities for Omics Biodiversity Data: Sustainable Darwin Core-MIxS Interoperability._** Biodiversity Data Journal 11: e112420. https://doi.org/10.3897/BDJ.11.e112420

Mappings can be found in the [TDWG/GBWG GitHub repository](https://github.com/tdwg/gbwg/tree/v2.1.0/dwc-mixs/mapping), with related discussions captured on the [issue tracker](https://github.com/tdwg/gbwg/issues?q=is%3Aissue+label%3A%22DwC-MIxS+TG%22+is%3Aclosed).


## Becoming involved

**NOTE: this Task Group has completed its work in 2023 and is no longer active.**

Interested parties are invited to watch and contribute the [Darwin Core](https://dwc.tdwg.org/) and joint TDWG-GSC [Genomic Biodiversity Working Group](https://www.tdwg.org/community/gbwg/), as well as other activities within TDWG and the [GSC](https://www.gensc.org/index.html).

## History and context

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

1. Darwin Core. <https://dwc.tdwg.org>
2. MIxS <https://gensc.org/mixs/>(broken link) <http://w3id.org/mixs>
3. Yilmaz P, Kottmann R, Field D, Knight R, Cole JR, Amaral-Zettler L, et al. Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications. Nat Biotechnol. 2011 May;29(5):415-20. doi: <https://doi.org/10.1038/nbt.1823>. PMID: 21552244; PMCID: PMC3367316.
4. Genomic Standards Consortium <https://gensc.org>
5. International Nucleotide Sequence Database Collaboration <https://insdc.org>
6. Ocean Biodiversity Information System <https://obis.org>
7. GBIF <https://www.gbif.org/>
8. MIxS DwC extension <https://github.com/tdwg/gbwg/tree/main/dwc-mixs/dwc>
9. Tuama EÓ, Deck J, Dröge G, Döring M, Field D, Kottmann R, Ma J, Mori H, Morrison N, Sterk P, Sugawara H, Wieczorek J, Wu L, Yilmaz P. Meeting Report: Hackathon-Workshop on Darwin Core and MIxS Standards Alignment (February 2012). Stand Genomic Sci. 2012 Oct 10;7(1):166-70. doi: <https://doi.org/10.4056/sigs.3166513>. Epub 2012 Sep 28. PMID: 23451295; PMCID: PMC3570805.
10. <https://github.com/microbiomedata/metadata_converter>
11. GitHub repository: <https://github.com/tdwg/gbwg>
