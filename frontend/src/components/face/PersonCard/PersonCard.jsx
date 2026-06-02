import React from 'react';
import './PersonCard.css';
export default function PersonCard({ person }) { return <div className="person-card">{person?.name || 'Person'}</div>; }
