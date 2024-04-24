import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css";
import "leaflet-defaulticon-compatibility";
import 'leaflet-routing-machine/dist/leaflet-routing-machine.css'
import 'leaflet-routing-machine'
import { useState, useEffect } from "react";
import L from 'leaflet'

const Map = () => {
  const [position, setposition] = useState([
    13.336818775814127, 74.74331442902206,
  ])

  function Routing() {
    const map = useMap()

    useEffect(() => {
      if (!map) return

      const routingControl = L.Routing.control({
        waypoints: [
          L.latLng(13.336818775814127, 74.74331442902206),
          L.latLng(13.352385434556018, 74.7927110262844),
        ],
        addWaypoints: false,
        routeWhileDragging: true,
        autoRoute: true,
        //    geocoder: true,
      }).addTo(map)

      //  map.remove()
      //return () => routingControl.removeFrom(map)
    }, [map])

    return null
  }

  return (
    <MapContainer
      center={[13.336818775814127, 74.74331442902206]}
      zoom={15}
      scrollWheelZoom={false}
      style={{ height: '100%', width: '100%' }}
    >
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Routing/>
      {/* <Marker
        position={[13.336818775814127, 74.74331442902206]}
        draggable={true}
      >
        <Popup>Hey ! I live here</Popup>
      </Marker> */}
    </MapContainer>
  )
};

export default Map;
