# The price of validity
The price of validity, an important paper assigned as a practical project for the course of Dependable Distributed Systems at Sapienza University of Rome.

Mayank Bawa, Aristides Gionis, Hector Garcia-Molina, Rajeev Motwani:
The price of validity in dynamic networks. J. Comput. Syst. Sci. 73(3): 245-264 (2007)
https://doi.org/10.1016/j.jcss.2006.10.007

In particular, the analysis must consider different dynamic networks, highlighting how the dependability metrics change on different networks.

# Define topology
* Open start.ipynb file
* Execute each code block in "Initial stuff" section setting number of hosts
* Execute preferred code block in "Random Topology" or in "Powerlaw Topology"
* Execute code block in "Generate docker-compose file"
* Open terminal and run
        
        docker build -p my_image .
        docker compose -p nodes up -d

* In start.ipynb file execute code block in "Start query"
* In start.ipynb file execute code block in "Stop container" defining seconds and container's name
