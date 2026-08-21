const demo = [
  { product: 'Coca-Cola 2L', stores: [{name:'Kipper', price:'1.39'}, {name:'Viva Fresh', price:'1.49'}, {name:'Meridian', price:'1.55'}] },
  { product: 'Milk 1L', stores: [{name:'Viva Fresh', price:'1.19'}, {name:'Kipper', price:'1.25'}, {name:'Meridian', price:'1.29'}] },
]

export default function Home() {
  return (
    <main style={{maxWidth:1100,margin:'0 auto',padding:'32px 20px',fontFamily:'system-ui'}}>
      <h1>Kosovo Supermarket Prices</h1>
      <p>Compare prices collected from permitted public supermarket sources.</p>
      <div style={{marginTop:32,display:'grid',gap:20}}>
        {demo.map(item => {
          const lowest = Math.min(...item.stores.map(s => Number(s.price)))
          return <section key={item.product} style={{border:'1px solid #ddd',borderRadius:12,padding:20}}>
            <h2>{item.product}</h2>
            {item.stores.map(s => <div key={s.name} style={{display:'flex',justifyContent:'space-between',padding:'10px 0'}}>
              <span>{s.name}</span><strong>{s.price} € {Number(s.price)===lowest ? '— CHEAPEST' : ''}</strong>
            </div>)}
          </section>
        })}
      </div>
      <p style={{marginTop:30,fontSize:13,opacity:.7}}>Demo values only. Live observations will replace these after the collection pipeline is connected to the database/API.</p>
    </main>
  )
}
