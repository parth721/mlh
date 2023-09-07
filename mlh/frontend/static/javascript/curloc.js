navigator.geolocation.getCurrentPosition(successlocation, errorlocation, {
    enableHighAccuracy: true
})

function successlocation(position) {
    console.log(position)
}

function errorlocation() {
    console.log("error in geocoding")
}