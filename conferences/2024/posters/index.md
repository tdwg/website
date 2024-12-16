---
title: Posters
description: >
  Posters presented at SPNHC-TDWG 2024
background:
  img: https://images.unsplash.com/photo-1621866486780-78be8fd22b97
  by: Georg Eiermann
  href: https://unsplash.com/photos/eWiTil2CAvA 
  toc: false
---

# Posters



## [From Manual to Automated: Enhancing Publication Tracking at the California Academy of Sciences Using the OpenAlex API](https://static.tdwg.org/conferences/2024/posters/abarca-188.pdf)

<div>
  <span class="mdc-typography--body1" style="text-align: left; font-weight: 500; text-decoration: underline">Maricela Abarca </span><a class="mdc-typography--body1" href="https://orcid.org/0000-0002-0890-8887" style="text-decoration: underline">ORCID iD</a><sup style="font-weight: 500">1,2</sup><span class="mdc-typography--body1" style="text-align: left">, </span><span class="mdc-typography--body1" style="text-align: left; font-weight: 500">Joseph Russack </span><a class="mdc-typography--body1" href="https://orcid.org/0000-0001-8366-0941" style="text-decoration: underline">ORCID iD</a><sup style="font-weight: 500">1</sup>

  <div style="font-size: 0.8em;">
    <sup>1</sup>California Academy of Sciences, San Francisco, California, USA.<br />
    <sup>2</sup>University of San Francisco, San Francisco, California, USA.<br />
    &nbsp;
  </div>
</div>

#### Abstract

<p class="calibri">Although publications alone are not a comprehensive measure of the impact of biodiversity collections, they provide a valuable starting point for formulating impact metrics due to the accessible and standardized nature of publication metadata. The ubiquity of attributes such as DOIs, author affiliation, and the increasing adoption of author identifiers such as ORCIDS facilitate automated collection and analysis of publication data. One useful and emerging area of publication metadata is the assignment of UN Sustainable Development Goals, which offer a direct linkage between collections based research and solutions to climate change and sustainability initiatives.</p>
<p class="calibri">At the California Academy of Sciences (CAS), the tracking of institutional publications was initially a manual process, conducted as needed using spreadsheets and documents. Recognizing the inefficiencies and potential for errors in this method, CAS aimed to develop an automated, reliable tracking system. The integration of publications from diverse sources posed a challenge, yet it was successfully addressed using the OpenAlex API, an open-source repository of publication data. Querying the API using affiliation metadata alone resulted in a significant improvement in publication tracking, and further refinement was achieved by incorporating ORCID-based searches and filters. In the calendar year 2022, while staff manually tracked 66 publications for reporting purposes, the API system successfully identified 198 publications authored by museum staff and affiliates during the same period. The API is also equipped to retrieve datasets published through platforms like Zenodo, Figshare, and other DataCite affiliates. It returned 22 CAS datasets, a metric that was previously untracked.&#xA0;</p>
<p class="calibri">Components of the publication tracking application include a MySQL database of publications and institutionally affiliated authors, as well as an automated email reporting system for tables and visualizations of publication data. Examples of these reports, including visualizations related to Sustainable Development assignments can be found at <a href="https://github.com/calacademy-research/publications_finder" class="calibri">https://github.com/calacademy-research/publications_finder</a>.</p>

------
