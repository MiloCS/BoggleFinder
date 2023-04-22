import React from 'react'

const NavBar = (props) => {

  return(
    <ul>
      <li>
        <h1>
          Hello World
        </h1>
      </li>
      <li>
        <h1>
          Hello Milo
        </h1>
      </li>
      {props.message && (
        <li>
          <h1>
            {props.message}
          </h1>
        </li>
      )}
    </ul>
  )
}

export default NavBar;
