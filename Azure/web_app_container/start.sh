sudo docker build -t flaskr_image:v1.0 .
sudo docker run -it -d -p 5000:5000 --network mynetwork --name flaskr_container flaskr_image:v1.0