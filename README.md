<h1> Newsdata Report</h1>
<h6> Udacity project at Full Stack Devekoper</h6>

This project will create a reporting tool that prints out reports (in plain text) based on the data in the database. 
This reporting tool is a Python program using the psycopg2 module to connect to the news database.This report will answer some
questions provided by Udacity team.

<h2> Questions </h2>

<ol>
  <li>What are the most popular three articles of all time? </li>
  <li>Who are the most popular article authors of all time? </li>
  <li>On which days did more than 1% of requests lead to errors?</li>
 </ol>
 
 <h2> Requirements </h2>
 
 This project makes use of the same Linux-based virtual machine (VM) and Vagrant.This virtual machine will give you the
 PostgreSQL database and support software needed for this project.
 
 <ul>
  <li><a href="https://www.vagrantup.com/">Vagrant</a></li>
  <li><a href="https://www.virtualbox.org/wiki/Download_Old_Builds_5_1">Virtual Box</a></li>
  <li><a href="https://git-scm.com/downloads">Git Bash</a></li>
  <li><a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">newsdata.sql</a></li>
 </ul>
 
 All the procedures given below to install the VirtualBox, Vagrant and Troubleshooting are from <a href="www.udacity.com">Udacity</a>'s 
 'Full Stack Developer Nanodegree Program.'
 
 <h2>Installing the Virtual Machine</h2>
 The VM is a Linux server system that runs on top of your own computer. You can share files easily between your computer and the VM; 
 and you'll be running a web service inside the VM which you'll be able to access from your regular browser.
<br/>
We're using tools called <a href="https://www.vagrantup.com/">Vagrant</a> and <a href="https://www.virtualbox.org/wiki/Download_Old_Builds_5_1">VirtualBox</a> 
to install and manage the VM.You'll need to install these to do some of the exercises. 
The instructions below will help you do this.

<h3> Use a terminal</h3>
You'll be doing these exercises using a Unix-style terminal on your computer.
If you are using a <strong>Mac</strong> or <strong>Linux</strong> system, your regular terminal program will do just fine. 
<br />
On <strong> Windows </strong>, we recommend using the <strong>Git Bash</strong> terminal that comes with the Git software. 
If you don't already have Git installed, download Git from <a href="https://git-scm.com/downloads">git-scm.com</a>.
<br>
<h3>Install VirtualBox</h3>
VirtualBox is the software that actually runs the virtual machine. <a href="https://www.virtualbox.org/wiki/Download_Old_Builds_5_1" >
You can download it from virtualbox.org, here.<a>
Install the <em>platform package</em> for your operating system.You do not need the extension pack or the SDK. You do not need to launch 
VirtualBox after installing it; Vagrant will do that.
<br>
Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the 
current release of Vagrant.
<br />
<strong> Ubuntu users </strong>: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead.
Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.
<br />
<h3> Install Vagrant </h3>

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.
<a href="https://www.vagrantup.com/downloads.html" >Download it from vagrantup.com</a>. Install the version for your operating system.
<br/>
<strong>Windows users</strong>: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. 
Be sure to allow this.

<img aligen="center" src="https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584881ee_screen-shot-2016-12-07-at-13.40.43/screen-shot-2016-12-07-at-13.40.43.png">



<h3> Download the VM configuration</h3>

<p>There are a couple of different ways you can download the VM configuration.</p>
<p>You can download and unzip this file: <a target="_blank" href="https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip">FSND-Virtual-Machine.zip</a> 
This will give you a directory called <strong>FSND-Virtual-Machine</strong>. It may be located inside your <strong>Downloads</strong> folder.</p>
<p>Alternately, you can use Github to fork and clone the repository <a target="_blank" href="https://github.com/udacity/fullstack-nanodegree-vm">https://github.com/udacity/fullstack-nanodegree-vm</a>.</p>
<p>Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with <code>cd</code>. 
Inside, you will find another directory called <strong>vagrant</strong>. Change directory to the <strong>vagrant</strong> directory:</p>

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58487f12_screen-shot-2016-12-07-at-13.28.31/screen-shot-2016-12-07-at-13.28.31.png">


