---
title: Darwin Core
summary: Darwin Core is our most popular standard for sharing biodiversity information.
cover_image: https://images.unsplash.com/photo-1492031215329-791748ee1253
cover_image_by: Alex Guillaume
cover_image_ref: https://unsplash.com/photos/0MC0o-xLucM
tags: technical specification, current standard, 2009
github: https://github.com/tdwg/dwc
---

## Header section

Title
: Darwin Core

IRI to be cited and linked
: <http://www.tdwg.org/standards/450>

Publisher
: [Biodiversity Information Standards (TDWG)](https://www.tdwg.org/)

Status
: Current Standard

Ratified
: 2009-10-09

Abstract
: The Darwin Core is a set of terms and definitions that facilitate the exchange of information about the geographic occurrence of organisms and the physical existence of biotic specimens in collections. Extensions to the Darwin Core provide a mechanism to share additional information, which may be discipline-specific, or beyond the commonly agreed upon scope of the Darwin Core itself. The Darwin Core and its extensions are primarily focused on intended semantics (definitions) and impose relatively few constraints on format or encoding. This makes the standard maximally useful in data publishing (reduces barriers), and enables the standard to support pipelines and other tools that can incrementally improve data quality.

Preferred citation
: Darwin Core Task Group (2009) Darwin Core (G. Kampmeier, review manager). Biodiversity Information Standards (TDWG). <http://www.tdwg.org/standards/450>

## Parts of the standard

The Darwin Core standard is comprised of one vocabulary, the Darwin Core vocabulary (<http://rs.tdwg.org/dwc/>), and five documents:

- [Simple Darwin Core Guide](http://rs.tdwg.org/dwc/terms/simple/) - a guide for sharing information using the simplest methods
- [Darwin Core Text Guide](http://rs.tdwg.org/dwc/terms/guides/text/) - a guide for sharing information using text files
- [Darwin Core XML Guide](http://rs.tdwg.org/dwc/terms/guides/xml/) - a guide for constructing application schemas using XML
- [Darwin Core RDF Guide](http://rs.tdwg.org/dwc/terms/guides/rdf/) - a guide for encoding biodiversity data using the Resource Description Framework (RDF)
- [Darwin Core Namespace Policy](http://rs.tdwg.org/dwc/terms/namespace/) - an explanation of how URIs for Darwin Core terms should be constructed

## Maintenance Group

Modifications and enhancements to Darwin Core are managed by the [Darwin Core Maintenance Group]({filename}maintenance/index.md).

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

- Resource directory: <http://rs.tdwg.org/dwc/>
- Maintenance group: [this subpage]({filename}maintenance/index.md)
- Primary collaboration platform: <https://github.com/tdwg/dwc>
- Darwin Core Questions & Answers: <https://github.com/tdwg/dwc-qa>
- Darwin Core landing page: [this page](https://www.tdwg.org/standards/dwc/)
