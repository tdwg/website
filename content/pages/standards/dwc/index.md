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

**Title:** Darwin Core RDF Guide <br/>
**Permanent IRI:** [http://rs.tdwg.org/dwc/terms/guides/rdf/](https://dwc.tdwg.org/rdf/) <br/>
**Created:** 2015-06-02 <br/>
**Last modified:** 2015-06-02 <br/>
**Contributors:** <br/>
Steve Baskauf (lead author) - TDWG RDF/OWL Task Group <br/>
John Wieczorek (author) - TDWG Darwin Core Task Group <br/>
John Deck  (author) - Genomic Biodiversity Working Group <br/>
Campbell Webb  (author) - TDWG RDF/OWL Task Group <br/>
Paul J. Morris  (author) - Harvard University Herbaria/Museum of Comparative Zoölogy <br/>
Mark Schildhauer  (author) - National Center for Ecological Analysis and Synthesis <br/>
**Publisher:** Biodiversity Information Standards (TDWG) <br/>
**Abstract:** This guide is intended to facilitate the use of Darwin Core terms in the Resource Description Framework (RDF). It explains basic features of RDF and provides details of how to expose data in the form of RDF using Darwin Core terms and terms from other key vocabularies. It defines terms in the namespace http://rs.tdwg.org/dwc/iri/ which are intended for use excusively with non-literal objects.  <br/>
**Citation:** Darwin Core and RDF/OWL Task Groups. 2015. Darwin Core RDF Guide. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/terms/guides/rdf/

**Title:** Darwin Core Text Guide <br/>
**Permanent IRI:** [http://rs.tdwg.org/dwc/terms/guides/text/](https://dwc.tdwg.org/text/) <br/>
**Created:** 2014-11-08 <br/>
**Last modified:** 2014-11-08 <br/>
**Contributors:** <br/>
Tim Robertson (lead author) - Global Biodiversity Information Facility <br/>
Markus Döring (author) - Global Biodiversity Information Facility <br/>
John Wieczorek (author) - TDWG Darwin Core Task Group <br/>
Renato De Giovanni (author) - Centro de Referência em Informação Ambiental <br/>
Dave Vieglais (author) - KU Natural History Museum <br/>
Gail E. Kampmeier (review manager) - University of Illinois at Urbana-Champaign <br/>
**Publisher:** Biodiversity Information Standards (TDWG) <br/>
**Abstract:** This document provides guidelines for implementing Darwin Core in Text files. <br/>
**Citation:** Darwin Core Task Group. 2014. Darwin Core Text Guide. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/terms/guides/text/

**Title:** Darwin Core XML Guide <br/>
**Permanent IRI:** [http://rs.tdwg.org/dwc/terms/guides/xml/](https://dwc.tdwg.org/xml/) <br/>
**Created:** 2014-11-08 <br/>
**Last modified:** 2014-11-08 <br/>
**Contributors:** <br/>
John Wieczorek (lead author) - Museum of Vertebrate Zoology at Berkeley <br/>
Markus Döring (author) - Global Biodiversity Information Facility <br/>
Renato De Giovanni (author) - Centro de Referência em Informação Ambiental <br/>
Tim Robertson (author) - Global Biodiversity Information Facility <br/>
Dave Vieglais (author) - KU Natural History Museum <br/>
Gail E. Kampmeier (review manager) - University of Illinois at Urbana-Champaign <br/>
**Publisher:** Biodiversity Information Standards (TDWG) <br/>
**Abstract:** This document provides guidelines for the implementation of Darwin Core in XML. <br/>
**Citation:** Darwin Core Task Group. 2014. Darwin Core XML Guide. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/terms/guides/xml/

**Title:** Simple Darwin Core <br/>
**Permanent IRI:** [http://rs.tdwg.org/dwc/terms/simple/](https://dwc.tdwg.org/simple/) <br/>
**Created:** 2014-11-08 <br/>
**Last modified:** 2014-11-08 <br/>
**Contributors:** <br/>
John Wieczorek (lead author) - Museum of Vertebrate Zoology at Berkeley <br/>
Markus Döring (author) - Global Biodiversity Information Facility <br/>
Renato De Giovanni (author) - Centro de Referência em Informação Ambiental <br/>
Tim Robertson (author) - Global Biodiversity Information Facility <br/>
Dave Vieglais (author) - KU Natural History Museum <br/>
Gail E. Kampmeier (review manager) - University of Illinois at Urbana-Champaign <br/>
**Publisher:** Biodiversity Information Standards (TDWG) <br/>
**Abstract:** This document is a reference for the Simple Darwin Core standard, a mechanism used to share biodiversity information using the simplest methods and structure.   <br/>
**Citation:** Darwin Core Task Group. 2014. Simple Darwin Core. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/terms/simple/

**Title:** Darwin Core Namespace Policy <br/>
**Permanent IRI:** [http://rs.tdwg.org/dwc/terms/namespace/](https://dwc.tdwg.org/namespace/) <br/>
**Created:** 2014-11-08 <br/>
**Last modified:** 2014-11-08 <br/>
**Contributors:** <br/>
John Wieczorek (lead author) - Museum of Vertebrate Zoology at Berkeley <br/>
Markus Döring (author) - Global Biodiversity Information Facility <br/>
Renato De Giovanni (author) - Centro de Referência em Informação Ambiental <br/>
Tim Robertson (author) - Global Biodiversity Information Facility <br/>
Dave Vieglais (author) - KU Natural History Museum <br/>
Gail E. Kampmeier (review manager) - University of Illinois at Urbana-Champaign <br/>
**Publisher:** Biodiversity Information Standards (TDWG) <br/>
**Abstract:** All terms in the Darwin Core must be assigned a unique Uniform Resource Identifier (URI). For convenience, the term URIs that are assigned and managed by the Darwin Core Task Group are grouped into collections known as Darwin Core namespaces. This document describes how term URIs are allocated by the Darwin Core Task Group and the policies associated with Darwin Core namespaces.  <br/>
**Citation:** Darwin Core Task Group. 2014. Darwin Core Namespace Policy. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/terms/namespace/

**Title:** Darwin Core List of Terms <br/>
**Permanent IRI:** [http://rs.tdwg.org/dwc/doc/list/](https://dwc.tdwg.org/list/) <br/>
**Created:** 2020-08-12 <br/>
**Last modified:** 2021-07-15 <br/>
**Contributors:** <br/>
John Wieczorek (contributor) - VertNet <br/>
Peter Desmet (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Steve Baskauf (contributor) - Vanderbilt University Libraries <br/>
Tim Robertson (contributor) - Global Biodiversity Information Facility <br/>
Markus Döring (contributor) - Global Biodiversity Information Facility <br/>
Quentin Groom (contributor) - Botanic Garden Meise <br/>
Stijn Van Hoey (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
David Bloom (contributor) - VertNet <br/>
Paula Zermoglio (contributor) - VertNet <br/>
Robert Guralnick (contributor) - University of Florida <br/>
John Deck (contributor) - Genomic Biodiversity Working Group <br/>
Gail Kampmeier (review manager) - Illinois Natural History Survey <br/>
Dave Vieglais (contributor) - KU Natural History Museum <br/>
Renato De Giovanni (contributor) - Centro de Referência em Informação Ambiental <br/>
Campbell Webb (contributor) - TDWG RDF/OWL Task Group <br/>
Paul J. Morris (contributor) - Harvard University Herbaria/Museum of Comparative Zoölogy <br/>
Mark Schildhauer (contributor) - National Center for Ecological Analysis and Synthesis <br/>
**Publisher:** Biodiversity Information Standards (TDWG) <br/>
**Abstract:** Darwin Core is a vocabulary standard for transmitting information about biodiversity. This document lists all terms in namespaces currently used in the vocabulary. <br/>
**Citation:** Darwin Core Maintenance Group. 2021. List of Darwin Core terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/list/2021-07-15

**Title:** Degree of Establishment Controlled Vocabulary List of Terms <br/>
**Permanent IRI:** [http://rs.tdwg.org/dwc/doc/doe/](https://dwc.tdwg.org/doe/) <br/>
**Created:** 2020-10-13 <br/>
**Last modified:** 2020-10-13 <br/>
**Contributors:** <br/>
Quentin Groom (lead author) - Botanic Garden Meise <br/>
Peter Desmet (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Lien Reyserhove (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Tim Adriaens (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Damiano Oldoni (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Sonia Vanderhoeven (contributor) - Belgian Biodiversity Platform <br/>
Steve Baskauf (contributor) - Vanderbilt University Libraries <br/>
Arthur Chapman (contributor) - Australian Biodiversity Information Services <br/>
Melodie McGeoch (contributor) - McGeoch Research Group <br/>
Ramona Walls (contributor) - University of Arizona <br/>
John Wieczorek (contributor) - VertNet <br/>
John R.U. Wilson (contributor) - South African National Biodiversity Institute <br/>
Paula F F Zermoglio (contributor) - VertNet <br/>
Annie Simpson (contributor) - U.S. Geological Survey <br/>
**Publisher:** Biodiversity Information Standards (TDWG) <br/>
**Abstract:** The Darwin Core term degreeOfEstablishment provides information about degree to which an Organism survives, reproduces, and expands its range at the given place and time.. The Degree of Establishment Controlled Vocabulary provides terms that should be used as values for dwc:degreeOfEstablishment and dwciri:degreeOfEstablishment. <br/>
**Citation:** Darwin Core Maintenance Group. 2020. Degree of Establishment Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/doe/2020-10-13

**Title:** Establishment Means Controlled Vocabulary List of Terms <br/>
**Permanent IRI:** [http://rs.tdwg.org/dwc/doc/em/](https://dwc.tdwg.org/em/) <br/>
**Created:** 2020-10-13 <br/>
**Last modified:** 2020-10-13 <br/>
**Contributors:** <br/>
Quentin Groom (lead author) - Botanic Garden Meise <br/>
Peter Desmet (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Lien Reyserhove (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Tim Adriaens (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Damiano Oldoni (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Sonia Vanderhoeven (contributor) - Belgian Biodiversity Platform <br/>
Steve Baskauf (contributor) - Vanderbilt University Libraries <br/>
Arthur Chapman (contributor) - Australian Biodiversity Information Services <br/>
Melodie McGeoch (contributor) - McGeoch Research Group <br/>
Ramona Walls (contributor) - University of Arizona <br/>
John Wieczorek (contributor) - VertNet <br/>
John R.U. Wilson (contributor) - South African National Biodiversity Institute <br/>
Paula F F Zermoglio (contributor) - VertNet <br/>
Annie Simpson (contributor) - U.S. Geological Survey <br/>
**Publisher:** Biodiversity Information Standards (TDWG) <br/>
**Abstract:** The Darwin Core term establishmentMeans provides information about whether an organism or organisms have been introduced to a given place and time through the direct or indirect activity of modern humans. The Establishment Means Controlled Vocabulary provides terms that should be used as values for dwc:establishmentMeans and dwciri:establishmentMeans. <br/>
**Citation:** Darwin Core Maintenance Group. 2020. Establishment Means Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/em/2020-10-13

**Title:** Pathway Controlled Vocabulary List of Terms <br/>
**Permanent IRI:** [http://rs.tdwg.org/dwc/doc/pw/](https://dwc.tdwg.org/pw/) <br/>
**Created:** 2020-10-13 <br/>
**Last modified:** 2020-10-13 <br/>
**Contributors:** <br/>
Quentin Groom (lead author) - Botanic Garden Meise <br/>
Peter Desmet (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Lien Reyserhove (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Tim Adriaens (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Damiano Oldoni (contributor) - Instituut voor Natuur- en Bosonderzoek (INBO) <br/>
Sonia Vanderhoeven (contributor) - Belgian Biodiversity Platform <br/>
Steve Baskauf (contributor) - Vanderbilt University Libraries <br/>
Arthur Chapman (contributor) - Australian Biodiversity Information Services <br/>
Melodie McGeoch (contributor) - McGeoch Research Group <br/>
Ramona Walls (contributor) - University of Arizona <br/>
John Wieczorek (contributor) - VertNet <br/>
John R.U. Wilson (contributor) - South African National Biodiversity Institute <br/>
Paula F F Zermoglio (contributor) - VertNet <br/>
Annie Simpson (contributor) - U.S. Geological Survey <br/>
**Publisher:** Biodiversity Information Standards (TDWG) <br/>
**Abstract:** The Darwin Core term pathway provides information about the process by which an Organism came to be in a given place at a given time. The Pathway Controlled Vocabulary provides terms that should be used as values for dwc:pathway and dwciri:pathway. <br/>
**Citation:** Darwin Core Maintenance Group. 2020. Pathway Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/pw//2020-10-13

**Title:** Chronometric Age Vocabulary List of Terms <br/>
**Permanent IRI:** [http://rs.tdwg.org/dwc/doc/chrono/](https://tdwg.github.io/chrono/list/) <br/>
**Created:** 2021-04-27 <br/>
**Last modified:** 2021-04-27 <br/>
**Contributors:** <br/>
John Wieczorek (lead author) - VertNet <br/>
Laura Brenskelle (contributor) - University of Florida <br/>
Robert Guralnick (contributor) - University of Florida <br/>
Kitty Emery (contributor) - University of Florida <br/>
Michelle LeFebvre (contributor) - University of Florida <br/>
Neill Wallis (contributor) - University of Florida <br/>
Steve Baskauf (contributor) - Vanderbilt University Libraries <br/>
Marie Elise Lecoq (contributor) <br/>
Eric Kansa (contributor) - Harvard University <br/>
Sarah Kansa (contributor) - The Alexandria Archive Institute <br/>
Denné Reed (contributor) - University of Texas at Austin <br/>
**Publisher:** Biodiversity Information Standards (TDWG) <br/>
**Abstract:** The Chronometric Age Vocabulary is a standard for transmitting information about chronometric ages - the processes and results of an assay or other analysis used to determine the age of a MaterialSample. This document lists all terms in namespaces currently used in the vocabulary. <br/>
**Citation:** TDWG Darwin Core Chronometric Age Extension Task Group. 2021. Chronometric Age Vocabulary List of Terms. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/dwc/doc/chrono/2021-04-27

