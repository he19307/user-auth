Step 1.
Create a new Docker network and name it api_network:

docker network create api_network

Step 2.
Build  Docker container images:

docker-compose build

Step 3.
run  Docker container images:

docker-compose up

Step 4.
Prepare each REST api ORM mysql database:

	for service in battery-service; 
	 do
	   docker exec -it $service flask db init;
	   docker exec -it $service flask db migrate -m "removel primary key migration";  
	   docker exec -it $service flask db upgrade; 
	 done

Step 5. 
	i) add data in mysql database :

 curl -X POST -H "Content-Type: application/json" -d '{"id":"1", "voltage": 12.5, "current": 5.2, "latitude": 40.7128, "longitude": -74.0060}' http://localhost:1111/addbatterydata
 
  response:
     {
     id : int,
     "voltage": float,
     "current": float,
     "latitude": float,
     "longitude": float 
     }, 201
     
	ii) get data of particular id:

 curl -X POST -H "Content-Type: application/json" -d '{"id":2}' http://127.0.0.1:1111/getbatterydata

 response:
     {
     id : int,
     "voltage": [float, float],
     "current": [float, float],
     "latitude": [float, float],
     "longitude": [float, float]
     }, 201
 
