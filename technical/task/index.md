---
title: Running a Task Group
background:
  img: https://images.unsplash.com/photo-1509715513011-e394f0cb20c4
  by: Alex Guillaume
  href: https://unsplash.com/photos/16oqzpFRMqs
toc: true
---

## Running a Task Group

TDWG is an open, consensus-driven organization. So Task Group (TG) meetings should be open to all and publicised to the community.

The convener of the TG should be familiar with the [TDWG Process (by-laws)](https://www.tdwg.org/about/process/) and the [community management page](https://www.tdwg.org/community/management/). Both provide important details about the operation of Task Groups. 

### Organization

Once the charter is approved, the convener of the TG will work with the [Outreach and Communications functional subcommittee](https://baskaufs.github.io/website/about/committees/outreach/) to publicize the group and the [Infrastructure functional subcommittee](https://baskaufs.github.io/website/about/committees/infrastructure/) set up a records and communication system for the group. Record-keeping is typically done using a GitHub repository and communication is usually done through an email list or Slack. It may be possible for the group to use the sponsoring Interest Group's GitHub repository or it may be better to have a separate repository if the task is complex. 

### Meetings

Unlike Interest Groups, Task Groups are required to produce specific deliverables with a projected timeline given in their charter. It is unlikely that the TG will be successful without holding regularly scheduled meetings. It is human nature to procrastinate and the deadline of an upcoming meeting is often an effective incentive for participants to complete the necessary work. Some components of successful meetings are:
- using a meeting planner to come up with times that are reasonable for TG participants. The [World Clock Meeting Planner](https://www.timeanddate.com/worldclock/meeting.html) is one such tool. Rather than announcing meeting times in some particular local time that is prone to misinterpretation, announce the times in UTC and provide a link to a time zone converter that will display local times appropriate for the participants ([example](https://www.timeanddate.com/worldclock/converter.html?iso=20230710T130000&p1=1440&p2=111&p3=37&p4=136&p5=51&p6=179&p7=64&p8=75&p9=224&p10=248&p11=152)).
- providing a calendar invitation at the time when the meeting is announced. If Zoom is used as the meeting platform, it can be used to generate several types of calendar invitations that will both place the meeting at the appropriate local time for the user and also include the Zoom link in the calendar event where the participant will be able to find it on the day of the meeting.
- provide an editable agenda/notes doc (e.g. Google Doc) link to participants ahead of the meeting. This will help the participants prepare for the meeting and also allow them to help take notes during the meeting.
- save a non-editable PDF export of the meeting notes in the group's GitHub repository so that people who miss the meeting can see what they missed. This is better than just providing a link to the Google Doc since it preserves a permanent record of what was discussed at the meeting. 

One mechanism for publicising meetings is to create a meeting announcement "issue" on the group's issue tracker ([example](https://github.com/tdwg/tag/issues/38)). This will ping anyone who is "watching" the repository and will provide consistent place where potential participants can look to find upcoming meetings. Once the meeting is over, a link to the meeting notes can be added as an issue comment and the issue can be closed. Since some participants may not be GitHub users, sending announcements via an email list is also a good idea.

Because the work of Task Groups is supposed to be open, transparent, and based on community input and consensus, it's important that meetings are open to all and that all work of the group is public. This creates challenges for announcing public meetings while avoiding "Zoom bombing". Small, boring task group meetings are unlikely to be the target of Zoom bombing and the damage done by a bomber is minimal. So it's generally not a problem to just post the meeting link publicly without a password. If the convener is concerned about Zoom bombing, a password-protected link can be sent to previous participants and public announcements can tell new participants to email the convener for a link. 

### Records

The current norm is that activities of the group should be recorded in its GitHub repository. Files, meeting records, and document drafts can be stored directly in the repository. Discussion and resolution of issues can be documented using the repository's issue tracker. As a practical matter, documents are often developed collaboratively using a system that allows for collaborative editing and commenting such as Google Docs. Completed drafts can then be exported as PDFs or converted to Markdown, then archived in the repository. Some groups prefer to use the built-in wiki function of GitHub for document development. 

The Task Group convener should be an active member of the sponsoring Interest Group and attend Interest Group meetings to keep the Interest Group up to date on the Task Group's progress. The Task Group convener is also required to submit an annual report to the Executive Committee. See the [community management page](https://www.tdwg.org/community/management/) for details.

### Getting started

The first job of the Task Group convener and core members is to engage the community, both to allow them to participate in development of the deliverable and to allow them to provide input on the features of the deliverable. If the deliverable is a coordinated enhancement to an existing vocabulary, it is required that the development process begin with the creation of a [Feature Report](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#4-vocabulary-enhancements). In other cases, the feature report is not required, but it's a best practice to create one for any kind of deliverable. The exact nature of the feature report is not specific, but it needs to document how community input was used to determine the features of the deliverable. An example would be to collect use cases ([example](https://github.com/tdwg/ac/blob/b0eb3f091557a86fe67cc207ff813493a4b3f4b8/views/submitted-use-cases.md)) and use them to determine the requirements of the deliverable ([example](https://github.com/tdwg/ac/blob/b0eb3f091557a86fe67cc207ff813493a4b3f4b8/views/requirements.md)). The requirements may change as the deliverable is developed and it becomes more clear what is possible. 

### Planning ahead

Once the Task Group is set up, the bulk of the work is designing and building the deliverable. However, there are two things that the convener should consider in preparation for the end game. 

The review process of new standards is controlled by a review manager who must be independent of the Task Group. There is a tendancy to involve as part of the Task Group every person who is knowledgeable about the subject of the new standard. However, there needs to be at least one person who is interested and knowledgeable about the subject who can serve as review manager once the draft is complete. So it may be useful to not involve at least one interested party who could potentially serve as review manager at the end. The choice of review manager is made by the Executive Committee, but the Executive is generally open to suggestions of candidates from the Task Group. For more information, see the description of [Review Managers](https://www.tdwg.org/about/review-managers/#13-review-manager) in the Review Manager Guidelines. For changes to existing vocabularies, the sponsoring Maintenance Group serves in the role of review manager, so finding a person to serve in that role is not an issue.

When the deliverable is complete, it will be evaluated on its technical merits and its interoperability with other TDWG standards. The [Technical Architecture Group (TAG)](https://github.com/tdwg/tag) is responsible for overseeing these aspects of TDWG standards. Therefore, it's a good idea to communicate with the TAG during the development process whenever issues come up that may be related to how the deliverable will interact with existing standards. As the deliverable nears completion, it is advisable to inform the TAG so that they can be paying attention to the Task Group's drafts to catch any glaring problems before the review process begins. 

### Finishing the task

The process of reviewing and ratifying the group's deliverable varies depending on whether it is a new standard or an addition to an existing vocabulary. The process for new standards is described briefly in the [Process document](https://www.tdwg.org/about/process/) but more details are available in the [Review Manager Guidelines](https://www.tdwg.org/about/review-managers/). The process for additions to existing vocabularies is described in the [TDWG Vocabulary Maintenance Specification (VMS)](http://rs.tdwg.org/vms/doc/specification/#3-change-process). In both cases, the Task Group will develop a proposal package that will be reviewed by experts, then subjected to a public review. 

Experience has shown that successful reviews require not only a clearly documented deliverable, but also evidence that the task group's product can meet the established requirements. The documentation must conform to the [requirements for human-readable documents outlined in the TDWG Standards Documentation Specification (SDS)](http://rs.tdwg.org/sds/doc/specification/#3-human-readable-documents) -- documentation that does not conform will not advance to the review stage. 

[Coordinated additions to vocabularies](http://rs.tdwg.org/vms/doc/specification/#4-vocabulary-enhancements) ("vocabulary enhancements") must include an [Implementation Experience Report](http://rs.tdwg.org/vms/doc/specification/#422-implementation-experience-report) ([example](http://doi.org/10.3897/biss.7.94188)) that shows that the features described in the Feature Report can actually be implemented. A good Implementation Experience Report will show that multiple implementers are able to use the features with a variety of data that spans the range intended to be covered by the deliverable. There is no particular length or publication requirements for the report, but the better the report, the less likely a reviewer will be to raise issues with the proposal.

Other types of proposals are not currently required to include an Implementation Experience Report. However, there have been several occasions where proposals have stalled or been sent back to a task group at the public review stage because there was not a consensus among reviewers that the proposal would actually achieve its goals. It is extremely demoralizing and frustrating for a Task Group to be sent back to the drawing board at a late stage in the ratification process, so it is better to guard against that by being prepared. Implementation testing is a best practice because it produces a higher quality deliverable that is less likely to need revision after adoption. 

### Normative, non-normative, and outside the standard

Documents associated with a standard fall into two categories: ones that are included in the standard and ones that are outside the standard. The key difference is that documents outside of the standard are not controlled by any standards process and can be changed at will. Documents within the standard are governed by TDWG change processes and will be difficult to change (but will be more stable than those outside of the standard). Documents within the standard are typically lists of terms and their metadata, documents explaining how the standard must be used in certain circumstances, and documents describing structural relationships among terms (hierarchies, how multiple values are represented, etc.). Documents outside of the standard can include introductions, user guides, recipes, translations, etc.

Documents within the standard are composed of two kinds of content. *Normative content* prescribes what is required to meet the standard and includes things like definitions and usage requirements. *Non-normative content* can include suggestions and examples. A requirement of the SDS is that standards documents must explain how a reader will know which parts of the document are normative and which parts are not. This is typically done in a "Status of the content of this document" section near the beginning of the document. Here is an example from the [Darwin Core Text Guide](http://rs.tdwg.org/dwc/terms/guides/text/):

> All sections of this document are normative, except for examples, whose sections are marked as non-normative.

Here is a more complicated statement from the [Audiovisual Core Controlled Vocabulary for Dublin Core format: List of Terms](http://rs.tdwg.org/ac/doc/format/)

> Section 1 is informative (non-normative).

> Section 2 is normative except as noted.

> Section 3 is informative.

> In Section 4, the values of the `Term IRI`, `Definition`, and `Controlled value` are normative. The value of `Usage` (if it exists for a given term) is normative. The values of `Has broader concept` and `Has exact match` are normative. The values of `Term Name` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace. Label and the values of all other properties are non-normative.

An important implication of designating part of a document as normative is that changing normative content is only possible through a process that evaluates how disruptive the change will be to existing implementations. This full change process includes expert and public review. Changing non-normative content requires a less strict process that may only involve informing the community that a change has been made. 

### Preparing the metadata

Deliverables generally fall into two categories: vocabularies (or parts of vocabularies) or descriptive documents. 

If a Task Group is adding terms to an existing vocabulary, the Maintenance Group should handle the technical details of documenting the metadata. This may be done by collecting the necessary metadata fields from the submitter using a template on the GitHub issue tracker ([example](https://github.com/tdwg/dwc/issues/new?assignees=&labels=Term+-+add&projects=&template=new-term-template.md&title=New+Term+-+)).

Metadata for large numbers of terms or entirely new vocabularies (e.g. controlled vocabularies) are managed using CSV spreadsheets. For information, see the page on [Creating a vocabulary spreadsheet](https://github.com/tdwg/rs.tdwg.org/blob/master/process/create-vocabulary.md). Every vocabulary has a corresponding human-readable List of Terms document ([example](http://rs.tdwg.org/ac/doc/part/)) and it will need a list of authors and an abstract (see following paragraph).

The process for managing metadata for descriptive documents is still under development. However, you will be asked to provide information about the authors ([example](https://github.com/tdwg/rs.tdwg.org/blob/master/process/document_metadata_processing/ac_doc_termlist/authors_configuration.yaml)) and to provide a title and abstract for the document. 

### Ratification - new standards

When a Task Group believes that its draft standard is ready for review, it needs to take the following steps:
1. Make sure that all documents that will be included within the standard conform to the SDS. Preferably the standards documents should be in Markdown since that is ultimately the form they will have to be in when they are put on the web. If they are pushed to the TG's GitHub repository, they will automatically be rendered in human-readable form. Alternatively, they can be pushed to GitHub as PDFs.
2. Make a list that indicates clearly what documents will be included in the standard. You may also list informative ancillary documents, but indicate clearly that they are not part of the official submission. Include the Feature Report and Implementation Experience Report, since these will be helpful in evaluating the submission. This list can be made as part of a Markdown document in the repository or as part of an issue in the GitHub issue tracker. It is helpful for reviewers to create hyperlinks from this list to the URLs of the actual documents themselves.
3. Although it is not an official requirement of the TDWG Process, it is probably a good idea to ask the [Technical Architecture Group](https://github.com/tdwg/tag) (TAG) to take a quick look at the proposal to see if anything glaring is missing. If the proposal is complicated, the Executive Committee is likely to ask the TAG to look at it anyway, so doing this in advance will save time. This is not an exhaustive review -- along with the rest of the community, the TAG will have an opportunity to participate in the public comment period.
4. Once the convener is satisfied that the draft standard is ready, they should officially submit their draft (i.e. a cover message and a link to the list of what's included in the standard) to the Executive Committee and request the appointment of a Review Manager. Once the Review Manager is appointed, the control of the process is in the Review Manager's hands until final ratification by the Executive Committee. For details of how the process works, see the [TDWG Process document](https://www.tdwg.org/about/process/) and the [Review Manager Guidelines](https://www.tdwg.org/about/review-managers/).

### Ratification - coordinated changes to existing vocabularies

When a Task Group believes that the additions they are proposing for the vocabulary are ready, it should take the following steps:
1. Create an issue in the parent Maintenance Group's GitHub issue tracker that summarizes the proposal. This umbrella issue may link to other issues or to documents uploaded to a GitHub repository. The critical thing is that the issue is clear about what all is included in the proposed addition. If there are other informative ancillary documents that are helpful for understanding the proposal, they may be linked from the issue, but should be clearly marked as not included in the proposal. Include links to the Feature Report and Implementation Experience Report, since these will be helpful in evaluating the submission. 
2. When the issue is submitted, the Maintenance Group will evaluate the proposal to see if it meets the [*demand*, *efficacy*, and *stability* requirements for change](http://rs.tdwg.org/vms/doc/specification/#31-justifications-for-change) and that it conforms to the SDS. If they determine that it does, they will implement the appropriate parts of the change process described in [Section 3 of the VMS](http://rs.tdwg.org/vms/doc/specification/#3-change-process). By their nature, proposals from Task Groups should meet the demand requirement as demand should be demonstrated by the participation of multiple stakeholders in the group. The Implementation Experience Report should clearly indicate the efficacy of the proposed changes. If the Task Group has been communicating with the sponsoring Maintenance Group and the TAG during the development process, it is likely that the stability requirement would also be met. Thus, the main hold-up to public comment would likely to be issues of adequate documentation and conformance to the SDS. 
3. Once the Maintenance Group approves moving the proposal to public comment, the MG convener will work with the Outreach and Communications functional subcommittee to publicize the public comment. The MG convener effectively functions as the review manager and works with the Task Group to resolve any issues that arise during the public comment period. For additional details, see the VMS. 
4. When the changes (with any revisions) have been ratified by the Executive Committee, the Maintenance Group will coordinate publication of a new version of the vocbulary. When that is complete, the Task Group's work is complete and it is disbanded.

----
Revised 2023-07-09
