"use client"

import { useMemo, useState } from "react"

const demo = [
  { supermarket: "Kipper", price: "1.39" },
  { supermarket: "Viva Fresh", price: "1.49" },
  { supermarket: "Meridian Express", price: "1.55" },
]

export default function Home() {
  const [query, setQuery] = useState("")
  const rows = useMemo(() => demo.filter(x => x.supermarket.toLowerCase().includes(query.toLowerCase())), [query])
  const lowest = Math.min(...demo.map(x => Number(x.price)))
  return <main style={{maxWidth:1000,margin:"40px auto",padding:24,fontFamily:"system-ui"}}>
    <h1>Kosovo Supermarket Price Tracker</h1>
    <p>Compare prices from permitted public supermarket sources.</p>
    <input aria-label="Search supermarket" placeholder="Search supermarket" value={query} onChange={e=>setQuery(e.target.value)} style={{padding:12,width:"100%",maxWidth:420}} />
    <h2 style={{marginTop:32}}>Example comparison</h2>
    <table style={{width:"100%",borderCollapse:"collapse"}}><thead><tr><th align="left">Supermarket</th><th align="right">Price</th><th align="right">Status</th></tr></thead><tbody>{rows.map(x=><tr key={x.supermarket}><td style={{padding:12}}>{x.supermarket}</td><td align="right">€{x.price}</td><td align="right">{Number(x.price)===lowest?"CHEAPEST":""}</td></tr>)}</tbody></table>
    <p style={{marginTop:24}}>Live observations will replace the example data after the collectors are connected to the production database.</p>
  </main>
}
