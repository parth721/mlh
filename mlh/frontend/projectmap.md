**How should our algorithm look like ?** 
a. when the submit button is clicked, country-code, lat & lon data send to algorithm
b. all the data's around that range all will be selected. eg: 12.34%
c. check the country code is same for all of them
d. measure the distance in between them.
e. select all the  names  & phone no. which lie between 800 to 3km
f. display the output.


**Further improvements**
* due to it their will be some geo-arbritrage. Like to deal with them ML implementation. (regression & clustering) to reduce the opprtuinity inequality.
* For privacy, we don't provide the phone no. instead provide a calling facility from our app.
* apply DS for searching & calculation. For large dataset.

* add logout & delete account feature.
* parsonalized welcome page.
* sending notification when find a match.
* review system. 
* having guidlines for user & partners for safe working environment
* pay as you go model.
* online transaction system.
* Audio asistance.
* light & dark theme.
* add partner concerns session before showing match.

RUN apt-get update && \
    apt-get upgrade -y libssl1.1 && \
    apt-get upgrade -y perl-base && \
    apt-get upgrade -y zlib1g && \
    apt-get upgrade -y gcc-12-base && \
    apt-get upgrade -y libgcc-s1 && \
    apt-get upgrade -y libgnutls30 && \
    apt-get upgrade -y libstdc++6 && \
    apt-get upgrade -y login && \
    apt-get upgrade -y passwd 