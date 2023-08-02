# job-portal

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/80e9cbb9-980d-4a47-8767-91a07b728f49)

1.	Introduction 

Welcome to the Job Portal Management Report, where we present a comprehensive analysis of our online job portal. Job Portal Management was created with the aim of streamlining the job search process for both job seekers and employers. In this report, we will delve into its performance, user engagement. Our goal is to evaluate its effectiveness in connecting talented professionals with leading companies. By analysing key metrics, user demographics, and feedback, we seek to identify areas of improvement and capitalize on growth opportunities. Let's explore the insights that will shape the future of Job Portal Management.


2.	Research and Planning

The web application Job Portal Management is designed for those seeking employment in their field. There are numerous job portals available across the globe. We used the Django Python Framework to develop this website. We used the cloud-based pythonAnywhere to access this site. SQLite is used to store all of a web application's records.

3.	Choice of Framework and Technologies 

3.1	Python

Incorporating Python version 3.11.1 into this web application. On the server, Python is used to construct web applications. This web application was created entirely with Python Django. Python is used in every aspect of the undertaking. Python was used to create the web application's configurations, files, and data models. The development of the web application occurs in a virtual environment.

3.2	Django Framework

Django is a high-level web platform written in Python that makes it easy to make web apps that are both secure and scalable. It uses the Model-View-Controller (MVC) design pattern, which in Django is called the Model-View-Template (MVT) pattern. The "Don't Repeat Yourself" (DRY) concept and clean, reusable, and easy-to-maintain code are at the heart of Django's philosophy. PostgreSQL, MySQL, Oracle, Microsoft SQL, and MariaDB are the five database backends that Django can use. The "settings.py" file is the main project file where all of the web application's loaded apps, external libraries, backend settings, debug settings, etc. are made.

3.3	SQLite

SQLite is an open-source relational database management system (RDBMS) that is small, self-contained, and doesn't need a server. It is made for embedded systems, mobile devices, and small to medium-sized applications that may not need a full-fledged database server. SQLite is written in the C computer language and is widely used because it is easy to use, works well, and is easy to add to other programmes.


3.4	PythonAnywhere

PythonAnywhere is a cloud-based Integrated Development Environment (IDE) and web hosting tool for programmers, developers, and data scientists who like to use the Python programming language. The platform has a number of features that make it easier to get work done, such as syntax highlighting, code autocompletion, and debugging tools. These features help users build and fix Python apps quickly.

3.5	Html

HTML, which stands for HyperText Markup Language, is the most important part of the World Wide Web. It is a markup language that is used to make web pages and organise their information. Tags, which are shown by angle brackets (tag>), are used in HTML to describe the parts of a webpage. HTML is made so that it works on any platform and is easy for web browsers to understand. This makes sure that material looks the same on all devices and platforms.


3.6	CSS

CSS, which stands for "Cascading Style Sheets," is an important part of building websites. It works with HTML to define how web pages look and how they are laid out. It is a language for style sheets that lets developers control how HTML parts look and make sure they look the same on all devices and platforms. CSS is based on the idea of sliding, which means that styles can be passed down from parents and changed by more specific rules.

4.	UX Design
 
4.1	Flow Diagram

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/af20e7e0-0dc9-45b4-9bbf-60c59f8fdc06)

4.2	Homepage:

The homepage contains three distinct sections. The homepage's left navigation bar displays the home, login, and Register sources, while the right navigation bar contains the search bar. Using the search bar located on the right side of the homepage, the user may execute a search based on the location and category for all available positions on the website. There are two options for the register model: employee and candidate. Below the navigation bar is a list of all available positions based on location and job descriptions.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/950e1c56-ed2e-49a4-9b78-8cb1e95a3393)

4.3	Homepage (Features):

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/bf997b16-60fb-46cc-b1ed-dbaaa21e99fe)

In the below figure 4.3.3, on search bar, I have search based on the category i.e. Full Time.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/4798978c-bbe1-427f-b2cf-08c1d37ae9f6)

You'll get a list of jobs after executing a location-based search. If you click on "Finance Analyst" or "read more," you'll see a job description. Refer to Figure 4.3.4 for more information on how it operates and job opportunities.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/2bf4b0b1-8151-423a-a4bf-41c4673bd2cd)

If a candidate is interested in the job after reading about it, he can click on the "Login Now" button, which will take him to the "Registration" page (Figure 4.3.5).

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/97b2fd39-c91b-4b9c-914d-5850c8cf5df3)

4.4	Login Page:

In the figure 4.4.1, if the person has already signed in. If the user is new, he or she must use the "Register" button to set up a new account.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/8c3d0a15-f86b-4aa4-8aba-270fe5f88cf6)

4.5	Register Page:

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/e827b7b1-bed0-4e43-a908-64f8d7997590)

On this page, a new person can sign up for the job portal by making an account. All of the forms have to be filled out by the user. At this point, certain validations are used. If any of the validations don't match, like if the user's password and confirm password aren't the same, the user will be shown a message. It shouldn't just be numbers, and it shouldn't be the same password as our personal details. It needs to be at least 8 characters long. Emails should be written in the right way. Please refer the below figure to view the validation errors.

User Name Validation

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/d66107a8-7bff-4dfa-bf6a-31295180c47e)

