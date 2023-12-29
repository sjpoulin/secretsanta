# Secret Santa Sorter

### TODO Video Demo:
[YouTube](https://youtu.be/OmyWezaFkIM)

### Description:

Secret Santa Sorter is a web application that enables users to input names and sort them so that each participant will be assigned a unique gift recipient among the group of participants. The web app is programmed so that no participant will "get" him or herself for the gift exchange.

This program was designed as the final project for the HarvardX course  [CS50's Introduction to Computer Science](https://cs50.harvard.edu/x/2023/), instructed by David Malan.

### Requirements and Installation:

Flask is required for use of this program. It can be installed by running:

```shell
pip install flask
```

A requirements.txt file is included with this program so that the user can alternatively install Flask running:
```shell
pip install -r requirements.txt
```

### Usage:

#### Running through the Command Line on Windows and MacOS:
```shell
flask run
```

From the home screen, the user can input names via the submit form on the home page. Two or more names are required for sorting, or else the web app will route to an error page.

Sort! - The web app sorts the listed names and routes to a page that matches the list of givers with a list of recipients.
Clear - All submitted names are cleared so the user can start over.

### Credits:

#### Libraries Used:
[Bootstrap](www.getbootstrap.com)
[Flask](www.flask.palletsprojects.com)
[jsPDF](https://parall.ax/products/jspdf)
[html2PDF](https://html2pdf.com)

#### Other Credits:
- Shuffle function created with help from [Stack Overflow](http://tinyurl.com/mrspwsx7)
- PDF function created with help from [Byte Blogger](http://tinyurl.com/4uaprt8d)
- Link images courtesy of [Free Logo Vectors](www.freelogovectors.net)
- Santa image: "Santa claus sitting beside lit tree photo" by Tim Mossholder via [Unsplash](https://unsplash.com/photos/santa-claus-sitting-beside-lit-tree-egV4ig2ZhpA)
- Santa image: "santa and his sleigh being pulled over by police on a snowy road", generated with Bing AI Image Generator



### Special Thanks:

-   My wife Laura for being a constant source of inspiration and encouragement
-   David Malan and the CS50 team at Harvard University

Created by Spencer Poulin 2023  
[Github](www.github.com/sjpoulin)