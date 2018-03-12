# setup.sh creates a docker

# sudo docker build -t docktest2 - < cmpe202w2018pavloVlastos
sudo docker build -t docktest2 - < ce202w18pvdock2

#curl benchmarks/cmpe202w2018pavloVlastos | docker build -f

#sudo docker build -t benchmarks -f ./cmpe202w2018pavloVlastos .
# could not get the above this commented out command to work.
# sudo docker rm $(sudo docker ps -a -q -f status=exited)
# sudo docker system prune -a
