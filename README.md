# Swan Laboratory New Website

## Table of Contents
1. Introduction
2. Installation
3. Usage
4. Using the admin features



## Introduction

This project is the new and improved version of the swan lab website .This README will guide you through the installation, usage, and configuration of the project.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Ruhifarhath/swan-backend.git
    ```

2. Navigate to the project directory:
    ```sh
    cd swanWebsite
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Django-admin-Interface
django-admin-interface is a modern **responsive flat admin interface customizable by the admin itself**.

![django-admin-interface-preview](https://user-images.githubusercontent.com/1035294/35631521-64b0cab8-06a4-11e8-8f57-c04fdfbb7e8b.gif)


```sh
python manage.py createsuperuser
Username (leave blank to use 'your-username'): admin
Email address: admin@example.com
Password: **********
Password (again): **********
Superuser created successfully.
```

## Accessing Django Admin

Once the website is hosted, you can access the Django admin page by appending `/admin` to your domain name (e.g., `https://yourdomain.com/admin`). You'll need administrative credentials to log in.

## Models Available in Admin

### Slide

- **Title:** Title of the slide.
- **Description:** Description related to the slide.
- **Image:** Image associated with the slide.
- **Link:** Optional URL link for the slide.

### Prototype

- **Name:** Name of the prototype.
- **Description:** Description related to the prototype.
- **Image:** Image associated with the prototype.
- **Link:** URL link related to the prototype.

### GalleryImage

- **Image:** Image to be displayed in the gallery.
- **Description:** Optional description for the image.

### Sponsor

- **Name:** Name of the sponsor.
- **Description:** Description related to the sponsor.
- **Image:** Image associated with the sponsor.
- **Link:** Optional URL link related to the sponsor.

### Patent

- **Application Number:** Number associated with the patent application.
- **Publication Date:** Date of publication (optional).
- **Title:** Title of the patent.
- **Authors:** Authors of the patent.
- **Is Granted:** Checkbox indicating if the patent is granted.

### EditedBooks, AuthoredBooks

- **Award:** Award received for the book (if any).
- **Title:** Title of the book.
- **Authors:** Authors of the book.
- **Link:** Optional URL link related to the book.

### BookChapters

- **Book Title:** Title of the book containing the chapter.
- **Title:** Title of the chapter.
- **Authors:** Authors of the chapter.
- **Publisher:** Publisher of the book (optional).
- **Year:** Year of publication (optional).
- **Chapter Title:** Title of the chapter (optional).
- **Pages:** Pages covered by the chapter (optional).
- **ISBN:** ISBN of the book (optional).
- **DOI:** DOI of the chapter (optional).
- **Link:** Optional URL link related to the chapter.

### ConferencePaper

- **Title:** Title of the conference paper.
- **Authors:** Authors of the paper.
- **Conference:** Name of the conference.
- **Location:** Location where the conference was held.
- **Start Date, End Date:** Dates of the conference.
- **Year:** Year of publication.
- **Extra Info:** Additional information related to the paper.

### JournalPapers

- **Title:** Title of the journal paper.
- **Authors:** Authors of the paper.
- **Journal:** Name of the journal.
- **Year:** Year of publication.
- **Link:** Optional URL link related to the paper.

### AwardWinningPaper

- **Award:** Award received for the paper (if any).
- **Title:** Title of the paper.
- **Authors:** Authors of the paper.
- **Journal:** Name of the journal.
- **Year:** Year of publication.
- **Volume, Issue, Pages:** Additional details (optional).
- **Link:** Optional URL link related to the paper.

### Announcement

- **Title:** Title of the announcement.
- **Author:** Author of the announcement.
- **Created At:** Date and time of announcement creation.
- **Link:** Optional URL link related to the announcement.
- **Is New:** Checkbox to mark if the announcement is new.

### MTechStudent, VisitingStudent

- **Name:** Name of the student.
- **Thesis Title:** Title of the thesis (for MTech and visiting students).
- **Thesis Year:** Year of thesis completion (for MTech students).
- **Co-supervisor:** Co-supervisor of the student (for MTech students).
- **Intern Duration:** Duration of the internship (for visiting students).
- **Additional Info:** Additional information (for visiting students).

### Contact

- **Name:** Name of the contact person.
- **Email:** Email address of the contact person.
- **Message:** Message sent by the contact.
- **Created At:** Date and time when the message was created.

### Member

- **Name:** Name of the member.
- **Designation:** Designation within the organization.
- **Photo:** Photo of the member.
- **Twitter, Facebook, LinkedIn:** Social media profiles (optional).
- **Is Current:** Checkbox indicating if the member is currently active.