Email Validation

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/8b3e0482-9c4d-48b0-987e-37ff3c443b8a)

Password Validation

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/a1ca2f1c-080c-435d-abce-79132e7e420f)

4.6	User Home Page

Once the user login, he will see the list of available jobs in the home page and user can use search bar for the applying jobs based on the category and location. On the left side of the navigation bar there is home, logout, and my profile option. 

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/f0813fc6-e405-4beb-9752-f0fbda3aa1ea)

4.7	User Profile

Clicking on the "Update" button, as seen in the image that follows, will allow Candidate to make modifications to his résumé. In the "Applied Jobs" section, he will be able to view any jobs for which he has submitted an application.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/fe730e3a-821e-4173-812b-6dd126a8a888)

The candidate can change his name, email address, phone number, and personal picture once he hits the "Update" button. The candidate can choose a file for submitting his picture, and once he clicks the "Submit" button, his profile will be updated.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/f83bfb68-a1f7-41e3-8489-c77180a06e20)

Profile Updated Successfully

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/7518878a-e41f-488e-884f-57187d12f6c9)

4.8	Applying Jobs

When a candidate clicks "Read More," he or she can see job titles. If the candidate wants to apply for the job, he or she can click "Apply Now." Once he has applied for the jobs, he can see them in the "my profile" part of the site.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/b18d9d47-c1e5-4cc9-b453-2bb7098028be)

When you click the "apply now" button, you will be redirected to the next page, where you will be asked to fill out the relevant fields, which include City, Address, Experience, Cover Letter, and Resume. A applicant can upload his resume to the section designated for resumes by utilising the choose file button. After the applicant has completed the form and clicked the submit button, they will be able to view all of their applied jobs on their candidate profile.

Apply Job Page

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/ad06dea8-71f7-4b7b-8e51-934a63545328)

4.9	Admin User

To access the admin page we need to use the given link – “ http://127.0.0.1:8000/admin/login/?next=/admin/ ”The username and password are the same which is used in the local SQLite login.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/911f42a3-82a8-484a-873a-722c722cacd3)

4.10	 Admin Dashboard

Figure, the admin can view all the data and add the data needed for the web application. 

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/4bb6201d-eb05-4cdf-817e-2cdf5629511d)

In the below figure, Admin can see the list of jobs applied by the candidate.

User Applied Jobs Page

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/65f25dd4-49fc-48e1-88ad-6faa9e028f86)

In the below figure, Admin can edit, view and add the below details and choose select, Reject and status option. After editing the below details admin can save the details. Admin can delete the ‘applied_job Object (1)’.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/71328f4a-a006-4201-80f1-914aacf6be14)

Update Applied Jobs Page

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/416b77c9-2647-4e76-a4e9-94d0aada5e19)

After the editing is done, admin can save the data and message will appear as “The applied_job  ‘applied_job object(1)’ was changed successfully”.

Successful Save Pop up

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/238ed2de-4ed2-4796-b20e-1da60e362002)

In the candidate section, admin can see the list of the candidates in the below figure. Admin can search the candidate based on the name, email and phone.

Candidates Page

In the candidate section, admin can see the list of the candidates in the below figure. Admin can search the candidate based on the name, email and phone. 

Admin can see all the candidates details by clicking on the candidates name. after clicking on the candidate name admin can edit, add, view and delete the candidates.

Update Candidates

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/c83abddc-dbe3-4485-9a99-2890cfafbc01)

Changed History of Candidates

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/02a12a6c-c9d9-44fe-a0e4-d71aaf6bb2db)

On the top right hand site there is history button. Used of this history button, admin can see the what changes are made.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/c9842433-10fc-4e2a-bc2d-0f4e6b18a393)

Change History List of Candidates

Change History List of Candidates![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/c8cd311f-1c65-4678-a09a-5fa62f4ec93e)

admin can add the cities and we can see the total number of cities added to this section. To add new city click on “ADD CITY” option.

Added the List of Cities

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/8bfb35cc-c7d3-4913-bbca-b256a561a73f)

If admin wants to add new city then, he can write on the text box and click on the save button. There are 2 more button that is “Save and add another”, “Save and continue editing”. 

Option to add new city

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/cb7cfcf7-44da-4eeb-9efe-b45c1f7cd464)

Admin can see the list of Job_category. And on the right top of the figure admin can add new category.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/2d1ddb84-3b89-491a-b339-ebd185c8911c)

admin can add new job category. There are two more buttons i.e. “Save and add another” this button will add one and open a new page as below picture. “Save and another editing” this button can save and still we can edit the that job_category.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/610fdf58-3759-4e1f-bb42-c5d741b79de1)

Option to add hob

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/f4d6e744-e295-4570-b0c9-94b549f62bed)

admin can see the list of new jobs from the other cities and company.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/604100d8-7265-4574-a399-2df8691023d1)

To add New jobs Admin need to fill all the below details based on the companies requirements.

![image](https://github.com/ujwalakabadi0508/job-portal/assets/58591291/bc122be8-1446-47d9-bcd8-cec9f783dbea)

Steps for running app:

1. Install Virtual Environment

    pip install venv

2. Activate Virtual Environment

   virtualenv venv

   source env/bin/activate
   
4. Install Dependencies

   pip install -r requirements.txt

5. Run Program

   python manage.py runserver




























