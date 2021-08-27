---
title: OSR - Material Sample
summary: this task group will investigate and make recommendations on current shortcomings in the capacity to share, re-use, compare, and relate physical objects to one another and to other concepts, and further integrate with other sources of biodiversity data.
cover_image:
cover_image_by:
cover_image_ref:
tags: task group
github: https://github.com/tdwg/material-sample
status: published
---


# MaterialSample Task Group Charter <br />A Task Group of Observation & Specimen Records Interest Group


## 1. Convenors 

+ Teresa J. Mayfield-Meyer | Arctos | [jegelewicz66@gmail.com](jegelewicz66@gmail.com) | @Jegelewicz 


## 2. Core Members 

+ John Wieczorek | VertNet - Darwin Core Maintenance Interest Group | [gtuco.btuco@gmail.com)](gtuco.btuco@gmail.com) | @tucotuco 
+ Richard L. Pyle | Bernice P. Bishop Museum | [deepreef@bishopmuseum.org](deepreef@bishopmuseum.org) | @deepreef 
+ Steve Baskauf | Vanderbilt University - Darwin Core Maintenance Interest Group | [steve.baskauf@vanderbilt.edu](steve.baskauf@vanderbilt.edu) | @baskaufs 
+ Rob Guralnick | Florida Museum of Natural History | [rguralnick@flmnh.ufl.edu](rguralnick@flmnh.ufl.edu) | @robgur
+ Sharon Grant | The Field Museum | s[grant@fieldmuseum.org](grant@fieldmuseum.org) | @rondlg
+ Roger Burkhalter | Sam Noble Museum of Natural History at the University of Oklahoma | [rjb@ou.edu](rjb@ou.edu) | @RogerBurkhalter 
+ Tim Robertson | GBIF | t[robertson@gbif.org](robertson@gbif.org) | @timrobertson100 
+ Matt Woodburn | DiSSCo | [m.woodburn@nhm.ac.uk](m.woodburn@nhm.ac.uk) | @mswoodburn
+ Christian Bölling | Museum für Naturkunde Berlin & DINA Consortium | christian.boelling@mfn.berlin | @cboelling 
+ Gabi Droege | GGBN | [g.droege@bgbm.org](g.droege@bgbm.org) | @gdadade 
+ Quentin Groom | Observations & Specimens Interest Group | [quentin.groom@plantentuinmeise.be](quentin.groom@plantentuinmeise.be) | @qgroom 
+ Simon Cox | CSIRO | [simon.cox@csiro.au](simon.cox@csiro.au) | @dr-shorthair 
+ Abby Benson | USGS | [albenson@usgs.gov](albenson@usgs.gov) | @albenson-usgs 
+ Anne Fuchs | Australian National Botanic Gardens | A[nne.Fuchs@environment.gov.au](nne.Fuchs@environment.gov.au) | @afuchs1 
+ Dave Vieglais | University of Kansas | [dave.vieglais@gmail.com](dave.vieglais@gmail.com) | @datadavev 
+ Dag Endresen | University of Oslo | [dag.endresen@gmail.com](dag.endresen@gmail.com) | @dagendresen
+ Greg Whitbread | | [taxamatics@gmail.com](taxamatics@gmail.com) | @ghwhitbread 
+ Stephen Richard | U.S. Geoscience Information Network | [smrTucson@gmail.com](smrTucson@gmail.com) | @smrgeoinfo 
+ Jutta Buschbom | Global Collections Network | j[utta.buschbom@statistical-genetics.de](utta.buschbom@statistical-genetics.de) | @jbstatgen 
+ Michael Hope | CSIRO | [Michael.Hope@csiro.au](Michael.Hope@csiro.au) | @m-hope 
+ Stan Blum | TDWG | stanblum@gmail.com | @stanblum 


## 3. Motivation 

