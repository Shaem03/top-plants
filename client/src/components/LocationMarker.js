import {InfoWindow, Marker} from "@react-google-maps/api";
import {useState} from "react";

const LocationMarker = ({info}) => {
    const [activeMarker, setActiveMarker] = useState(null);

    const handleActiveMarker = (marker) => {
        if (marker === activeMarker) {
            return;
        }
        setActiveMarker(marker);
    };

    return (
        <div className="location-marker">
            {/*<Marker position={{lat: lat, lng: lng}}/>*/}
            <Marker
                key={info.seq_number}
                position={{lat: info.plant_latitude, lng: info.plant_longitude}}
                onClick={() => handleActiveMarker(info.seq_number)}
            >
                {activeMarker === info.seq_number ? (
                    <InfoWindow onCloseClick={() => setActiveMarker(null)}>

                        <div className="location-info">
                            <h3>Plant Name: {info.plant_name}</h3>
                            <ul>
                                <li>Annual Net Generation: <strong>{ info.annual_net_generation }</strong></li>
                                <li>Nuclear Percentage: <strong>{ info.nuclear_generation_percent }</strong></li>
                                <li>Gas Genration Percentage: <strong>{ info.gas_generation_percent }</strong></li>
                                <li>Total Combustion Percentage: <strong>{ info.total_combustion_percent }</strong></li>
                                <li>Total Non Combustion Percentage: <strong>{ info.total_non_combustion_percent }</strong></li>
                            </ul>
                        </div>
                    </InfoWindow>
                ) : null}
            </Marker>
        </div>
    )
}

export default LocationMarker