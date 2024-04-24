'use client'
import React, { useRef, useEffect, useState } from 'react';
import * as maptilersdk from '@maptiler/sdk';
import "@maptiler/sdk/dist/maptiler-sdk.css";
import './map.css';

interface Coordinates {
  lat: number;
  lng: number;
}

export default function Map() {
  const Mapcontainer = useRef<HTMLDivElement>(null);
  const map = useRef<maptilersdk.Map | null>(null);
  const udupi: Coordinates = { lat: 13.340924790682903, lng: 74.74311446677487 };
  const [zoom] = useState<number>(16);
  const apiKey = process.env.NEXT_PUBLIC_MAPTILER;

  useEffect(() => {
    if (map.current) return;

    map.current = new maptilersdk.Map({
      container: Mapcontainer.current!,
      style: maptilersdk.MapStyle.SATELLITE,
      center: [udupi.lng, udupi.lat],
      zoom: zoom,
      apiKey: apiKey
    });

  }, [udupi.lng, udupi.lat, zoom]);

  return (
    <div className="map-wrap">
      <div ref={Mapcontainer} className="map" />
    </div>
  )
}