Members of the Arctos Working Group feel that [MaterialSample]() and [PreservedSpecimen]() are currently interchangeable. See [ArctosDB/arctos#2432]() for further discussion. The Global Genome Biodiversity Network ([GGBN]()) community is using the Occurrence class currently as a MaterialSample class, as there is no alternative available right now if we want to publish information to aggregators such as the Global Biodiversity Information Facility ([GBIF](https://www.gbif.org)). It became apparent in the [TDWG issue]() about this change request that other issues pertaining to the representation of settings and events in which material samples occur need clarification too. There are terms in the Occurrence class that feel unnatural there, and the distinction between Darwin Core terms that are related to physical objects<sup>1</sup> feels arbitrary. 

The purpose of this task group is to investigate and make recommendations on current shortcomings in the capacity to share, re-use, compare, and relate physical objects to one another and to other concepts, and further integrate with other sources of biodiversity data. 


## 4. Goals Outputs and Outcomes 


### Scope 


While Darwin Core is described as a bag of terms, users do apply additional semantics to it for different application goals, and this needs to be addressed. Developing a model within the limited scope of the properties and direct relationships of MaterialSample to other classes would be an ideal outcome of this group. The scope of any such modelling is expected to include the classes to be defined below and would possibly include the relationships of MaterialSample to _Identification_, _Occurrence_, _Organism_, and _MeasurementOrFact_. 

### Goals

Our **main goal** is to enable physical object data sharing as part of the TDWG corpus of standards. The **primary deliverable** will be revised formal definitions of the terms below with appropriate use case examples following the Darwin Core format, adapted from the original definitions currently provided in Darwin Core. This does not depend upon any other tasks/goals of the Task Group. 

+ [MaterialSample]() 
+ [PreservedSpecimen]() 
+ [LivingSpecimen]() 
+ [FossilSpecimen]() 

**Other deliverables.**

The primary deliverable will be accompanied by a review of the following properties that fall under [Occurrence](), but seem to be properties of one of the above. The task group will make a recommendation for each of these terms as to which class in the Darwin Core standard these properties belong which may also include recommendations for terms being revised, added, disambiguated, or deprecated. Depends upon definitions provided above. 

+ [catalogNumber]() 
+ [preparations]() 
+ [disposition]() 
+ [associatedSequences]() 
+ [otherCatalogNumbers]() 
+ [BasisOfRecord]() 
  - Recommendations will be provided for a revised formal definition as it pertains to materialSample but will not consider other data types. 

**Other documentation**

We intend to document the rationale for creating revised definitions, particularly as these revisions promote physical object data sharing. This documentation should enable the relevant communities of practice (e.g., natural history collecations managers) to understand the fundamental concepts, avoiding technical jargon wherever possible.  Documentation and recommendations may include:

+ Use cases and examples 
+ Suggest new terms if needed (e.g. preservationType)  
+ Alignments/mappings to related standards, ontologies and vocabularies when possible and desirable 


## 5. Strategy 

The task group will develop term definitions using GitHub issues in the GitHub repository (https://github.com/tdwg/material-sample) from TDWG GitHub organization. Monthly meetings in a virtual platform will ensure that the task group remains active and working on the deliverables. Specific examples of the ways these terms are used by collection management systems will inform the definitions and recommendations. Members of related Interest and Task Groups are core members of this Task Group to ensure different use cases are addressed. 


## 6. Becoming Involved 

Individuals having an interest in this work should contact the conveners, and are invited to watch and contribute via the GitHub repository ([https://github.com/tdwg/material-sample]()). 

A mailing list is used for discussion outside of GitHub, and is open to follow or join ([http://lists.tdwg.org/mailman/listinfo/dwc-material-sample]()) 


## 7. History/Context 

See Motivation


## 8. Summary 

This task group will review Darwin Core terms related to physical objects<sup>1</sup> and how they may change over time, with the goal of enabling data about physical objects to be shared, re-used, compared to one another, and further integrated with other sources of biodiversity data. The outcome will be to provide clear semantics for physical object classes and properties with possible recommendations for changes to the class associated with some properties. 

<div><sup>1</sup>1 Physical object - In common usage and classical mechanics, a physical object or physical body (or simply an object or body) is a collection of matter within a defined contiguous boundary in three-dimensional space. -- [Wikipedia](https://en.wikipedia.org/wiki/Physical_object)</div>

## 9. Resources 

### TDWG Documentation
 - TDWG Vocabulary Maintenance Specification (VMS): https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md
 - TDWG Standards Documentation Standard (SDS): https://github.com/tdwg/vocab/blob/master/sds/documentation-specification.md
 - Material Sample Core definition:  https://tools.gbif.org/dwca-validator/extension.do?id=dwc:MaterialSample.

### Other resources and references:
 - Dublin Core Terms: dcmitype:PhysicalObject | dcterms:PhysicalResource | dcterms:PhysicalMedium 
 - Biological Collections Ontology (BCO): http://www.obofoundry.org/ontology/bco
 - Darwin-SW: https://github.com/darwin-sw/dsw/blob/master/README.md
 - GGBN Data Standard: https://terms.tdwg.org/GGBN_Data_Standard
 - ABCD's accessionStatus: https://abcd.tdwg.org/terms/#accessionStatus
 - CIDOC Conceptual Reference Model (CRM) is a theoretical and practical tool for information integration in the field of cultural heritage: Home | CIDOC CRM (cidoc-crm.org)
 - Looking ahead: GBIF data model - https://vimeo.com/564600741
 - SSN Ontology, in particular the classes `sosa:Sample` and `sosa:Sampling` - https://www.w3.org/TR/vocab-ssn/#Sampling
 - SSN Extension ontology, in particular sample-chains - https://www.w3.org/TR/vocab-ssn-ext/#sample-chains 
 - International Geosample Number registry https://www.igsn.org/ 

### Related Issues:
 - New term - organismPart: https://github.com/tdwg/dwc/issues/3
 - Move terms from Occurrence to MaterialSample: https://github.com/tdwg/dwc/issues/24 
 - New term - environmentalMaterial: https://github.com/tdwg/dwc/issues/40
 - umbrella issue related to dwc:basisOfRecord and an Evidence class: https://github.com/tdwg/dwc/issues/302 
 - Change term - MaterialSample: https://github.com/tdwg/dwc/issues/314 
 - New Term - MaterialCitation: https://github.com/tdwg/dwc/issues/329
 - Change term - associatedSequences: https://github.com/tdwg/dwc/issues/332
 - New Term - materialSampleType: https://github.com/tdwg/dwc/issues/345
 - Change term - preparations: https://github.com/tdwg/dwc/issues/346
 - Change term - disposition: https://github.com/tdwg/dwc/issues/347

**NOTE: The TDWG Executive Committee has stipulated that by default, products of TDWG will use the [Creative Commons CC-BY license]().**


