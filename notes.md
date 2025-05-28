# Port:
5071

# Docker image build command:
docker build -t bell-d20-img .

# Docker image run command:
docker run -p 5071:5071 bell-d20-img
<!-- To run without a console use -d argument -->
docker run -d -p 5071:5071 bell-d20-img
hub
# Project Tree
📦Bell_D20
 ┣ 📂app
 ┃ ┣ 📂static
 ┃ ┃ ┗ 📂css
 ┃ ┃ ┃ ┣ 📜input.css
 ┃ ┃ ┃ ┗ 📜tailwind.css
 ┃ ┗ 📜main.py
 ┣ 📜.gitignore
 ┣ 📜Dockerfile
 ┣ 📜LICENSE
 ┣ 📜notes.md
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜tailwind.config.js
