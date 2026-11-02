---
title: Mineralogy Extension terms ratified
description: >
  Darwin Core now supports mineralogical and geological collections with 26 new properties, a new class, and one revised term
background:
  img: https://static.tdwg.org/images/articles/2026/wulfenite-crystal.jpg
  by: Ivar Leidus via Wikimedia Commons CC BY-SA 4.0. Orange red tabular crystals of wulfenite
  href: https://en.wikipedia.org/wiki/File:Wulfenite_-_Red_Cloud_mine,_La_Paz_Co.,_Arizona,_USA.jpg

tags: [Standards, Darwin Core, Mineralogy Extension]

toc: true
---

After several years of work by the [Mineralogy Extension Task Group](/community/esp/mineralogy/), terms supporting mineralogical and geological collections have been ratified as additions to the [Darwin Core Standard](https://dwc.tdwg.org/). The additions consist of a new class, `dwc:GeologicalMaterial`, 26 new properties, nine IRI-valued (`dwciri:`) equivalents, and a revision of one existing term. The TDWG Executive Committee ratified them on 13 October 2026, and they are now published in the [Darwin Core List of Terms](https://dwc.tdwg.org/list/) and [Quick Reference Guide](https://dwc.tdwg.org/terms/).

## Bringing mineralogy into Darwin Core

The Task Group formed under the [Earth Sciences and Paleobiology Interest Group](/community/esp/) to fill a long-standing gap. Biological and paleontological specimens share a hierarchical, Linnaean classification. Mineral specimens do not: they are classified under separate, partly hierarchical systems such as Dana and Nickel-Strunz, and are often compound objects made of several minerals in a single rock. Darwin Core's existing terms could not describe this.

Led by conveners Ben Norton (Yale University) and Dr. Rachel Walcott (National Museums Scotland), the Task Group brought together curators, collection managers, and geoinformatics specialists from institutions in North America and Europe, many of which had not taken part in TDWG before. Before submitting anything to Darwin Core, the Task Group held a targeted community review. Eleven earth sciences collection specialists assessed every draft term; together, the reviewers and the Task Group came from seven countries. Because TDWG has less depth in some earth sciences subdomains, the Task Group deliberately set a higher bar for ratification than usual. The term set was also implemented end to end on the [GeoSpecimens](https://geospecimens.org) platform and documented in a [Feature and Implementation Experience Report](https://github.com/tdwg/mineralogy/blob/main/reference/FeatureImplementationReport_v20260706.pdf).

## What the new terms provide

The ratified terms let collections describe:

- **Compound specimens and their parts.** `dwc:materialRole` and `dwc:materialProportion` describe how a part relates to the specimen it belongs to, for example a phenocryst making up a minor share of a host rock.
- **Geological materials.** The new `dwc:GeologicalMaterial` class is a kind of `dwc:MaterialEntity`. It carries mineral and lithotaxon names, classification codes, measured chemistry, analysis protocols, and mineral paragenetic sequences.
- **Geological context.** Lithodemic units, tectonic units, geologic provinces, and geologic events cover the many geological settings that stratigraphic terms alone cannot describe.
- **Curation and safety.** Hazard types, handling requirements, treatments, and damage remarks apply to material entities in any discipline.
- **Mass, sampled features, and named places.** These fill common gaps in specimen and locality records.

Several of these terms are useful beyond the earth sciences, including in botanical and zoological collections.

## Review and ratification

The terms were proposed to the [Darwin Core Maintenance Group](/community/dwc/) and reviewed in the [Darwin Core Public Review – July 2026](https://dwc.tdwg.org/public_review/), the first in Darwin Core's new triannual review and release cycle. The proposals are collected under [umbrella issue 900](https://github.com/tdwg/dwc/issues/900).

The review led to substantial improvements. The Task Group withdrew four proposed classes (Chemistry, Conservation, Hazard, and GeoName) in favour of a flatter model. Their properties now sit in existing Darwin Core classes or in the new `dwc:GeologicalMaterial` class. Proposed descriptive properties such as crystal habit, luster, cleavage, and color were not added as Darwin Core properties. Instead, they are recorded as assertions, with their names used as `dwc:assertionType` values (see [Material Assertion vocabulary](#material-assertion-vocabulary) below). One proposal, `isTypeLocality` ([tdwg/dwc\#796](https://github.com/tdwg/dwc/issues/796)), is still under discussion and was not part of this release.

## Ratified terms

The tables below list the terms added or changed by the Mineralogy Extension. Each term links to its entry in the normative [Darwin Core List of Terms](https://dwc.tdwg.org/list/).

Darwin Core publishes many of its terms in two namespaces:

- **`dwc:` terms** take literal values, that is, text or numbers as they appear in a record, such as `dwc:hazardType` \= "radioactive".
- **`dwciri:` terms** have the same meaning as their `dwc:` analogues, but their values must be IRIs. An IRI identifies a resource on the web, such as a concept in a controlled vocabulary. An example is `dwciri:hazardType` \= a link to the "radioactive" concept in a published hazard vocabulary. These terms make the data machine-actionable as Linked Data. The [Darwin Core RDF Guide](https://dwc.tdwg.org/rdf/) explains how to use them.

### Darwin Core (`dwc:`) terms

| Class | Term | Label | Action | Issue |
| :---- | :---- | :---- | :---- | :---- |
| Location | [dwc:namedPlace](https://dwc.tdwg.org/list/#dwc_namedPlace) | Named Place | new | [tdwg/dwc\#795](https://github.com/tdwg/dwc/issues/795) |
| GeologicalContext | [dwc:geologicEvent](https://dwc.tdwg.org/list/#dwc_geologicEvent) | Geologic Event | new | [tdwg/dwc\#800](https://github.com/tdwg/dwc/issues/800) |
| GeologicalContext | [dwc:geologicProvince](https://dwc.tdwg.org/list/#dwc_geologicProvince) | Geologic Province | new | [tdwg/dwc\#799](https://github.com/tdwg/dwc/issues/799) |
| GeologicalContext | [dwc:lithodemicUnit](https://dwc.tdwg.org/list/#dwc_lithodemicUnit) | Lithodemic Unit | new | [tdwg/dwc\#798](https://github.com/tdwg/dwc/issues/798) |
| GeologicalContext | [dwc:tectonicUnits](https://dwc.tdwg.org/list/#dwc_tectonicUnits) | Tectonic Units | new | [tdwg/dwc\#956](https://github.com/tdwg/dwc/issues/956) |
| MaterialEntity | [dwc:damageRemarks](https://dwc.tdwg.org/list/#dwc_damageRemarks) | Damage Remarks | new | [tdwg/dwc\#952](https://github.com/tdwg/dwc/issues/952) |
| MaterialEntity | [dwc:handlingRequirements](https://dwc.tdwg.org/list/#dwc_handlingRequirements) | Handling Requirements | new | [tdwg/dwc\#951](https://github.com/tdwg/dwc/issues/951) |
| MaterialEntity | [dwc:hazardRemarks](https://dwc.tdwg.org/list/#dwc_hazardRemarks) | Hazard Remarks | new | [tdwg/dwc\#790](https://github.com/tdwg/dwc/issues/790) |
| MaterialEntity | [dwc:hazardType](https://dwc.tdwg.org/list/#dwc_hazardType) | Hazard Type | new | [tdwg/dwc\#788](https://github.com/tdwg/dwc/issues/788) |
| MaterialEntity | [dwc:materialDescription](https://dwc.tdwg.org/list/#dwc_materialDescription) | Material Description | new | [tdwg/dwc\#957](https://github.com/tdwg/dwc/issues/957) |
| MaterialEntity | [dwc:materialProportion](https://dwc.tdwg.org/list/#dwc_materialProportion) | Material Proportion | new | [tdwg/dwc\#941](https://github.com/tdwg/dwc/issues/941) |
| MaterialEntity | [dwc:materialRole](https://dwc.tdwg.org/list/#dwc_materialRole) | Material Role | new | [tdwg/dwc\#942](https://github.com/tdwg/dwc/issues/942) |
| MaterialEntity | [dwc:measuredMassInGrams](https://dwc.tdwg.org/list/#dwc_measuredMassInGrams) | Measured Mass In Grams | new | [tdwg/dwc\#802](https://github.com/tdwg/dwc/issues/802) |
| MaterialEntity | [dwc:sampledFeatureType](https://dwc.tdwg.org/list/#dwc_sampledFeatureType) | Sampled Feature Type | new | [tdwg/dwc\#794](https://github.com/tdwg/dwc/issues/794) |
| MaterialEntity | [dwc:treatments](https://dwc.tdwg.org/list/#dwc_treatments) | Treatments | new | [tdwg/dwc\#950](https://github.com/tdwg/dwc/issues/950) |
| MaterialEntity | [dwc:verbatimMass](https://dwc.tdwg.org/list/#dwc_verbatimMass) | Verbatim Mass | new | [tdwg/dwc\#801](https://github.com/tdwg/dwc/issues/801) |
| GeologicalMaterial | [dwc:GeologicalMaterial](https://dwc.tdwg.org/list/#dwc_GeologicalMaterial) | Geological Material | new | [tdwg/dwc\#1050](https://github.com/tdwg/dwc/issues/1050) |
| GeologicalMaterial | [dwc:chemistryRemarks](https://dwc.tdwg.org/list/#dwc_chemistryRemarks) | Chemistry Remarks | new | [tdwg/dwc\#936](https://github.com/tdwg/dwc/issues/936) |
| GeologicalMaterial | [dwc:classificationCodes](https://dwc.tdwg.org/list/#dwc_classificationCodes) | Classification Codes | new | [tdwg/dwc\#937](https://github.com/tdwg/dwc/issues/937) |
| GeologicalMaterial | [dwc:geologicMaterialNameID](https://dwc.tdwg.org/list/#dwc_geologicMaterialNameID) | Geologic Material Name ID | new | [tdwg/dwc\#944](https://github.com/tdwg/dwc/issues/944) |
| GeologicalMaterial | [dwc:geologicalMaterialNames](https://dwc.tdwg.org/list/#dwc_geologicalMaterialNames) | Geological Material Names | new | [tdwg/dwc\#943](https://github.com/tdwg/dwc/issues/943) |
| GeologicalMaterial | [dwc:geologicalMaterialNameTypes](https://dwc.tdwg.org/list/#dwc_geologicalMaterialNameTypes) | Geological Material Name Types | new | [tdwg/dwc\#947](https://github.com/tdwg/dwc/issues/947) |
| GeologicalMaterial | [dwc:measuredChemistry](https://dwc.tdwg.org/list/#dwc_measuredChemistry) | Measured Chemistry | new | [tdwg/dwc\#792](https://github.com/tdwg/dwc/issues/792) |
| GeologicalMaterial | [dwc:measuredChemistrySource](https://dwc.tdwg.org/list/#dwc_measuredChemistrySource) | Measured Chemistry Source | new | [tdwg/dwc\#793](https://github.com/tdwg/dwc/issues/793) |
| GeologicalMaterial | [dwc:mineralogicalAnalysisProtocol](https://dwc.tdwg.org/list/#dwc_mineralogicalAnalysisProtocol) | Mineralogical Analysis Protocol | new | [tdwg/dwc\#954](https://github.com/tdwg/dwc/issues/954) |
| GeologicalMaterial | [dwc:mineralSequence](https://dwc.tdwg.org/list/#dwc_mineralSequence) | Mineral Sequence | new | [tdwg/dwc\#955](https://github.com/tdwg/dwc/issues/955) |
| Identification | [dwc:classificationSystem](https://dwc.tdwg.org/list/#dwc_classificationSystem) | Classification System | new | [tdwg/dwc\#945](https://github.com/tdwg/dwc/issues/945) |
| Identification | [dwc:verbatimIdentification](https://dwc.tdwg.org/list/#dwc_verbatimIdentification) | Verbatim Identification | change | [tdwg/dwc\#905](https://github.com/tdwg/dwc/issues/905) |

### IRI-valued (`dwciri:`) terms

| Class | Term | Label | Literal (`dwc:`) analogue |
| :---- | :---- | :---- | :---- |
| GeologicalContext | [dwciri:geologicEvent](https://dwc.tdwg.org/list/#dwciri_geologicEvent) | Geologic Event (IRI) | [dwc:geologicEvent](https://dwc.tdwg.org/list/#dwc_geologicEvent) |
| GeologicalContext | [dwciri:geologicProvince](https://dwc.tdwg.org/list/#dwciri_geologicProvince) | Geologic Province (IRI) | [dwc:geologicProvince](https://dwc.tdwg.org/list/#dwc_geologicProvince) |
| MaterialEntity | [dwciri:hazardType](https://dwc.tdwg.org/list/#dwciri_hazardType) | Hazard Type (IRI) | [dwc:hazardType](https://dwc.tdwg.org/list/#dwc_hazardType) |
| MaterialEntity | [dwciri:materialProportion](https://dwc.tdwg.org/list/#dwciri_materialProportion) | Material Proportion (IRI) | [dwc:materialProportion](https://dwc.tdwg.org/list/#dwc_materialProportion) |
| MaterialEntity | [dwciri:materialRole](https://dwc.tdwg.org/list/#dwciri_materialRole) | Material Role (IRI) | [dwc:materialRole](https://dwc.tdwg.org/list/#dwc_materialRole) |
| MaterialEntity | [dwciri:sampledFeatureType](https://dwc.tdwg.org/list/#dwciri_sampledFeatureType) | Sampled Feature Type (IRI) | [dwc:sampledFeatureType](https://dwc.tdwg.org/list/#dwc_sampledFeatureType) |
| GeologicalMaterial | [dwciri:measuredChemistrySource](https://dwc.tdwg.org/list/#dwciri_measuredChemistrySource) | Measured Chemistry Source (IRI) | [dwc:measuredChemistrySource](https://dwc.tdwg.org/list/#dwc_measuredChemistrySource) |
| GeologicalMaterial | [dwciri:mineralogicalAnalysisProtocol](https://dwc.tdwg.org/list/#dwciri_mineralogicalAnalysisProtocol) | Mineralogical Analysis Protocol (IRI) | [dwc:mineralogicalAnalysisProtocol](https://dwc.tdwg.org/list/#dwc_mineralogicalAnalysisProtocol) |
| Identification | [dwciri:classificationSystem](https://dwc.tdwg.org/list/#dwciri_classificationSystem) | Classification System (IRI) | [dwc:classificationSystem](https://dwc.tdwg.org/list/#dwc_classificationSystem) |

## Material Assertion vocabulary

Alongside the ratified terms, the Task Group has published the [Geological Material Assertion Types](https://kos.geospecimens.org/def/geological-material-assertion-type) vocabulary. It is a controlled vocabulary of 17 assertion types for recording the observable, measurable, and structural qualities of geological materials, especially mineral specimens. It is the first controlled vocabulary developed for material assertions. In a [Darwin Core Data Package](https://dwc.tdwg.org/dp/), each concept supplies a value for the `assertionType` field of the Material Assertion table. In a Darwin Core Archive, the same values can be used in the MeasurementOrFact extension or as keys in `dwc:dynamicProperties`.

Each concept is published as Linked Data with a persistent URI on the [GeoSpecimens Vocabulary Publisher](https://kos.geospecimens.org), with a definition, usage notes, and mappings to related vocabularies. The vocabulary is not part of this ratification; it is currently listed with a status of *submitted* and may be proposed in a future Darwin Core review. The Task Group has also published related vocabularies on the same site, including luster, aggregate form, and hazard types.

| Category | Assertion type | `dwc:assertionType` value |
| :---- | :---- | :---- |
| Dimensions | [Verbatim Size](https://kos.geospecimens.org/def/geological-material-assertion-type/verbatim-size) | `verbatimSize` |
| Dimensions | [Measured Width in Millimeters](https://kos.geospecimens.org/def/geological-material-assertion-type/measured-width-in-millimeters) | `measuredWidthInMillimeters` |
| Dimensions | [Measured Height in Millimeters](https://kos.geospecimens.org/def/geological-material-assertion-type/measured-height-in-millimeters) | `measuredHeightInMillimeters` |
| Dimensions | [Measured Depth in Millimeters](https://kos.geospecimens.org/def/geological-material-assertion-type/measured-depth-in-millimeters) | `measuredDepthInMillimeters` |
| Dimensions | [Maximum Axial Dimension](https://kos.geospecimens.org/def/geological-material-assertion-type/maximum-axial-dimension) | `maxCrystalDimensionInMillimeters` |
| Crystallography and morphology | [Aggregate Form](https://kos.geospecimens.org/def/geological-material-assertion-type/aggregate-form) | `aggregateForm` |
| Crystallography and morphology | [Crystal Habit](https://kos.geospecimens.org/def/geological-material-assertion-type/crystal-habit) | `crystalHabit` |
| Crystallography and morphology | [Crystal Form](https://kos.geospecimens.org/def/geological-material-assertion-type/crystal-form) | `crystalForm` |
| Crystallography and morphology | [Twinning Law](https://kos.geospecimens.org/def/geological-material-assertion-type/twinning-law) | `twinningLaw` |
| Crystallography and morphology | [Cleavage](https://kos.geospecimens.org/def/geological-material-assertion-type/cleavage) | `cleavage` |
| Crystallography and morphology | [Exsolution Texture](https://kos.geospecimens.org/def/geological-material-assertion-type/exsolution-texture) | `exsolutionTexture` |
| Optical and surface properties | [Color](https://kos.geospecimens.org/def/geological-material-assertion-type/color) | `color` |
| Optical and surface properties | [Luster](https://kos.geospecimens.org/def/geological-material-assertion-type/luster) | `luster` |
| Optical and surface properties | [Luminescence Description](https://kos.geospecimens.org/def/geological-material-assertion-type/luminescence-description) | `luminescence` |
| Composition and associations | [Associated Minerals](https://kos.geospecimens.org/def/geological-material-assertion-type/associated-minerals) | `associatedMinerals` |
| Composition and associations | [Inclusions](https://kos.geospecimens.org/def/geological-material-assertion-type/inclusions) | `inclusions` |
| Composition and associations | [Alteration Description](https://kos.geospecimens.org/def/geological-material-assertion-type/alteration-description) | `alterationDescription` |

## Next steps

The ratified terms will be maintained under the [Vocabulary Maintenance Specification](https://www.tdwg.org/standards/vms/) through the regular Darwin Core review cycle. Future work includes SKOS crosswalks to adjacent standards, such as the [ABCD Extension for Geosciences (EFG)](/community/esp/efg/) and GeoSciML, and extending the model to neighbouring domains, including petrology, astromaterials, and economic geology.

## Acknowledgements

This work was made possible by TDWG community support funding, which enabled an international collaboration across eleven institutions. The Task Group thanks its members: Thomas Burri (Natural History Museum Bern), Allison Dombrowski (North Carolina Museum of Natural Sciences), Nicolas Greber (Natural History Museum of Geneva), Olle Hints (Tallinn University of Technology), Adam Mansur (Smithsonian Institution National Museum of Natural History), André Puschnig (Natural History Museum Basel), Jolyon Ralph (Mindat.org), Stephen Richard, and Chris Tacker (North Carolina Museum of Natural Sciences). It also thanks the community reviewers: Marie Angel (California Academy of Sciences), Veronica di Cecco (Royal Ontario Museum), Allison Dombrowski (North Carolina Museum of Natural Sciences), Carrie A. Eaton (Geology Museum, University of Wisconsin), Jana Horak (Amgueddfa Cymru – Museum Wales), Mary Johnson (Mary Johnson Consulting), Stéphane Jouve (Sorbonne Université), Duncan Murdock (Oxford University Museum of Natural History), Mike Rumsey (Natural History Museum, London), Roy Starkey (Russell Society), and Yakov Weiss (Hebrew University of Jerusalem). Finally, the Task Group is grateful to the Darwin Core Maintenance Group, the Executive Committee, the Earth Sciences and Paleobiology Interest Group, and the wider TDWG community for their support.

## Questions

For more information, see the [Darwin Core data standard](https://dwc.tdwg.org/) website and the [Mineralogy Extension repository](https://github.com/tdwg/mineralogy). You can reach out to the [Mineralogy Extension Task Group](/community/esp/mineralogy/) or the [Darwin Core Maintenance Group](/community/dwc/) with any questions.