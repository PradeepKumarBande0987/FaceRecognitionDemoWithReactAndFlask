import { useState, useEffect } from 'react';
export default function useLiveRecognition(){ const [running, setRunning] = useState(false); useEffect(()=>{},[]); return { running, setRunning }; }
