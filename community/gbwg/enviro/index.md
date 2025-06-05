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
  * [Miwa Takahashi](mailto:miwa.takahashi@csiro.au) – Commonwealth Scientific and Industrial Research Organisation (CSIRO), Perth, Australia

## Core members
  * [Kristy Deiner](mailto:alpinedna@gmail.com)
  * [Chris Hunter](mailto:chris@gigasciencejournal.com)
  * [Stefania Marcheggiani](mailto:stefania.marcheggiani@iss.it)
  * [Joana Paupério](mailto:joanap@ebi.ac.uk)
  * [Peter Woollard](mailto:woollard@ebi.ac.uk)
  * [Luke Thompson](mailto:lrt175@ngi.msstate.edu) 
  * [Katherine Silliman](mailto:ks567@msstate.edu) 
  * [Steve Formel](mailto:steve@formeldataservices.com)
  * [Camila Babo](mailto:camila.babo@cibio.up.pt)
  * [Tobias Frøslev](mailto:tfroeslev@gbif.org)
  * [Saara Suominen](mailto:s.suominen@unesco.org)

## Motivation
Detection and monitoring of organisms and biodiversity via environmental DNA (eDNA) is becoming increasingly critical in times of climate change and anthropogenic pressure. A significant part of eDNA data’s value lies in its reusability, which can be enhanced through the use of rich metadata aligned with FAIR (Findable, Accessible, Interoperable, Reusable) data principles. Although established data standards organisations and infrastructures, such as GBIF, TDWG, GSC and GGBN, provide frameworks for managing DNA-related data, existing standards require substantial revision and extension to fit the specific needs of eDNA workflows and data. Our goal is to review and refine existing checklists, incorporate relevant terms into the DwC suite, and ensure interoperability and integration with other established standards and infrastructures. This will enhance FAIR data practices within eDNA communities and facilitate the integration of eDNA-derived occurrence records into broader biodiversity and environmental datasets. 

## History and context
  * This group has been established to develop a data standard and usage guidelines for sharing environmental DNA protocols and data. 
  * We will build on existing works by various organisations and initiatives (e.g., TDWG, GSC, GBIF, OBIS, ENA, FAIR eDNA (FAIRe), eDNAqua-Plan). 
  * Members of the eDNA Task Group co-lead the [MIxS-eDNA project](https://www.gensc.org/pages/projects/eDNA-project.html) under the GSC, coordinating efforts across initiatives and fulfilling the [MoU between TDWG and the GSC](https://github.com/tdwg/gbwg/blob/main/dwc-mixs/MoU/MemorandumOfUnderstanding_TDWG-GSC.md). 

## Challenges
  * Complex relationships within and between samples 
  * Complex relationships within and between sequences derived from samples
  * High variability in workflows (i.e., sampling, lab and bioinformatics protocols, metabarcoding or targeted-assay-based detections)
  * High diversity of use cases
  * Uncertainty in species assignments based on sequence data
  * Changes in identification associated with a given sequence
  * Large volumes of data associated with a single environmental sample
  * Complex preservation history and changes over time
  * Structural limitations of the star schema and occurrence-based data model 

**Goals/ Scopes/ Outputs** 
  * Collaborate with other data standards organisations (e.g., GSC), infrastructures (e.g., GBIF, OBIS, INSDC), working groups and initiatives (e.g., eDNAqua-Plan, FAIRe, commercial sectors) to build upon existing efforts and ensure interoperability and alignment with stakeholder needs
  *  Develop a metadata checklist with the following key focuses;
  * Describe the source and processing of eDNA samples and derived data, including sampling, DNA extraction, PCR-based species detection, sequencing, bioinformatics pipeline, resulting sequences, and species annotation.
  * Improve the description of the sample and its preservation history (in collaboration with the Material Sample TG)
  * Describe the “degree of uncertainty” of species occurrence records, enabling users to assess confidence levels and methodological limitations associated with detections
  * Capture relationships within and between samples and sequences, including parent-child relationships (e.g. by extending recommended vocabulary in relatedResourceClass) and sample-control associations (e.g., linking extraction negative controls to specific batches of eDNA samples). 
  * Develop definitions for glossary terms
  * Define application schemes using the standard with current ABCD and DwC models, including DwC-DP (alternative application schemes if needed)
  * Provide example use cases to illustrate best practice applications
  * Publish the proposed DwC/MIxS eDNA data standard and best practice guidelines

## Strategy
  * Collaborate and co-develop with related initiatives, working groups and networks (e.g. GBIF, GSC, GGBN, eDNAqua-Plan, FAIRe initiatives, commercial sectors, biobank networks, permit working group, data aggregators, material sample working group) 
  * Build on and consolidate existing works
  * Hold joint fortnightly meetings with members of the TDWG/GSC eDNA TG
  * Provide regular reports to the TDWG Interest Group and Executive Committee

## Outcomes
  * A comprehensive and interoperable eDNA metadata checklist, integrated into the DwC and MIxS frameworks and adopted by major biodiversity and sequence data infrastructures (e.g., GBIF, OBIS, INSDC)  
  * Strengthened adoption of FAIR data principles within the eDNA research and practitioner communities, supporting greater data reuse, integration, and long-term value

## Becoming involved
Interested parties are invited to watch and contribute to the [GitHub repository](https://github.com/tdwg/gbwg/) and participate in our calls. Please contact the convenor for more information. Also, please subscribe to our [open mailing](http://lists.tdwg.org/mailman/listinfo/tdwg-gbwg) list to be informed about upcoming meetings and news.

## Resources
  * Darwin Core Quick Reference Guide [https://dwc.tdwg.org/terms/](https://dwc.tdwg.org/terms/)
  * Minimum Information about any (x) Sequence (MIxS) standard [https://genomicsstandardsconsortium.github.io/mixs/](https://genomicsstandardsconsortium.github.io/mixs/)  
  * Darwin Core extension of DNA derived data [https://rs.gbif.org/extension/gbif/1.0/dna\_derived\_data\_2024-07-11.xml](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2024-07-11.xml)  
  * Abarenkov et al., (2023) Publishing DNA-derived data through biodiversity data platforms, v1.3. Copenhagen: GBIF Secretariat. [https://docs.gbif.org/publishing-dna-derived-data/en/](https://docs.gbif.org/publishing-dna-derived-data/en/)  
  * eDNAqua-Plan [https://ednaquaplan.com/](https://ednaquaplan.com/)
  * Takahashi et al., (in press) A metadata checklist and data formatting guidelines to make eDNA FAIR (Findable, Accessible, Interoperable and Reusable). Environmental DNA.
  * FAIR eDNA (FAIRe) guidelines [https://fair-edna.github.io/index.html](https://fair-edna.github.io/index.html)
  * GSC eDNA project [https://www.gensc.org/pages/projects/eDNA-project.html](https://www.gensc.org/pages/projects/eDNA-project.html)

