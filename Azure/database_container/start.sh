sudo docker build -t postgres_image:v1.0 .
sudo docker run -d -p 5432:5432 --network mynetwork --name postgres_container postgres_image:v1.0