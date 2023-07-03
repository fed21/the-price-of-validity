# The price of validity
The price of validity, an important paper assigned as a practical project for the course of Dependable Distributed Systems at Sapienza University of Rome.

Mayank Bawa, Aristides Gionis, Hector Garcia-Molina, Rajeev Motwani:
The price of validity in dynamic networks. J. Comput. Syst. Sci. 73(3): 245-264 (2007)
https://doi.org/10.1016/j.jcss.2006.10.007

In particular, the analysis must consider different dynamic networks, highlighting how the performance metrics change on different networks.

# How to start project
* Clone the repository.
* Execute in command line prompt, in the repository:

        pip install -r requirements.txt

* Retrieve a url from cloud amqp service: https://www.cloudamqp.com/
* Open start.ipynb file.
* Execute each code block in "Initial stuff" section:
	* Execute code block "Imports" to import all required libraries.
	* Execute code block "Constants" to set constants variable used in the code.
	* Define in code block "User definable variables":
	  * The url to cloud amqp message broker.
	  * Boolean to enable host's failures.
	  * Number of hosts.
	  * Value of the variable "c".
	* Execute code block "User definable variables".
	* Execute code block "Methods for docker-compose and neighbors" to define methods that are used to build neighbors list and to populate docker-compose.yml file.
	* Execute code block "Methods to retrieve data" to define methods that retrieve and print data on query execution.
	* If there exists older results in folder "results", execute code block in "Clear results folder".
* Execute preferred code block in "Create Topology": choose between "Random Topology" or "Powerlaw Topology" to generate the corresponding topology. 
* Execute code block in "Generate docker-compose file" to generate in each folder of the two algorithm the docker-compose.yml file, following the structure of topology generted in the previous step.
* Execute code block in "Docker Compose Up" choosing between the two supported algorithm: "Spanning-Tree" or "WildFire". Each code block will build the corresponding docker image and will compose the stack of nodes. 
* Once the hosts are up, execute code block in "Start query" defining in the variable "query_host" the id of the host from which the query will start. This will also print the results of the query with interesting parameters.
* If an algorithm with host failures is executed, we suggest to purge queues in order to keep them clear executing code block in "Purge queues"
