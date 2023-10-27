
//function declaration
function getLocation(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(showCoordinates, handleError);
    }
    else{
        alert("Live location not supported by this browser. Please update this Browser.");
    }
}

// function to handle the success call back
function showCoordinates(position){
    var lattitude = position.coords.lattitude;
    var longitude = position.coords.longitude;

}

//function to handle the error callback
function handleError(error){
    switch(error.code){
        case error.PERMISSION_DENIED:
           alert("request denied");
           break;
        case error.POSITION_UNAVAILABLE:
           alert("not available");
           break;
        case error.TIMEOUT:
           alert("timeout");
           break;   
        case error.UNKNOWN_ERROR:
           alert("unknown error");
           break;
    }
}