<h3>Start the virtual machine</h3>

<p>From your terminal, inside the <strong>vagrant</strong> subdirectory, run the command <code>vagrant up</code>. 
This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) 
depending on how fast your Internet connection is.</p>

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488603_screen-shot-2016-12-07-at-13.57.50/screen-shot-2016-12-07-at-13.57.50.png">


<p>When <code>vagrant up</code> is finished running, you will get your shell prompt back. At this point, 
you can run <code>vagrant ssh</code> to log in to your newly installed Linux VM!</p>

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488962_screen-shot-2016-12-07-at-14.12.29/screen-shot-2016-12-07-at-14.12.29.png">


<h3>Logged in!</h3>

<p>If you are now looking at a shell prompt that starts with the word <code>vagrant</code> (as in the above screenshot), 
congratulations — you've gotten logged into your Linux VM.</p>

<h3>Download the data</h3>

<p>Next, <a target="_blank" href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">download 
the data here.</a> You will need to unzip this file after downloading it. The file inside is called <code>newsdata.sql</code>.
Put this file into the <code>vagrant</code> directory, which is shared with your virtual machine.</p>
<p>To build the reporting tool, you'll need to load the site's data into your local database. 
<p>To load the data, <code>cd</code> into the <code>vagrant</code> directory and use the 
command <code>psql -d news -f newsdata.sql</code>.<br>Here's what this command does:</p>
<ul>
<li><code>psql</code> — the PostgreSQL command line program</li>
<li><code>-d news</code> — connect to the database named news which has been set up for you</li>
<li><code>-f newsdata.sql</code> — run the SQL statements in the file newsdata.sql</li>
</ul>
<p>Running this command will connect to your installed database server and execute the SQL commands in the downloaded file,
  creating tables and populating them with data. </p>


<h3 >Running the database</h3>
<p>The PostgreSQL database server will automatically be started inside the VM. You can use the <code>psql</code> command-line 
tool to access it and run SQL statements:</p>
<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58489186_screen-shot-2016-12-07-at-14.46.25/screen-shot-2016-12-07-at-14.46.25.png">

<h3>Logging out and in</h3>
<p>If you type <code>exit</code> (or <code>Ctrl-D</code>) at the shell prompt inside the VM, 
you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same
directory and type <code>vagrant ssh</code> again.</p>
<p>If you reboot your computer, you will need to run <code>vagrant up</code> to restart the VM.</p>

<h3>Create the Report</h3>
<ul>
	<li> Once you have the data loaded into your database, connect to your database using <code>psql -d news</code></li>
	<li> Create the <code> <a href="#views">views </a></code> in Views section.</li>
	<li> Run the report <code>python loganalysis.py</code></li>

</ul>
then the report will be printing for you.

<h3 id="views">Views</h3>

<h4> articleviews </h4>

<p> This views is used to display the title and total views for each articles by joining articles and log tables.</p>

```sql

	create view articleviews as (
	select title, count(*) as views 
	from articles, log 
	where '/article/' || articles.slug = log.path 
	group by(title) 
	order by(views) desc
	);

```

<h4> authorviews </h4>

<p> This views is used to display the author id and total views for each author by joining articles table  and articleviews view.</p>

```sql

	create view authorviews as (
	select articles.author, articleviews.views 
	from articles join articleviews 
	on articles.title= articleviews.title 
	order by(articles.author)
	);
  
```
<h4> dayerrors </h4>

<p> This views is used to display the total errors that occured in each day  from log table</p>

```sql

	create view dayerrors as(
	select time::date as date, 
	count(*) as errors 
	from log 
	where status='404 NOT FOUND' 
	group by date 
	order by errors);
  
```

<h4> dayrequests </h4>

<p> This views is used to display the total requests that occured in each day  from log table</p>

```sql

	create view dayrequests as (
	select time::date as date, 
	count(*) as requests 
	from log 
	group by(date) 
	order by (requests) desc);

```

<h2>License</h2>
<p>This project is licensed under the <a href="https://github.com/MayAlalawi">MIT</a> License.</p>