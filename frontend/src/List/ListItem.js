import React from "react";

function ListItem(props) {
    return (
        <li>
            {props.text}
            <button onClick={() => props.removeItem(props.id)}>Remove</button>
        </li>
    );
}

export default ListItem;