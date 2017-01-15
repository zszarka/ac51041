Welcome to instant MyFlix on Docker<br/>
Tested on Ubuntu 16.04<br/>
Clone or download the project onto your filesystem
for testing<br/>
The system currently consists of:<br/>
<ul>
	<li>Player: Front end application server</li>
	<li>Nginx: Video Streaming (as Designed by Andy Cobley)</li>
	<li>Login: Flask API with mongodb</li>
	<li>Catalog: Flask API with mongodb</li>
	<li>Session: Flask API with redis (not fully integrated)</li>
</ul>
cd ac51041/v2
chmod +x start.sh stop.sh pause.sh resume.sh 
<h2>Starting up the system:</h2>
<ol>
	<li>Stop and remove all project containers (remove persisting data)</li>
	<li>Build Containers (docker-compose build)</li>
	<li>Start them in deamon mode (docker-compose up -d)</li>
	<li>Import Data (sample users and videos) from folders linked to directories on the host</li>
</ol>
sudo ./start.sh
<h2>Stop Services</h2>
Stop and remove all project containers (remove persisting data)<br/>
./stop.sh
<h2>Pause and Resume</h2>
Stop and start containers without loosing persisting data