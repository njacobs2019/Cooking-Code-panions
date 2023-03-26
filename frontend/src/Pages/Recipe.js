import React from 'react'
import List from './../List/List';

export default function Recipe() {
  return (
    <>
      <div style={{display: 'flex'}}>
        <div style={{flex: 1}}>Ingredients<List/></div>
        <div style={{flex: 1}}>Instructions<List/></div>
      </div>
    </>
  )
}
