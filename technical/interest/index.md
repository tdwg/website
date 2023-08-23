---
title: Running an Interest Group
background:
  img: https://images.unsplash.com/photo-1509715513011-e394f0cb20c4
  by: Alex Guillaume
  href: https://unsplash.com/photos/16oqzpFRMqs
toc: true
---

## Running an Interest Group

TDWG is an open, consensus-driven organization. So Interest Group (IG) meetings should be open to all and publicized to the community.

The convener of the IG should be familiar with the [TDWG Process (by-laws)](https://www.tdwg.org/about/process/) and the [community management page](https://www.tdwg.org/community/management/). Both provide important details about the operation of Interest Groups. 

### Organization

Once the charter is approved, the convener of the IG will work with the [Outreach and Communications functional subcommittee](https://baskaufs.github.io/website/about/committees/outreach/) to publicize the group and the [Infrastructure functional subcommittee](https://baskaufs.github.io/website/about/committees/infrastructure/) to set up a records and communication system for the group. Record-keeping is typically done using a GitHub repository and communication is usually done through an email list or Slack. 

### Meetings

IGs vary in terms of the formality and frequency of their meetings. Some IGs meet only annually or a few times per year, while others meet more often. Some IGs primarily conduct their business via email and rarely have formal meetings. The frequency and type of meetings is up to the group and is flexible based on the needs of the group.

In some cases, an Interest Group exists primarily as a mechanism to generate a Task Group to develop some standard. In that case, the Interest Group may have few activities of its own. However, it is still the responsibility of the Interest Group to monitor the progress of the Task Group to ensure that it is making progress towards completing its task. If the Task Group is "stuck" and not making progress, the IG should meet with the convener of the Task Group to figure out how to remove the impediments to progress or to decide to abandon the task and shut down the Task Group. 

### Records

The current norm is that activities of the group should be recorded in its GitHub repository. Files, meeting records, and document drafts can be stored directly in the repository. Discussion and resolution of issues can be documented using the repository's issue tracker. As a practical matter, documents are often developed collaboratively using a system that allows for collaborative editing and commenting such as Google Docs. Completed drafts can then be exported as PDFs or converted to Markdown, then archived in the repository. Some groups prefer to use the built-in wiki function of GitHub for document development. 

The IG convener is required to report annually to the Executive Committee on the group's activities. See the [community management page](https://www.tdwg.org/community/management/) for details. There may also be opportunities for the group to share its work with the community by participating in annual working sessions held remotely via Zoom. 

### Vocabulary Maintenance Groups

A Vocabulary Maintenance Group (MG) is a special type of IG that has a specific role that is detailed in the [TDWG Vocabulary Maintenance Specification (VMS)](http://rs.tdwg.org/vms/doc/specification/#21-vocabulary-maintenance-interest-groups). Generally, that involves maintaining one or more related vocabularies by:
- tracking new developments related to the vocabularies
- determining unmet community needs related to the vocabularies
- correcting errors and updating examples
- chartering Task Groups to develop new features of the vocabulary 
- managing the change process for the vocabulary and its associated documents.

The MG convener should be familiar with the VMS as well as the more general information about Interest Groups given in the [TDWG Process (by-laws)](https://www.tdwg.org/community/process/) and the [community management page](https://www.tdwg.org/community/management/) documents. 

As with generic Interest Groups, MGs have the same annual reporting requirements.

When perceived needs for maintenance or change are relatively small and uncomplicated, the MG may decide to develop solutions as part of their normal operations. When they are large and complex, the MG may deligate the development of solutions to a Task Group that it charters. 

Changes to improve the vocabulary may be proposed by a Task Group chartered by the MG, or by any person or group. Changes include individual term changes, or larger packages known as "coordinated additions". Cooridinated additions to vocabularies are more complex and require additional documentation [described in the VMS](http://rs.tdwg.org/vms/doc/specification/#4-vocabulary-enhancements). In both cases, change proposals should be documented using the MG's GitHub issue tracker. Communication related to the proposals should be documented as comments associated with the issue in the tracker. 

![change process diagram](https://github.com/tdwg/vocab/raw/master/graphics/change-process.png)

The general change process applies both to individual term changes and coordinated additions. It is shown in the diagram above, with [details given in the VMS](http://rs.tdwg.org/vms/doc/specification/#3-change-process). The MG plays several key roles in the process:
- monitoring change proposals made through the issue tracker and determining when they are mature enough to move forward.
- managing public comment periods for proposals.
- communicating with the Executive Committee once consensus is reached on proposals.
- publishing new versions of vocabulary-related documents.

Publication of changes requires coordination between the MG and the general TDWG metadata management system. In order to enable IRI dereferencing and the generation of machine-readable metadata, the changes need to be incorporated in the [rs.tdwg.org GitHub repository](https://github.com/tdwg/rs.tdwg.org). Once the changes are released there, the MG can use those data to generate new term reference documents by script (at a minimum, the List of Terms document for the vocabulary). See the [Processing a vocabulary spreadsheet](https://github.com/tdwg/rs.tdwg.org/blob/master/process/process-vocabulary.md) page for details.

----
Revised 2023-08-19
