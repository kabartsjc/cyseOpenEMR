# cyseOpenEMR

1) Prepare the WSL to run the project. In the terminal run this command:

    wsl --install -d Ubuntu

2) Define Ubuntu as the main distribution

    wsl --set-default Ubuntu

    wsl --list --verbose


3) In the VS Code

    - Type Ctrl + Shift + P

    - Select  “WSL: Connect to WSL”

4) In the wsl shell, clone the repo

    git clone https://github.com/kabartsjc/cyseOpenEMR.git

5) Update the env variables

    cp .env.example .env

6) Enter in the Docker Windows configuration 

    - Click on Settings --> Resources → WSL Integration --> Enable integration with my default WSL distro --> Ubuntu
    - Restart Docker

    - check if the changes work
        
        docker version
        
        docker compose version

    - Add the user to have permissions in Docker

        sudo usermod -aG docker $USER

7) In the Windows terminal, run these commands

    wsl --shutdown

    wsl

    - wait few seconds and reopen the vscode


8) Run the Docker compose commands
    
    docker compose up -d
    
    docker compose run --rm seed

7) 