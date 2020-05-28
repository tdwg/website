---
title: AC - 3D Imagery and Data
summary: 
cover_image: https://images.unsplash.com/photo-1580407196238-dac33f57c410
cover_image_by: Wolfgang Hasselman
cover_image_ref: https://unsplash.com/photos/6JZJyHXQ-p0https://unsplash.com/photos/6JZJyHXQ-p0
tags: task group
github: https://github.com/tdwg/ac/tree/master/3d
status: published
---
# 3D Imagery and Data 

**A task group of the Audubon Core interest group**

# Convenor

  - [Doug Boyer](mailto:douglasmb@gmail.com), Duke University

# Core members 

  - [Rebecca Snyder](mailto:snyderr@si.edu), National Museum of Natural History, Washington DC
  - [Gary Motz](mailto:garymotz@indiana.edu), Indianna University, Bloomington
  - [Kate Webbink](mailto:kwebbink@fieldmuseum.org), Field Museum, Chicago
  - [Julia Winchester](mailto:julia.winchester@stonybrook.edu), New York State University, Stonybrook
  - [Jon Blundell](mailto:blundellj@si.edu), National Museum of Natural History, Washington DC

# Motivation 

A growing number of 3D imaging methods are being used to create high
fidelity models of natural history objects, and in some cases even to
record field observations of living organisms. The core metadata
describing the files resulting from these imaging events is more
extensive than that currently included in Audubon Core. Therefore the
ability to describe, find and preserve these digital objects robustly
in biodiversity databases remains limited. As imaging becomes more and
more dominated by 3D, Audubon Core will be more and more limited until
its terms in this area are extended.

# Goals outputs and outcomes 

The deliverables from this task group will include the following
additions to the Audubon Core standard:

Phase 1 (to be completed by the end of 2019):

  - Property term additions to Audubon Core. The terms will be used to
    describe metadata specifically related to 3D images and will be
    organized within the Service Access Point (SAP) vocabulary.

  - Additional controlled vocabulary terms to be used as values for
    ac:variant. The terms will describe the format of the SAP as do the
    current recommended values.

  - Class terms for 3D imaging modalities to be used as values for
    ac:subtype. These terms would be subclasses of dcmitype:StillImage.

Phase 2 (to be completed by the end of 2020):

  - Property term additions for creating modality-specific metadata.
    Many of these terms will be organized within the Resource Creation
    vocabulary.

The task group will also produce the following reference documents,
which may be ancillary to (not included within) the standard.

  - A descriptive document summarizing the major 3D imaging modalities
    in use. This document will associate the enumerated modalities with
    their corresponding class terms (ac:subtype values) and the
    recommended metadata terms that are appropriate for describing each
    modality.

  - A descriptive document summarizing the major 3D file formats and
    listing the recommended metadata terms for describing them.

  - A Best Practices document for describing the image capture event.

# Strategy 

Since the deliverables outlined in this charter constitute coordinated
additions to Audubon Core, the task group will produce a Feature
Report as required in Section 4.2.1 of the Vocabulary Maintenance
Specification (VMS) prior to Phase 1 of the work. The convenor and
core members will collaborate with CS3DP working group to assemble the
use cases necessary for the creation of the report.

Following the development of the suite of terms, the task group will
collect implementation experience data from the CS3DP working group
who have tried using the new terms with their data sets. These data
will be included in an Implementation Experience Report (Section 4.2.2
of the VMS) for Phase 1 that will be completed before submission of
the Phase 1 terms for adoption.

Following the completion of Phase 1, the experience gained in Phase 1
will be used to guide the Feature Report for Phase 2 and the
subsequent development of the Phase 2 terms. After the CS3DP
constituency has had an opportunity to try using the Phase 2 terms,
their experience will be documented in a Phase 2 Implementation
Experience Report prior to submission of the Phase 2 term list.

The additional documents will be developed simultaneously with the
terms that they describe so that they will be available for use by the
community at the time the new terms are adopted.

# Becoming involved 

Anyone with practical experience in describing 3D imagery in a
database is invited to contact the convenor or core members to
register their interest.

# History/context 

Multiple initiatives began seeking develop and implement community
standards for 3D data description and preservation between 2013-2018
partly in response to major increases in the rate of production of 3D
imagery including major NSF DBI (ADBC & ABI) funded initiatives to 3D
image 10’s of thousands of species from museum collections (e.g.,
oVert).

# Summary 

A task group to extend vocabulary relating to 3D imagery and data
has been formed under the Audubon Core Maintenance group. The main
deliverables in Phase 1 of the group's work will be: property terms
for describing Service Access Points of 3D images, controlled
vocabulary terms for 3D imaging formats to serve as values for
ac:variant, and class terms for 3D imaging modalities to be used as
values for ac:subtype. The main deliverables in Phase 2 will be
property terms additions for 3D modality-specific metadata.

# Resources 

  - [Group GitHub repository](https://github.com/tdwg/ac/tree/master/3d)
  - [https://osf.io/ewt2h/](https://osf.io/ewt2h/)
  - [https://www.idigbio.org/wiki/index.php/3D\_Scan\_Modality\_Subtypes](https://www.idigbio.org/wiki/index.php/3D_Scan_Modality_Subtypes)
  - [https://www.idigbio.org/wiki/index.php/MorphoSource](https://www.idigbio.org/wiki/index.php/MorphoSource)
