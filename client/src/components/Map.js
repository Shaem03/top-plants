import {GoogleMap, useLoadScript} from "@react-google-maps/api";
import LocationMarker from "./LocationMarker";

const libraries = ["places"];

const Map = ({plantsData, center, mapContainerStyle}) => {
    const {isLoaded, loadError} = useLoadScript({
        googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
        libraries
    })

    const markers = plantsData.map(data => {
        return <LocationMarker info={data} />
    })


    if (loadError) return "Error on Loading Maps"

    if (!isLoaded) return "Loading Maps"

    return (
        <div className="map">
            <GoogleMap center={center} zoom={5} mapContainerStyle={mapContainerStyle}>
                {markers}
            </GoogleMap>
        });
        </div>
    )
}

Map.defaultProps = {
    center: {lat: 37.0902, lng: -95.7129},
    mapContainerStyle: {
        width: '100vw',
        height: '100vh'
    }
}
export default Map