---
title: Contributing to the TDWG website
description: >
  The TDWG website is a collaborative effort: anyone can contribute. Whether it is [reporting an issue](#how-do-i-report-an-issue), [writing content](#how-do-i-edit-content) or [reviewing](#how-can-i-review-content), any help in keeping the website up to date and relevant is helpful. This page explains how.
background:
  img: https://images.unsplash.com/photo-1508780709619-79562169bc64
  by: Kaitlyn Baker
  href: https://unsplash.com/photos/vZJdYl5JVXY
toc: true
---

## Reporting issues

Discovered a typo? Noticed a bug? Have a suggestion to improve a page? Let us know by [creating an issue](https://github.com/tdwg/website/issues/new) in the website repository.

### How do I report an issue?

[Click here](https://github.com/tdwg/website/issues/new) to report an issue on GitHub. Doing so will automatically notify website maintainers and you will receive an email notification if they have questions or if the issue has been resolved.

Want to solve the issue yourself instead? See [how to edit content](#how-do-i-edit-content).

## Writing content

### How do I edit content?

1. Click `Edit this page` at the top right of the page you want to change. Note: this page has this too!
2. Doing so will open the corresponding Markdown document for that page. Alternatively, you can [browse the website repository](https://github.com/tdwg/website/tree/master/content) for the page you are looking for.
3. Click the pencil button on the top right to edit the page. You need to be logged-in to GitHub to do this.

    ![Edit button on GitHub](/assets/images/edit-page-button.png)

    Note: behind the scenes, this will fork the website repository to your account, so you can make suggestions.

4. Edit the file using [Markdown syntax](https://guides.github.com/features/mastering-markdown/).
5. Preview your suggestions by switching to the `Preview changes` tab. You can switch between the tabs `Edit file` / `Preview changes` as much as you want.
6. At the bottom of the page, write a short description of what you changed. If you want to explain more, use the bigger text box as well, e.g.:

    > Add how to become involved to BDQ IG + correct link
    > 
    > ---
    > 
    > The biodiversity data quality page was missing a section on how people could become involved in that interest group. I also updated a broken link.

7. Click the green buttons `Propose file change`, then `Create pull request` and then `Create pull request` again.
8. Great! Your **proposed changes** are now submitted as a [pull request](https://help.github.com/articles/about-pull-requests/) and the website maintainers have been notified. You will receive an email notification if they have questions or when your suggestions have been accepted.

Want to make more substantial changes instead? See [how to edit multiple pages at once](#how-do-i-edit-multiple-pages-at-once).

### How do I edit multiple pages at once?

If you want to edit multiple pages, then the workflow to [propose a single file change](#how-do-i-edit-content) might be too limiting. You can solve this by working on the files on your own computer. It does require some more advanced knowledge of GitHub however:

1. [Fork this repository](https://help.github.com/articles/fork-a-repo/) to your own GitHub account. This is actually done too if you [edit a single file](#how-do-i-edit-content). In your fork, you can experiment freely without effecting the original website repository.
2. [Clone your fork](https://help.github.com/articles/cloning-a-repository/#cloning-a-repository-to-github-desktop) to your computer. The easiest tool for this [GitHub Desktop](https://desktop.github.com/).
3. Edit the files in your favourite text editor. You can also add/delete files.
4. Commit and push your changes.
5. Propose your changes by [creating a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) from your fork.

Note: it's best not to let your work linger in your fork, as it will get out of sync with the main repository. To get your fork up to date again, [sync your fork](https://help.github.com/articles/syncing-a-fork/).

### Do I need to login to edit content?

No, there is no logged-in section for this website. Anyone can suggest changes by clicking `Edit this page` at the top right of a page:

![Edit this page link](/assets/images/edit-page-link.png)

For articles it will say `Edit this article`. The link will take you to [GitHub](https://github.com/tdwg/website) where the authentication and review process is handled.

### How is content organized?

Content is organized in a [hierarchical directory structure](https://github.com/tdwg/website/tree/master/content/), which represent the different sections of the website:

```
content
├── pages
│   ├── about       : About pages
│   ├── community   : Interest group and their task group pages
│   ├── conferences : Conference pages
│   ├── home        : Home page
│   ├── journal     : Journal page
│   └── standards   : Standard pages
│
└── articles
    ├── 2018        : News articles for 2018
    └── ...         : Another year directory
```

Each page/article is a self-contained directory with:

- A single **Markdown document** `index.md` with the text and metadata for that page
- Optionally **static files** (images, pdfs) referenced from the text
- Optionally **directories** for subpages

```
bdq          : Directory for the bdq page
├── index.md : Text and metadata for the bdq page
├── info.pdf : Pdf referenced in text
├── logo.jpg : Image referenced in text
└── vocab    : Directory for the vocab subpage
```

Directory names should be short, lowercase and hyphen-separated (e.g. `citizen-science`) as together with the hierarchy they make up the URL: `/community/citizen-science/index.md` → `https://www.tdwg.org/community/citizen-science/`

### What is the difference between a page and an article?

An article has a publication date, while a page has not. The use of articles is reserved for the [news section](/news/) of this website.

### How do I start a new page?

Before starting a new page, consult with the website maintainers if and where the page should be created by [opening an issue](#how-do-i-report-an-issue). The steps below describe how to create a page after this has been discussed.

1. Browse the [website repository](https://github.com/tdwg/website/tree/master/content/pages) to the place where you want to create the page. See [how content is organized](#how-is-content-organized).
2. Click `Create new file`. You need to be logged-in to GitHub to do this.

    ![Create button on GitHub](/assets/images/create-page-button.png)

3. Name your file `page-name/index.md`. File names should be short, lowercase and hyphen-separated.

    ![Name file](/assets/images/create-page-name.png)

4. Copy and adapt the following content:

        ---
        title: Page title
        description: >
          Short description
        background:
          img:  
          by: 
          href:
        ---

        Page content


5. End your page with an empty line.
6. At the bottom of the page, write a short description of what you changed.
7. Click the green buttons `Propose new file`, then `Create pull request` and then `Create pull request` again.
8. Great! Your **proposed page** is now submitted as a [pull request](https://help.github.com/articles/about-pull-requests/) and the website maintainers have been notified. You will receive an email notification if they have questions or when your suggestions have been accepted.

### How do I start a new news article?

...

### How do I add a static document (e.g. image, pdf)?

...

### How do add an internal link?

...

### What is page metadata?

...

### Should I use American or British English?

We use [Oxford spelling](https://en.wikipedia.org/wiki/Oxford_spelling) (British English with "-ize") for all TDWG content.

## Changing layout

### How do I change the cover image?

...

### How do I change the order of pages in the navigation?

...

### How do I create the side navigation?

...

### How do I change the home page

...

### How do I change the rest of the layout?

...

## Reviewing

### Why are my suggestions not appearing on www.tdwg.org?

[Suggestions](#how-do-i-edit-content) you make do not appear live on www.tdwg.org. This takes three steps:

1. They need to be **reviewed** ([by anyone](#how-can-i-review-content)). This is done on a voluntary basis and can take some time. You will receive an email notification for this.
2. They need to be **approved** by one of the [website maintainers](#who-maintains-the-website). You will receive an email notification for this.
3. Once accepted (i.e. the pull request is merged), an **automatic build script** will rebuild the website and incorporate your changes. This can take up to a minute.

If your suggestions are rejected (i.e. the pull request is closed without merging), you will also receive an email notification, but step 3 will be skipped (i.e. the website will not be updated).

### How can I review content?

You can review content by [watching this repository](https://help.github.com/articles/watching-and-unwatching-repositories/#watching-a-single-repository):

1. Click the `Watch` button in the top right of this repository, then select `Watching`.
2. You will be notified by email of any reported issue or suggested changes.
3. From those emails, click `view it on GitHub` at the bottom to open the issue or pull request.
4. Review the issue or suggested change and leave feedback as a comment.
5. Great! Your review helps website maintainers to approve/refuse suggestions and improves the quality of the website.

If you also want to approve suggestions, you can [ask to become a website maintainer](#who-maintains-the-website)?

### Who maintains the website?

Everyone! See [how you can contribute](#how-can-i-contribute) and [who has contributed already](https://github.com/tdwg/website/graphs/contributors).

There is a dedicated group of **website maintainers** however that have admin rights to this repository: they are the people who can [approve changes](#why-are-my-suggestions-not-appearing-on-wwwtdwgorg) and have these appear on www.tdwg.org. If you want to join that group, send an email to secretary@tdwg.org.

## Other

### What is the technology behind the TDWG website?

...

### How do I update these FAQ?

...
