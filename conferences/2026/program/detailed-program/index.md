---
title: Detailed program
description: >
  Browse the detailed TDWG 2026 program and open talk abstracts without leaving the schedule.
background:
  img: https://static.tdwg.org/conferences/2026/images/monolitten-vigelandsparken.jpg
  by: Visit Norway / Field Productions
  href: https://www.visitnorway.com/listings/vigeland-sculpture-park/2799/
layout: base
toc: false
---

<link rel="stylesheet" href="https://storage.gbif-no.sigma2.no/misc/static/tdwg-2026/tdwg-2026-programme.css">

<div class="programme-app">
  <div class="programme-intro">
    <p class="lead">Select any talk to see its abstract, presenter, time, room and session information.</p>
    <p class="programme-updated">Program current as of 19 September 2026. Late changes will also be announced in Whova.</p>
  </div>

  <div class="programme-tools" aria-label="Programme filters">
    <label class="programme-search">
      <span>Search talks, presenters or sessions</span>
      <input type="search" data-programme-search autocomplete="off" placeholder="Start typing to filter the programme">
    </label>
    <div class="programme-days" data-programme-days role="tablist" aria-label="Conference day"></div>
  </div>

  <p class="programme-status" data-programme-status role="status">Loading programme…</p>
  <div class="programme-schedule" data-programme-schedule></div>

  <dialog class="programme-dialog" data-programme-dialog aria-labelledby="programme-dialog-title">
    <div class="programme-dialog-panel">
      <button class="programme-dialog-close" type="button" data-programme-close aria-label="Close abstract">&times;</button>
      <p class="programme-dialog-kicker" data-dialog-kicker></p>
      <h2 id="programme-dialog-title" data-dialog-title></h2>
      <p class="programme-dialog-speakers" data-dialog-speakers></p>
      <dl class="programme-dialog-meta" data-dialog-meta></dl>
      <div class="programme-dialog-note" data-dialog-note hidden></div>
      <div class="programme-dialog-abstract" data-dialog-abstract></div>
    </div>
  </dialog>
</div>

<noscript>
  <div class="alert alert-warning">JavaScript is required for the interactive programme and abstract windows.</div>
</noscript>

<script src="https://storage.gbif-no.sigma2.no/misc/static/tdwg-2026/tdwg-2026-programme-data.js" defer></script>
<script src="https://storage.gbif-no.sigma2.no/misc/static/tdwg-2026/tdwg-2026-programme.js" defer></script>
