import React, { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.css';
import { Container, Row, Col } from 'react-bootstrap/Container';

const Grid = (props) => {
  const size = props.dimension

  [ formData, setFormData ] = useState(
    Array.from('x'.repeat(size * size))
  )

  function onSubmit(formData) {
    console.log(formData)
  }

  return (
    <div>
      <h1>Hello This is the grid</h1>
      <Container>
        {Array(size).map((_, i) => {
          return(<Row>
            {Array(size).map((_, j) => {
              return(<LetterInput i={i} j={j}/>)
            })}
          </Row>)
        })}

      </Container>

    </div>
  )

}