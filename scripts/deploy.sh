# create remotely the app folder
ssh -p 22 administrateur@devincidocker01003.northeurope.cloudapp.azure.com 'mkdir app'
# copy files from app folder to the remote app folder
scp -r ./app/* administrateur@devincidocker01003.northeurope.cloudapp.azure.com:~/app/*
# copy the docker-compose file to the remote
scp docker-compose.yml administrateur@devincidocker01003.northeurope.cloudapp.azure.com:~/
# docker-compose up on the remote 
ssh -p 22 administrateur@devincidocker01003.northeurope.cloudapp.azure.com 'sudo docker-compose up --build'