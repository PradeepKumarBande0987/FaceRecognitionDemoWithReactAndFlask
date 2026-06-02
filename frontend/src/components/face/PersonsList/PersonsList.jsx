import React from 'react';
import './PersonsList.css';
export default function PersonsList({ persons=[] }) { return <div className="persons-list">{persons.map((p,i)=><div key={i}>{p.name}</div>)}</div>; }
