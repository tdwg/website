---
title: Darwin Core
summary: Darwin Core is a standard maintained by the [Darwin Core maintenance group](../../community/dwc). It includes a glossary of terms intended to **facilitate the sharing of information about biological diversity** by providing identifiers, labels, and definitions. Darwin Core is primarily based on taxa, their occurrence in nature as documented by observations, specimens, samples, and related information.
cover_image: https://images.unsplash.com/photo-1492031215329-791748ee1253
cover_image_by: Alex Guillaume
cover_image_ref: https://unsplash.com/photos/0MC0o-xLucM
tags: technical specification, current standard, 2009
github: https://github.com/tdwg/dwc
website: https://dwc.tdwg.org
website_title: Darwin Core website
---

## Header section

Title
: Darwin Core

Permanent IRI (for citations and links)
: <http://www.tdwg.org/standards/450>

Publisher
: [Biodiversity Information Standards (TDWG)](https://www.tdwg.org/)

Ratified
: 2009-10-09

Status
: [Current standard](https://www.tdwg.org/standards/status-and-categories/)

Category
: [Technical specification](https://www.tdwg.org/standards/status-and-categories/#categories%20of%20tdwg%20standards_1)

Abstract
: Darwin Core is a standard maintained by the Darwin Core maintenance group. It includes a glossary of terms (in other contexts these might be called properties, elements, fields, columns, attributes, or concepts) intended to facilitate the sharing of information about biological diversity by providing identifiers, labels, and definitions. Darwin Core is primarily based on taxa, their occurrence in nature as documented by observations, specimens, samples, and related information.

Bibliographic citation
: > Darwin Core Task Group. 2009. Darwin Core. Biodiversity Information Standards (TDWG) http://www.tdwg.org/standards/450

## Maintenance group

Modifications and enhancements to Darwin Core are managed by the [Darwin Core Maintenance Group](../../community/dwc).

The best way to be involved is to create an account on [GitHub](https://github.com), and "watch" the [Darwin Core GitHub repository](https://github.com/tdwg/dwc), as well as the [Darwin Core Questions & Answers repository](https://github.com/tdwg/dwc-qa), and respond to requests for comments or "issues" ([Darwin Core issues](https://github.com/tdwg/dwc/issues) and [Darwin Core QA issues](https://github.com/tdwg/dwc-qa/issues/)). Information about how to suggest changes to the standard can be found at the [Guidelines for Contributing](https://github.com/tdwg/dwc/blob/master/.github/CONTRIBUTING.md) page.

## Scope of Darwin Core

What is in scope?

- Collections of any kind of biological objects or data.
- Terminology associated with biological collection data.
- Striving for compatibility with other biodiversity-related standards.
- Facilitating the addition of components and attributes of biological data.

What is not in scope?

- Data interchange protocols.
- Non-biodiversity-related data.
- Purely taxonomic data.

## Audience

- Biodiversity data holders (organizations, institutions, researchers).
- Consumers of biodiversity data.
- Developers of collections management systems.
- Other TDWG interest and task groups.
- Protocol developers (TAPIR).
- Biodiversity network developers.

## Contributors

[List of contributors](https://github.com/tdwg/dwc/contributors)

## Resources

- Quick Reference Guide <https://dwc.tdwg.org/terms/>
- Maintenance group: <https://www.tdwg.org/community/dwc/>
- Primary collaboration platform: <https://github.com/tdwg/dwc>
- Darwin Core Questions & Answers: <https://github.com/tdwg/dwc-qa>
- Darwin Core landing page (this page): <https://www.tdwg.org/standards/dwc/>

## Parts of the standard

This standard is comprised of 5 vocabularies and 11 documents. 

Vocabularies:

Darwin Core main vocabulary (<http://rs.tdwg.org/dwc/>)
establishmentMeans controlled vocabulary (<http://rs.tdwg.org/dwcem/>)
degreeOfEstablishment controlled vocabulary (<http://rs.tdwg.org/dwcdoe/>)
pathway controlled vocabulary (<http://rs.tdwg.org/dwcpw/>)
Darwin Core Chronometric Age Extension vocabulary (<http://rs.tdwg.org/chrono/>)

Documents:

**Title:** Darwin Core RDF Guide \
**Permanent IRI:** [http://rs.tdwg.org/dwc/terms/guides/rdf/](https://dwc.tdwg.org/rdf/) \
**Created:** 2015-06-02 \
**Last modified:** 2015-06-02 \
**Contributors:** \
Steve Baskauf (lead author) - TDWG RDF/OWL Task Group \
John Wieczorek (author) - TDWG Darwin Core Task Group \
John Deck  (author) - Genomic Biodiversity Working Group \
Campbell Webb  (author) - TDWG RDF/OWL Task Group \
Paul J. Morris  (author) - Harvard University Herbaria/Museum of Comparative Zoölogy \
Mark Schildhauer  (author) - National Center for Ecological Analysis and Synthesis \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** This guide is intended to facilitate the use of Darwin Core terms in the Resource Description Framework (RDF). It explains basic features of RDF and provides details of how to expose data in the form of RDF using Darwin Core terms and terms from other key vocabularies. It defines terms in the namespace http://rs.tdwg.org/dwc/iri/ which are intended for use excusively with non-literal objects.  \
**Citation:** Darwin Core and RDF/OWL Task Groups. 2015. Darwin Core RDF Guide. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/terms/guides/rdf/

**Title:** Darwin Core Text Guide \
**Permanent IRI:** [http://rs.tdwg.org/dwc/terms/guides/text/](https://dwc.tdwg.org/text/) \
**Created:** 2014-11-08 \
**Last modified:** 2014-11-08 \
**Contributors:** \
Tim Robertson (lead author) - Global Biodiversity Information Facility \
Markus Döring (author) - Global Biodiversity Information Facility \
John Wieczorek (author) - TDWG Darwin Core Task Group \
Renato De Giovanni (author) - Centro de Referência em Informação Ambiental \
Dave Vieglais (author) - KU Natural History Museum \
Gail E. Kampmeier (review manager) - University of Illinois at Urbana-Champaign \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** This document provides guidelines for implementing Darwin Core in Text files. \
**Citation:** Darwin Core Task Group. 2014. Darwin Core Text Guide. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/terms/guides/text/

**Title:** Darwin Core XML Guide \
**Permanent IRI:** [http://rs.tdwg.org/dwc/terms/guides/xml/](https://dwc.tdwg.org/xml/) \
**Created:** 2014-11-08 \
**Last modified:** 2014-11-08 \
**Contributors:** \
John Wieczorek (lead author) - Museum of Vertebrate Zoology at Berkeley \
Markus Döring (author) - Global Biodiversity Information Facility \
Renato De Giovanni (author) - Centro de Referência em Informação Ambiental \
Tim Robertson (author) - Global Biodiversity Information Facility \
Dave Vieglais (author) - KU Natural History Museum \
Gail E. Kampmeier (review manager) - University of Illinois at Urbana-Champaign \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** This document provides guidelines for the implementation of Darwin Core in XML. \
**Citation:** Darwin Core Task Group. 2014. Darwin Core XML Guide. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/terms/guides/xml/

**Title:** Simple Darwin Core \
**Permanent IRI:** [http://rs.tdwg.org/dwc/terms/simple/](https://dwc.tdwg.org/simple/) \
**Created:** 2014-11-08 \
**Last modified:** 2014-11-08 \
**Contributors:** \
John Wieczorek (lead author) - Museum of Vertebrate Zoology at Berkeley \
Markus Döring (author) - Global Biodiversity Information Facility \
Renato De Giovanni (author) - Centro de Referência em Informação Ambiental \
Tim Robertson (author) - Global Biodiversity Information Facility \
Dave Vieglais (author) - KU Natural History Museum \
Gail E. Kampmeier (review manager) - University of Illinois at Urbana-Champaign \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** This document is a reference for the Simple Darwin Core standard, a mechanism used to share biodiversity information using the simplest methods and structure.   \
**Citation:** Darwin Core Task Group. 2014. Simple Darwin Core. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/terms/simple/

**Title:** Darwin Core Namespace Policy \
**Permanent IRI:** [http://rs.tdwg.org/dwc/terms/namespace/](https://dwc.tdwg.org/namespace/) \
**Created:** 2014-11-08 \
**Last modified:** 2014-11-08 \
**Contributors:** \
John Wieczorek (lead author) - Museum of Vertebrate Zoology at Berkeley \
Markus Döring (author) - Global Biodiversity Information Facility \
Renato De Giovanni (author) - Centro de Referência em Informação Ambiental \
Tim Robertson (author) - Global Biodiversity Information Facility \
Dave Vieglais (author) - KU Natural History Museum \
Gail E. Kampmeier (review manager) - University of Illinois at Urbana-Champaign \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** All terms in the Darwin Core must be assigned a unique Uniform Resource Identifier (URI). For convenience, the term URIs that are assigned and managed by the Darwin Core Task Group are grouped into collections known as Darwin Core namespaces. This document describes how term URIs are allocated by the Darwin Core Task Group and the policies associated with Darwin Core namespaces.  \
**Citation:** Darwin Core Task Group. 2014. Darwin Core Namespace Policy. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/terms/namespace/

**Title:** Darwin Core List of Terms \
**Permanent IRI:** [http://rs.tdwg.org/dwc/doc/list/](https://dwc.tdwg.org/list/) \
**Created:** 2020-08-12 \
**Last modified:** 2021-07-15 \
**Contributors:** \
John Wieczorek (contributor) - VertNet \
Peter Desmet (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Steve Baskauf (contributor) - Vanderbilt University Libraries \
Tim Robertson (contributor) - Global Biodiversity Information Facility \
Markus Döring (contributor) - Global Biodiversity Information Facility \
Quentin Groom (contributor) - Botanic Garden Meise \
Stijn Van Hoey (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
David Bloom (contributor) - VertNet \
Paula Zermoglio (contributor) - VertNet \
Robert Guralnick (contributor) - University of Florida \
John Deck (contributor) - Genomic Biodiversity Working Group \
Gail Kampmeier (review manager) - Illinois Natural History Survey \
Dave Vieglais (contributor) - KU Natural History Museum \
Renato De Giovanni (contributor) - Centro de Referência em Informação Ambiental \
Campbell Webb (contributor) - TDWG RDF/OWL Task Group \
Paul J. Morris (contributor) - Harvard University Herbaria/Museum of Comparative Zoölogy \
Mark Schildhauer (contributor) - National Center for Ecological Analysis and Synthesis \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** Darwin Core is a vocabulary standard for transmitting information about biodiversity. This document lists all terms in namespaces currently used in the vocabulary. \
**Citation:** Darwin Core Maintenance Group. 2021. List of Darwin Core terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/list/2021-07-15

**Title:** Degree of Establishment Controlled Vocabulary List of Terms \
**Permanent IRI:** [http://rs.tdwg.org/dwc/doc/doe/](https://dwc.tdwg.org/doe/) \
**Created:** 2020-10-13 \
**Last modified:** 2020-10-13 \
**Contributors:** \
Quentin Groom (lead author) - Botanic Garden Meise \
Peter Desmet (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Lien Reyserhove (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Tim Adriaens (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Damiano Oldoni (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Sonia Vanderhoeven (contributor) - Belgian Biodiversity Platform \
Steve Baskauf (contributor) - Vanderbilt University Libraries \
Arthur Chapman (contributor) - Australian Biodiversity Information Services \
Melodie McGeoch (contributor) - McGeoch Research Group \
Ramona Walls (contributor) - University of Arizona \
John Wieczorek (contributor) - VertNet \
John R.U. Wilson (contributor) - South African National Biodiversity Institute \
Paula F F Zermoglio (contributor) - VertNet \
Annie Simpson (contributor) - U.S. Geological Survey \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** The Darwin Core term degreeOfEstablishment provides information about degree to which an Organism survives, reproduces, and expands its range at the given place and time.. The Degree of Establishment Controlled Vocabulary provides terms that should be used as values for dwc:degreeOfEstablishment and dwciri:degreeOfEstablishment. \
**Citation:** Darwin Core Maintenance Group. 2020. Degree of Establishment Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/doe/2020-10-13

**Title:** Establishment Means Controlled Vocabulary List of Terms \
**Permanent IRI:** [http://rs.tdwg.org/dwc/doc/em/](https://dwc.tdwg.org/em/) \
**Created:** 2020-10-13 \
**Last modified:** 2020-10-13 \
**Contributors:** \
Quentin Groom (lead author) - Botanic Garden Meise \
Peter Desmet (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Lien Reyserhove (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Tim Adriaens (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Damiano Oldoni (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Sonia Vanderhoeven (contributor) - Belgian Biodiversity Platform \
Steve Baskauf (contributor) - Vanderbilt University Libraries \
Arthur Chapman (contributor) - Australian Biodiversity Information Services \
Melodie McGeoch (contributor) - McGeoch Research Group \
Ramona Walls (contributor) - University of Arizona \
John Wieczorek (contributor) - VertNet \
John R.U. Wilson (contributor) - South African National Biodiversity Institute \
Paula F F Zermoglio (contributor) - VertNet \
Annie Simpson (contributor) - U.S. Geological Survey \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** The Darwin Core term establishmentMeans provides information about whether an organism or organisms have been introduced to a given place and time through the direct or indirect activity of modern humans. The Establishment Means Controlled Vocabulary provides terms that should be used as values for dwc:establishmentMeans and dwciri:establishmentMeans. \
**Citation:** Darwin Core Maintenance Group. 2020. Establishment Means Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/em/2020-10-13

**Title:** Pathway Controlled Vocabulary List of Terms \
**Permanent IRI:** [http://rs.tdwg.org/dwc/doc/pw/](https://dwc.tdwg.org/pw/) \
**Created:** 2020-10-13 \
**Last modified:** 2020-10-13 \
**Contributors:** \
Quentin Groom (lead author) - Botanic Garden Meise \
Peter Desmet (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Lien Reyserhove (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Tim Adriaens (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Damiano Oldoni (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) \
Sonia Vanderhoeven (contributor) - Belgian Biodiversity Platform \
Steve Baskauf (contributor) - Vanderbilt University Libraries \
Arthur Chapman (contributor) - Australian Biodiversity Information Services \
Melodie McGeoch (contributor) - McGeoch Research Group \
Ramona Walls (contributor) - University of Arizona \
John Wieczorek (contributor) - VertNet \
John R.U. Wilson (contributor) - South African National Biodiversity Institute \
Paula F F Zermoglio (contributor) - VertNet \
Annie Simpson (contributor) - U.S. Geological Survey \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** The Darwin Core term pathway provides information about the process by which an Organism came to be in a given place at a given time. The Pathway Controlled Vocabulary provides terms that should be used as values for dwc:pathway and dwciri:pathway. \
**Citation:** Darwin Core Maintenance Group. 2020. Pathway Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/pw//2020-10-13

**Title:** Chronometric Age Vocabulary List of Terms \
**Permanent IRI:** [http://rs.tdwg.org/dwc/doc/chrono/](https://tdwg.github.io/chrono/list/) \
**Created:** 2021-04-27 \
**Last modified:** 2021-04-27 \
**Contributors:** \
John Wieczorek (lead author) - VertNet \
Laura Brenskelle (contributor) - University of Florida \
Robert Guralnick (contributor) - University of Florida \
Kitty Emery (contributor) - University of Florida \
Michelle LeFebvre (contributor) - University of Florida \
Neill Wallis (contributor) - University of Florida \
Steve Baskauf (contributor) - Vanderbilt University Libraries \
Marie Elise Lecoq (contributor) \
Eric Kansa (contributor) - Harvard University \
Sarah Kansa (contributor) - The Alexandria Archive Institute \
Denné Reed (contributor) - University of Texas at Austin \
**Publisher:** Biodiversity Information Standards (TDWG) \
**Abstract:** The Chronometric Age Vocabulary is a standard for transmitting information about chronometric ages - the processes and results of an assay or other analysis used to determine the age of a MaterialSample. This document lists all terms in namespaces currently used in the vocabulary. \
**Citation:** TDWG Darwin Core Chronometric Age Extension Task Group. 2021. Chronometric Age Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/chrono/2021-04-27

